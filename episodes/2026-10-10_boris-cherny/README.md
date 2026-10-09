# Boris Cherny의 Claude Code 활용법 4단계: 지우고, 써 보고, 막힐 때만 되돌리기

- 영상: https://youtu.be/CbArZ2FFrAU (2026-10-10 19:00 공개 예정)
- 원본: Y Combinator 대담 "Boris Cherny: We Cut 80% of Claude Code's Prompt" https://www.youtube.com/watch?v=qyPCVqFUyDo
- 바로 쓰는 체크리스트: [checklist.md](checklist.md)
- 실행 키트(48시간 한정, 2026-10-12 19:00 KST까지): [빼기 실험 프롬프트](kit/prompt_subtraction_experiment.md) · [우리가 먼저 돌려 본 결과](kit/example_result.md). Claude Code에 붙여 넣으면 지시 파일이 있을 때와 뺐을 때를 같은 과제로 비교하고, 되돌릴 지시만 골라 줘요. 요약과 체크리스트는 기간이 끝나도 남아요.

## 요약
새 모델이 나오면 지시문을 늘리지 말고 먼저 지웁니다. 평소 일을 그대로 맡겨 보고, 같은 곳에서 계속 막힐 때만 지시를 한 줄씩 되돌립니다. 어려운 일을 맡길 때는 할 일, 지킬 선, 끝 기준과 함께 모델이 스스로 확인할 방법(테스트, 화면 비교)을 줍니다.

## 영상에 나온 옵션 (Claude Code CLI 도움말 v2.1.287에서 확인)
```
claude --system-prompt "내가 쓴 지시문"   # 시스템 프롬프트를 내 글로 바꾸기
```
연사가 말한 심플 모드는 `CLAUDE_CODE_SIMPLE=1` 환경 변수입니다. 도움말에 따르면 이 모드(`--bare`)는 OAuth 로그인을 읽지 않으므로, API 키 없이 켜면 로그인이 안 될 수 있습니다.

## 출처
연사의 말은 옮겨 싣지 않고 우리 말로 요약했습니다. 단계 이름과 체크리스트의 세부 문장(옮겨 두기, 두 번 넘게 막히면 되돌리기, 맡기는 글 틀)은 우리 제안입니다.
