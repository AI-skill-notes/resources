# 자동 압축 시점 정하기

출처: Claude Code 공식 문서 https://code.claude.com/docs/en/model-config · https://code.claude.com/docs/en/env-vars

## 1. 명령 한 줄 (지금 모델, 이번 세션과 다음 세션)
```
/autocompact 140k
```
- 사용자 설정의 현재 모델 항목(`modelSettings`)에 저장되고 지금 세션에도 바로 적용됩니다.
- 기본값으로 돌아가기: `/autocompact auto`
- 설정할 수 있는 범위는 100K부터 모델의 대화 창 크기까지입니다.

## 2. 설정 파일 (모든 모델)
`~/.claude/settings.json`
```json
{
  "autoCompactWindow": 140000
}
```
- 같은 파일에서 `/autocompact`로 모델별로 저장한 값이 있으면 그 모델에는 그 값이 먼저입니다.

## 3. 한 번 실행할 때만
```
claude --autocompact 140k
```
- 저장해 둔 설정은 바꾸지 않습니다. `claude --autocompact auto`는 저장값이 있어도 기본 창으로 실행합니다.

## 4. 스크립트 · 클라우드 환경
환경 변수 `CLAUDE_CODE_AUTO_COMPACT_WINDOW`를 설정하면 명령 · 옵션 · 설정 파일보다 먼저 적용됩니다.

## 참고: 서브에이전트
Claude Code 2.1.296부터 서브에이전트 frontmatter와 `--agents`에도 `autoCompactWindow`를 쓸 수 있습니다(공식 CHANGELOG).

140k는 Matt Pocock의 경험칙입니다. 답이 흐려지기 시작할 때의 `/context` 숫자를 기록해 내 작업에 맞는 선을 찾아 보세요.
