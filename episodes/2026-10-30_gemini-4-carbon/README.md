# 구글 새 모델 Gemini 4 Carbon: 공식 비교표 17개 시험, 가격, 지금 쓸 수 있는 곳

- 영상(AI스킬노트 쇼츠, 10월 30일 저녁 6시 공개): 공개 뒤 이 줄에 주소를 붙여요.
- 출처 1: Google DeepMind 'Gemini 4 Carbon model evaluation'(평가 방법 문서, 2026년 10월) https://deepmind.google/models/evals-methodology/gemini-4-carbon
- 출처 2: Google 'Gemini 4 Carbon: our next frontier model'(2026-10-28) https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
- 정리한 날: 2026-10-29. 아래 숫자는 모두 구글이 낸 표에 적힌 값을 옮긴 거예요. 다른 회사 모델 점수도 구글 표에 적힌 값이고, 우리가 직접 잰 값은 없어요. 광고·협찬 아님.

## 어디서 쓸 수 있나요
- 이번 주는 사이버 보안을 지키는 일부 전문가에게만 열어요(구글 Fairwind 프로그램).
- 개발자·기업·일반 사용자에게는 안전장치를 더 다듬은 뒤 '최대한 빨리' 연다고만 했고, 날짜는 없어요.
- 지금 바로 쓸 수 있는 건 Gemini 4 Argon이에요(API·AI Studio, Gemini 앱 Pro·Ultra 요금제).

## 가격 (100만 토큰당)
| 구간 | 입력 | 출력 |
|---|---|---|
| 입문 가격(Argon과 같음) | 2달러 | 10달러 |
| 입문 기간이 끝난 뒤 | 4달러 | 20달러 |

- 캐시 입력은 입력 가격의 95% 할인이에요.
- 입문 기간이 언제 끝나는지는 적혀 있지 않아요.

## 공식 비교표 (17개 시험, 구글 표 그대로)
Carbon이 17개 중 15개에서 가장 높아요. 가장 높지 않은 두 줄은 굵게 표시했어요. '—'는 표에 값이 없는 칸이에요.

| 시험 | Gemini 4 Carbon | Gemini 4 Argon | GPT-6 Astra | Claude Opus 5.5 | Claude Fable 5.1 |
|---|---|---|---|---|---|
| AA Index v5.0 (종합 지수) | 59 | 50 | 57 | 58 | 49 |
| Vals Index v2.2 | 70.4 | 69.2 | 65.0 | 70.2 | — |
| SWE-sweep | 9.6 | 4.3 | 9.5 | 3.6 | 2.9 |
| **FrontierSWE 2 (실전 코딩 과제)** | 61.2 | 55.0 | **65.5** | 62.3 | 56.3 |
| Terminal-Bench 4.0 (터미널 코딩) | 65.2 | 57.1 | 59.1 | 59.6 | 52.0 |
| Agents' Last Exam v1.1 | 77.4 | 69.0 | 73.1 | 71.6 | — |
| **OSWorld-2.1 오프라인 (컴퓨터 조작)** | 81.5 | 74.7 | 80.9 | **87.2** | 76.8 |
| AutomationBench (Zapier) | 53.9 | 51.3 | 41.4 | 42.5 | 31.4 |
| Vending-Bench 2 (남은 돈, 달러) | 16,484 | 13,718 | 15,515 | 9,235 | 5,422 |
| Chartography | 72.5 | 71.6 | 71.0 | 66.3 | 46.2 |
| Blueprint-Bench 2 | 58.6 | 54.4 | 49.7 | 51.2 | 41.9 |
| GraphWalks (256k~1M) | 96.2 | 84.2 | 71.8 | 66.8 | 65.0 |
| RiemannBench | 80.0 | 76.0 | 72.0 | 69.6 | 65.6 |
| Terminal-Bench-Science 0.1 | 64.8 | 52.9 | 63.3 | 59.0 | 43.3 |
| CWE-bench | 71.0 | 68.0 | 68.0 | 67.0 | 58.0 |
| ExploitGym | 54.8 | 42.0 | 42.4 | 34.5 | — |
| SEC-bench Pro | 88.2 | 83.4 | 85.4 | — | — |

- 다른 회사 모델은 공개된 결과 중 가장 높은 추론 설정 값을 썼고, 공개 값이 없으면 구글이 쓸 수 있는 최선의 설정으로 잰 값이라고 문서에 적혀 있어요.

## 표 읽는 법 체크리스트
- [ ] 1위 개수보다, 내가 실제로 맡기는 일과 비슷한 시험 줄부터 본다(코딩이면 Terminal-Bench·FrontierSWE, 화면 조작이면 OSWorld).
- [ ] 다른 회사 점수가 누가 잰 값인지 본다. 이 표는 구글이 정리한 값이에요.
- [ ] 같은 모델 버전·같은 추론 설정끼리 비교하는지 본다.
- [ ] 지금 쓸 수 있는 모델인지, 가격이 입문가인지 정가인지 본다.
