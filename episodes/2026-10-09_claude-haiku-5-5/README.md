# Claude Haiku 5.5: 이전 모델과 같은 시험으로 비교한 공식 점수와 가격

- 원본(Anthropic 발표 글, 2026-10-07): https://www.anthropic.com/claude-haiku-5-5
- 바로 쓰는 체크리스트: [checklist.md](checklist.md)

## 시험별 점수 (Anthropic 발표 표 그대로)
점수는 시험 하나 안에서만 비교합니다. 시험끼리 점수를 비교하지 마세요. 점수가 높다고 모든 일에 최강이라는 뜻은 아닙니다.

| 시험 | Haiku 5.5 | Haiku 4.5 | GPT-6 Luna | Sonnet 5.5 |
|---|---|---|---|---|
| Terminal-Bench 4.0 (터미널 코딩) | 39.2점 | 0.0점 | 16.4점 | 70.6점 |
| OSWorld 2.1 (컴퓨터 조작, 오프라인 일부) | 72.4점 | 15.7점 | 48.9점 | 83.9점 |
| GDPval-AA v2.1 (업무 지식, Elo) | 1620 | 735 | 1437 | 1840 |
| AA-Briefcase v1.1 (업무 지식, Elo) | 1578 | 614 | 1336 | 1824 |
| Humanity's Last Exam (도구 없음) | 45.9점 | 10.2점 | 없음 | 56.9점 |
| Humanity's Last Exam (도구 사용) | 57.4점 | 18.7점 | 없음 | 64.5점 |
| FrontierCode 1.1 (Main) | 46.4점 | 없음 | 42.4점 | 52.1점 |
| Chartography (도구 없음) | 46.4점 | 6.4점 | 29.1점 | 61.6점 |

## API 가격 (100만 토큰당, 프롬프트 10만 토큰 이하)
| | Haiku 5.5 | Haiku 4.5 | Sonnet 5.5 |
|---|---|---|---|
| 입력 | $0.10 | $1.00 | $2.00 |
| 출력 | $0.50 | $5.00 | $10.00 |

10만 토큰을 넘는 프롬프트는 Haiku 5.5도 입력 $0.50, 출력 $2.50입니다.

## 어디서 쓰나
- Claude.ai(웹, iOS, Android): 무료·Pro·Max·Team·Enterprise 모두 모델 목록에서 Haiku 5.5 선택 가능
- Claude Code에서도 사용 가능
- API 모델 이름: `claude-haiku-5-5`

## 출처
표의 숫자는 Anthropic 발표 글에서 옮겼고, 해석은 우리 말로 적었습니다. 모든 시험에서 Sonnet 5.5가 Haiku 5.5보다 높습니다. 싸고 빠른 일(요약, 분류, 서브에이전트 등)에 맞는 모델이라는 것이 발표 글의 설명입니다.
