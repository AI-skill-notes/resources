# 읽기·검색은 Haiku 서브에이전트에게

공식 문서: "For simple subagent tasks, specify model: haiku in your subagent configuration" (https://code.claude.com/docs/en/costs)

서브에이전트 파일 위치(공식 문서 https://code.claude.com/docs/en/sub-agents):
- 이 프로젝트에서만: 프로젝트 폴더의 `.claude/agents/`
- 모든 프로젝트에서: `~/.claude/agents/`

## 1. 읽기 전용 조수 만들기
`.claude/agents/reader.md` 로 저장하세요.

```markdown
---
name: reader
description: Reads and searches files without editing them, then returns a short summary. Use for broad file reading, log reading and code search.
tools: Read, Grep, Glob
model: haiku
---
You read and search files only. Never edit files.
Return a short summary: what you found, file paths with line numbers, and anything that looked wrong.
Keep the summary under 30 lines.
```

- `model: haiku` 한 줄이 핵심이에요. 이 줄이 없으면 서브에이전트는 보통 메인 대화와 같은 모델로 돌아요.
- `tools` 를 읽기 도구로만 두면 실수로 파일을 고치지 않아요.
- 쓰는 법: Claude Code에서 "reader 서브에이전트로 src 폴더를 훑어보고 요약해 줘"처럼 부탁하세요.

## 2. 기본 Explore 서브에이전트를 Haiku로 바꾸기
Claude Code에는 코드를 훑어보는 기본 서브에이전트 Explore가 있어요. 같은 이름의 파일을 만들면 기본값 대신 내 설정이 쓰여요.
공식 문서: "A user or project subagent named Explore overrides the built-in and keeps its own model field, so define one with model: haiku to run exploration on a lower-cost model."

`.claude/agents/explore.md` 로 저장하세요.

```markdown
---
name: Explore
description: Fast read-only agent for searching and analyzing codebases. Use when you need to find files, search code or understand a codebase without making changes.
tools: Read, Grep, Glob
model: haiku
---
Search and read the codebase to answer the question. Do not edit files.
Report file paths with line numbers and a short explanation.
```

## 3. 모든 서브에이전트를 한 모델로
공식 문서는 환경 변수 `CLAUDE_CODE_SUBAGENT_MODEL` 로 모든 서브에이전트에 한 모델을 강제하는 방법도 안내해요("Run every subagent on one model" 절). 어려운 작업을 하는 서브에이전트까지 Haiku가 되므로, 처음에는 위 1·2처럼 필요한 것만 바꾸는 쪽을 권해요.

## 주의
- Haiku는 빠르고 저렴한 대신, 복잡한 설계나 어려운 버그 수정에는 메인 모델이 더 나아요(영상 속 비유: Opus = 꼼꼼한 선배, Haiku = 빠르고 저렴한 조수).
- 가격은 모델 페이지(https://platform.claude.com/docs/en/models/opus-5-5/overview)의 비교표를 확인하세요. 영상 기준(2026-10-13): Opus 5.5 입력 $4 / MTok, Haiku 5.5 입력 $0.10 / MTok부터.
