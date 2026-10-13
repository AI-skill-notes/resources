# Claude Code 대화가 길어지면 답이 흐려지는 이유: 스마트 존과 지키는 법

- 영상(AI스킬노트, 10/17 토요일 저녁 7시 공개): https://youtu.be/IT9JYVKTGfA
- 바로 쓰는 체크리스트: [checklist.md](checklist.md)
- 설정 한 줄 · 인수인계 프롬프트 키트(영상 공개 후 48시간): [kit/](kit/)

## 영상 요약
1. **창은 질문 전에 이미 차 있다**: `/context`로 보면 시스템 프롬프트, 도구 설명, 스킬 목록, CLAUDE.md가 먼저 자리를 잡는다.
2. **길어지면 흐려진다**: Anthropic은 이를 컨텍스트 부패라고 부른다. 모델에게는 주의력 예산이 있고, 새 토큰이 들어올 때마다 그 예산을 쓴다.
3. **생각보다 빨리 닿는다**: 우리가 공개 저장소에서 잰 결과, 평범한 요청 두 번 만에 Matt Pocock이 말한 스마트 존 선에 닿았다(한 번 잰 값, 저장소마다 다름).
4. **기본 자동 압축은 그 선을 지켜 주지 않는다**: 기본값은 스마트 존을 한참 지나서야 정리를 시작한다.
5. **상황별 네 가지**: 새 일이면 `/clear`, 같은 일이면 `/compact` + 남길 것, 두 번 고쳤으면 `/clear` 뒤 더 구체적으로, 큰 일은 문서로 나누기.
6. **명령 한 줄**: `/autocompact`로 자동 압축 시점을 앞당길 수 있다.

## 출처
- 자동 압축 기본값 · 설정 방법: https://code.claude.com/docs/en/model-config
- 명령 목록: https://code.claude.com/docs/en/commands
- /clear · /compact · /rewind: https://code.claude.com/docs/en/best-practices
- 컨텍스트 엔지니어링(Anthropic): https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

요약과 체크리스트는 공식 문서를 바탕으로 한 우리 정리입니다. 스마트 존 선은 Matt Pocock의 경험칙입니다.
