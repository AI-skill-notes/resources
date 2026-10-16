# 토큰 점검표 (Claude Code · Opus 5.5)

> 왜: Claude Code는 요청할 때마다 대화 전체를 함께 보내요("Claude Code sends your full conversation with every request", https://code.claude.com/docs/en/costs).
> 140k 같은 선은 Matt Pocock의 좋은 습관이에요. 아래는 그 선을 지키는 공식 방법이에요.

## 시작할 때
- [ ] `/context` 로 무엇이 자리를 차지하는지 본다 ("Run /context to see what's consuming space.")
- [ ] 이번 작업이 이전 대화와 상관없다면 새 대화로 시작한다

## 일하는 중
- [ ] 다른 일로 넘어가면 `/clear` ("/clear costs nothing")
- [ ] 지금 대화를 나중에 다시 볼 것 같으면 `/clear` 전에 `/rename`, 돌아올 땐 `/resume`
- [ ] 같은 일을 이어 가야 하면 `/compact <남길 내용>`
      예: `/compact 테스트 결과와 바뀐 코드 위주로 남겨 줘`
      주의: `/compact` 는 대화 전체를 읽고 요약하는 큰 요청이에요. 일이 바뀌었으면 `/clear` 가 먼저.
- [ ] 파일을 많이 읽거나 검색만 하는 일은 Haiku 서브에이전트에게 (`haiku-subagent.md`)
- [ ] 간단한 일은 `/effort` 로 effort를 낮춘다 (Opus 5.5 기본값은 medium)
- [ ] 부탁은 구체적으로: '이 코드 좋게 해 줘' 대신 '로그인 함수에 입력 검사 추가'

## 확인
- [ ] `/usage` 로 지금까지 쓴 양을 본다
- [ ] 세션을 몇 시간째 열어 두었다면 정리할 때인지 본다
      ("A session that has been open for hours can use far more of your plan limits than your activity suggests")

## 참고
- Claude Code는 1M 창 모델에서 기본으로 약 967K 토큰쯤에 자동으로 정리해요(Claude Code 모델 설정 문서). 그 전까지는 계속 쌓이니 위 습관이 먼저예요.
- 모든 공식 문장은 2026-10-13 확인. 문서는 바뀔 수 있어요.
