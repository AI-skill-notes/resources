# 빼기 실험 도입해 보기 (Claude Code에 그대로 붙여 넣기)

당신은 시니어 개발 생산성 엔지니어다.
지금 열린 저장소에서 'CLAUDE.md·스킬·훅 같은 지시 파일을 빼도 결과가 같은가'를 재는 빼기 실험을 끝까지 실행하라. 설명만 하지 말고 파일을 만들고 실제로 실행하라. 사용자에게 추가 질문하지 말고 아래 기본값을 사용하라.

[목표]
같은 과제 3개를 (A) 지금 지시 파일 그대로, (B) 지시 파일을 뺀 상태로 각각 실행한다. 테스트 통과 여부, 바뀐 줄 수, 소요 시간, 대화 턴 수, 비용, 막힌 지점을 비교한다. 그리고 B에서 막힌 지점과 관련된 지시만 '되돌릴 후보'로 고른다. 지시를 늘리는 제안은 하지 않는다.

[절대 원칙]
1. 원본 지시 파일을 삭제하지 마라. B 작업 폴더에서만 옮기고, 원래 저장소의 파일은 처음과 끝의 해시가 같아야 한다.
2. 추적 중인 파일에 커밋하지 않은 변경이 있으면(`git status --porcelain --untracked-files=no`가 비어 있지 않으면) 시작하지 말고 이유를 남긴 뒤 종료 코드 2로 끝내라. 추적되지 않는 파일(`__pycache__`, 빌드 결과 등)은 worktree에 들어가지 않으므로 목록만 남기고 진행한다. `subtraction_report/`는 커밋하지 않는다.
3. 실험은 git worktree 두 개(`../_exp_A`, `../_exp_B`)에서 하고, 끝나면 반드시 정리하라(실패해도). main 브랜치에는 커밋·푸시하지 마라.
4. 수치는 실제 실행 결과에서만 쓴다. 측정하지 못한 값은 null로 두고 0으로 위장하지 마라.
5. `.env`·키·토큰 같은 비밀 파일은 읽지도 옮기지도 마라. 사용자 홈의 `~/.claude` 설정은 건드리지 마라.

[실행 그래프]
check_clean_tree → inventory → pick_tasks → baseline_tests → make_worktrees → (병렬 가능) run_A, run_B → compare → decide → restore_and_cleanup → write_report
어느 노드가 실패해도 restore_and_cleanup과 write_report는 실행하고, 실패한 노드 이름과 이유를 남겨라.

[노드 규칙]
- inventory: 저장소 안의 지시 파일 목록과 각 파일의 줄 수·해시를 `inventory.json`에 적는다.
  - 대상: CLAUDE.md(하위 폴더 포함), `.claude/skills/`, `.claude/settings.json`·`.claude/settings.local.json`의 hooks 블록, `.cursorrules`, `AGENTS.md`
- pick_tasks: 과제 3개를 `tasks.json`에 고정한다.
  - TODO·FIXME 주석 중 작은 것을 고른다.
  - 없으면 다음 셋을 쓴다: '가장 긴 함수 하나를 동작 변화 없이 나누기', '입력 검증 하나를 추가하고 테스트 작성', 'README의 실행 방법이 실제 명령과 맞는지 확인하고 고치기'.
  - A와 B에 글자 하나 다르지 않게 같은 문장을 준다.
- baseline_tests: 테스트 명령을 찾아(package.json scripts, pytest, go test, cargo test 등) 실행하고 기준 결과를 남긴다. 테스트가 없으면 '테스트 없음'을 적고, 과제마다 확인 명령을 하나씩 정한다.
- run_A / run_B: 과제마다 각 worktree에서 `claude -p "<과제 문장>" --output-format json`을 실행한다.
  - JSON 결과에서 duration_ms, num_turns, total_cost_usd를 읽는다.
  - 그다음 테스트·확인 명령을 다시 돌리고, `git diff --stat`의 바뀐 줄 수와 마지막 오류를 기록한다.
  - B worktree에서는 inventory의 지시 파일을 `.subtraction_parked/`로 옮긴 뒤 실행한다.
  - 비대화 실행이 편집 승인에서 멈추지 않게 A와 B 모두 같은 옵션을 쓴다: `--permission-mode acceptEdits`, 그리고 `--allowedTools`로 테스트·확인 명령만 허용한다.
  - 지시 파일에 적힌 규칙(예: 타입 힌트, docstring, 테스트 실행)은 결과 코드에서 직접 세어 A/B 표에 '규칙 준수' 칸으로 넣는다.
- compare: 과제별 A/B 표를 만든다. 같은 과제가 한쪽만 통과하면 그 차이를 맨 위에 적는다.
- decide: 각 지시 파일을 '빼도 됨(B가 같거나 나음)', '되돌릴 후보(B가 같은 곳에서 막힘, 관련 줄 인용)', '판단 불가(측정 부족)'로 나눈다. 근거 없는 판단을 만들지 마라.
- restore_and_cleanup: worktree를 지우고, 원래 저장소의 지시 파일 해시가 inventory와 같은지 `restore_check.txt`에 적는다.

[산출물] `subtraction_report/` 아래
- `report.md`: 사람이 읽는 요약, A/B 표, 되돌릴 후보 목록, 다음에 다시 해 볼 시점(새 모델이 나왔을 때 또는 6개월 뒤)
- `results.json`: 과제별 원 수치(null 허용)
- `inventory.json`, `tasks.json`, `restore_check.txt`
- `run_view.html`: 외부 CDN 없이 혼자 열리는 한 장짜리 HTML. 위 그래프의 노드가 실제 실행 순서와 소요 시간대로 차례로 켜지는 재생 화면이다.
  - 성공 ✓ 초록, 실패 ✕ 빨강, 건너뜀은 회색 점선
  - 노드를 클릭하면 입력·출력·오류를 보여 준다.
  - 기록된 결과만 재생하고 꾸며내지 않는다.

[완료 조건]
1. restore_check.txt에서 모든 해시가 일치한다.
2. worktree가 남아 있지 않다(`git worktree list`로 확인).
3. 마지막 답변에는 A/B 표, 되돌릴 후보, 실행한 명령, 측정하지 못한 항목만 간결하게 적는다.

> 참고: 과제 3개 × 2회 = `claude -p` 6번을 실행하므로 그만큼 사용량이 듭니다. 처음에는 작은 저장소에서 해 보세요.
