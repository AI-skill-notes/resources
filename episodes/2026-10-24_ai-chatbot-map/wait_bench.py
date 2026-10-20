# -*- coding: utf-8 -*-
"""AI스킬노트 A1 대기 실험: AI 챗봇 서버는 계산보다 '기다림'에서 막힌다.
실제 AI 대신 WAIT_S초 뒤에 답하는 시험용 서버를 두고, 채팅 서버 세 가지(한 번에 하나 / 스레드 8개 / 비동기)에
요청 USERS개를 한꺼번에 RUNS번 보내 '마지막 요청이 답을 받기까지 걸린 시간'을 잽니다.
파이썬 표준 라이브러리만, 내 컴퓨터(127.0.0.1) 안에서만 통신합니다.  실행: python wait_bench.py  -> results/
"""
import asyncio, json, socket, statistics, sys, threading, time
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
from pathlib import Path
from socketserver import ThreadingMixIn

sys.stdout.reconfigure(encoding="utf-8")
WAIT_S, USERS, RUNS = 2.0, 40, 5
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)
LLM_PORT, SRV_PORT = 18901, 18902


# ---------------------------------------------------------------- test AI server: answers after WAIT_S seconds (always concurrent)
class LLM(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(WAIT_S)
        self.send_response(200); self.send_header("Content-Length", "2"); self.end_headers(); self.wfile.write(b"ok")

    def log_message(self, *a):
        pass


class BigThreadingServer(ThreadingHTTPServer):
    request_queue_size = 1024
    daemon_threads = True


def call_llm_blocking():
    with socket.create_connection(("127.0.0.1", LLM_PORT)) as s:
        s.sendall(b"GET / HTTP/1.0\r\nHost: x\r\n\r\n")
        while s.recv(4096):
            pass


# ---------------------------------------------------------------- chat servers
class Chat(BaseHTTPRequestHandler):
    def do_GET(self):
        call_llm_blocking()
        self.send_response(200); self.send_header("Content-Length", "2"); self.end_headers(); self.wfile.write(b"hi")

    def log_message(self, *a):
        pass


class OneWorker(HTTPServer):
    request_queue_size = 1024


class PoolServer(ThreadingMixIn, HTTPServer):
    """Thread pool of fixed size (like a WSGI server with N workers)."""
    request_queue_size = 1024
    daemon_threads = True
    pool_size = 8

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self._pool = ThreadPoolExecutor(self.pool_size)

    def process_request(self, request, client_address):
        self._pool.submit(self.process_request_thread, request, client_address)


async def async_handle(reader, writer):
    await reader.readuntil(b"\r\n\r\n")
    r, w = await asyncio.open_connection("127.0.0.1", LLM_PORT)
    w.write(b"GET / HTTP/1.0\r\nHost: x\r\n\r\n"); await w.drain()
    await r.read()
    w.close()
    writer.write(b"HTTP/1.0 200 OK\r\nContent-Length: 2\r\n\r\nhi"); await writer.drain()
    writer.close()


def start_async_server():
    loop = asyncio.new_event_loop()

    async def main():
        srv = await asyncio.start_server(async_handle, "127.0.0.1", SRV_PORT, backlog=1024)
        async with srv:
            await srv.serve_forever()

    t = threading.Thread(target=lambda: loop.run_until_complete(main()), daemon=True)
    t.start()
    return loop


# ---------------------------------------------------------------- load
def one_user():
    t0 = time.perf_counter()
    with socket.create_connection(("127.0.0.1", SRV_PORT), timeout=600) as s:
        s.sendall(b"GET / HTTP/1.0\r\nHost: x\r\n\r\n")
        while s.recv(4096):
            pass
    return time.perf_counter() - t0


def burst():
    t0 = time.perf_counter()
    with ThreadPoolExecutor(USERS) as ex:
        waits = list(ex.map(lambda _: one_user(), range(USERS)))
    return time.perf_counter() - t0, statistics.median(waits)


def run_case(name):
    if name == "async":
        loop = start_async_server(); srv = None
    else:
        cls = OneWorker if name == "one" else PoolServer
        srv = cls(("127.0.0.1", SRV_PORT), Chat)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
    time.sleep(0.5)
    rows = [burst() for _ in range(RUNS)]
    if srv:
        srv.shutdown(); srv.server_close()
    else:
        loop.call_soon_threadsafe(loop.stop)
    time.sleep(0.5)
    return rows


if __name__ == "__main__":
    llm = BigThreadingServer(("127.0.0.1", LLM_PORT), LLM)
    threading.Thread(target=llm.serve_forever, daemon=True).start()
    res = {"date": time.strftime("%Y-%m-%d %H:%M"), "wait_s": WAIT_S, "users": USERS, "runs": RUNS, "cases": {}}
    term = [f"$ python a1_wait_bench.py   # AI answer takes {WAIT_S:g}s, {USERS} users at once, {RUNS} runs"]
    for name, label in (("one", "1 worker"), ("pool8", "8 workers"), ("async", "async")):
        rows = run_case(name)
        last = statistics.median(r[0] for r in rows)
        med = statistics.median(r[1] for r in rows)
        res["cases"][name] = {"label": label, "last_s": [round(r[0], 2) for r in rows], "median_wait_s": [round(r[1], 2) for r in rows],
                              "last_s_median": round(last, 1), "median_wait_s_median": round(med, 1)}
        line = f"{label:<10} last answer {last:6.1f}s   median wait {med:6.1f}s"
        term.append(line); print(line, flush=True)
    c = res["cases"]
    res["speedup_one_vs_async"] = round(c["one"]["last_s_median"] / c["async"]["last_s_median"], 1)
    md = [f"# A1 wait bench ({res['date']} KST, this PC, localhost, stdlib)", "",
          f"Test AI server answers after {WAIT_S:g} s (setting). {USERS} users send one message at the same time. {RUNS} runs per server; medians.", "",
          "| server | last answer (s) | median user wait (s) | runs (last answer) |", "|---|---|---|---|"]
    for k, v in c.items():
        md.append(f"| {v['label']} | {v['last_s_median']} | {v['median_wait_s_median']} | {v['last_s']} |")
    md += ["", f"one worker / async last-answer ratio: {res['speedup_one_vs_async']}x", "",
           f"text: with 1 worker the last of {USERS} users waited {c['one']['last_s_median']}s; with 8 workers {c['pool8']['last_s_median']}s; async {c['async']['last_s_median']}s."]
    (OUT / "results.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    (OUT / "results.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (OUT / "terminal.txt").write_text("\n".join(term) + "\n", encoding="utf-8")
    print("\n".join(md))
