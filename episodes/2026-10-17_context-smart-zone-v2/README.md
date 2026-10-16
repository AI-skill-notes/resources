# Claude Code 스마트 존, Opus 5.5에서 토큰 아끼기 (자료실)

> 📄 **PDF로 받기:** [claude_code_token_guide.pdf 바로 다운로드](https://github.com/AI-skill-notes/resources/raw/main/episodes/2026-10-17_context-smart-zone-v2/claude_code_token_guide.pdf) (7쪽) · [브라우저에서 보기](claude_code_token_guide.pdf)

영상: AI스킬노트 「Matt Pocock의 140k 스마트 존, Opus 5.5 공식 문서로 다시 보기」 (2026-10-17 공개 예정)

## 한 줄 요약
Matt Pocock의 140k 기준은 Opus 4.8로 일하던 구루의 경험칙이고, 지금도 좋은 습관이에요.
Opus 5.5에서는 그 선을 지키면 토큰과 시간을 아낄 수 있어요. Claude Code는 요청할 때마다 대화 전체를 함께 보내기 때문이에요.

## 이 폴더
| 파일 | 내용 |
|---|---|
| `claude_code_token_guide.pdf` | 영상에 나온 방법 5가지 + 덤 3가지 + 점검표 + 설정 파일을 모은 PDF(7쪽) |
| `haiku-subagent.md` | 읽기·검색만 하는 서브에이전트를 Haiku로 돌리는 설정 파일 두 가지(복사해서 쓰기) |
| `token-checklist.md` | 대화를 시작·전환·마무리할 때 보는 토큰 점검표 |

## 영상에 나온 공식 문장 (원문 링크)
- Claude Code 비용 문서: https://code.claude.com/docs/en/costs
  - "Claude Code sends your full conversation with every request"
  - "Stale context wastes tokens on every subsequent message."
  - "When you want a fresh start instead of continuity, /clear costs nothing"
  - "/compact reads the conversation it summarizes, so compacting a large context is itself a large request."
  - "For simple subagent tasks, specify model: haiku in your subagent configuration"
- Claude Code 서브에이전트 문서: https://code.claude.com/docs/en/sub-agents
  - "A user or project subagent named Explore overrides the built-in and keeps its own model field, so define one with model: haiku to run exploration on a lower-cost model."
- Claude Opus 5.5 프롬프트 가이드: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
- Claude Opus 5.5 새로 바뀐 점: https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5 (effort 기본값 medium)
- Claude Opus 5.5 모델 페이지(가격·출시일): https://platform.claude.com/docs/en/models/opus-5-5/overview

모든 문장은 2026-10-13에 공식 페이지에서 확인했어요. 문서는 바뀔 수 있으니 쓰기 전에 링크를 한 번 열어 보세요.

## 측정 값에 대해
영상의 19.6k → 116.8k → 140.3k, 그리고 '서브에이전트 단계 비용 4.8배'는 2026-10-11에 공개 저장소 하나에서 한 번 재 본 값이에요(Claude Code · Opus 5.5). 저장소와 작업에 따라 숫자는 달라져요.
