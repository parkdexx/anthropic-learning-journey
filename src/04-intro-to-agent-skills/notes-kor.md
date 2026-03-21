
## 스킬
- SKILL.md 파일에 기록된 지침.
- 로컬(모든 프로젝트) : ~/.claude/skills
- 단일 프로젝트 : .claude/skills
- 생긴 모습 :
```
name: pr-review
description: Reviews pull requests for code quality. Use when reviewing PRs or checking code changes.
```

- 클로드 코드는 사용자의 요청에 상황을 인식하여 -> 스킬을 알아서 사용한다

- CLAUDE.md VS "/" 커맨드 VS SKILL :
  * CLAUDE.md : 프로젝트의 전반적인 지침
  * "/" 커맨드 : 일회성 지침. 수동 사용 해야 함.
  * SKILL : 반복적인 작업에 대한 지침. 자동으로 사용됨.

## 스킬 메타데이터 필드
스킬 메타데이터 필드에는 이름, 설명 외에도 몇개 더 입력 가능.
```
name (required) — 폴더명과 똑같이. 64자 제한. 소문자만 쓰셈.
description (required) — 클로드가 언제 이 스킬을 쓸지에 대한 설명. 1024자 제한.
allowed-tools (optional) — 이 스킬이 실행될 때 클로드가 사용할 수 있는 권한. 안적으면 제약없이 다씀.
model (optional) — 닭 잡는데 소 잡는 칼을 쓸 순 없으니, 모델 제한.
```

## 스킬++
스킬의 내용이 깊고 방대해질 경우...
SKILL.md 파일에 모든 내용을 다 때려박는건 토큰의 낭비가 됨으로 ->
- /scripts : 스크립트 파일
- /references : 레퍼런스 파일
- /assets : 이미지, 영상 등 에셋 파일
와 같이 폴더링해서 각각에 적절한 설명, 파일, 코드 넣어 놓고
SKILL.md 에는 좌표만 찍어 주는 걸로 운영하면 됨.

SKILL.md 파일은 500줄 미만으로 운영해라.

## 정리
- CLAUDE.md — 상시 가동되는 프로젝트 표준
- Skills — 필요할 때 불러오는 작업별 전문 지식
- Hooks — 이벤트 발생 시 자동으로 실행되는 작업
- Subagents — 위임된 작업을 위한 독립적인 실행 컨텍스트
- MCP servers — 외부 도구 및 통합

## 서브에이전트
- 사용 이유 : 메인 컨텍스트 오염 방지

- 서브에이전트는 독립적인 실행 컨텍스트를 가진 별도의 에이전트.
- 메인 에이전트가 서브에이전트를 호출하여 작업을 위임할 수 있음.
- 서브에이전트는 자체 CLAUDE.md, skills, hooks, subagents, MCP servers 를 가질 수 있음.
- 서브에이전트는 메인 에이전트에게 결과를 반환할 수 있음.
- 서브에이전트는 메인 에이전트에게 작업을 위임할 수 있음.
- 서브에이전트는 메인 에이전트에게 작업을 위임할 수 있음.

```
name (required) — 폴더명과 똑같이. 64자 제한. 소문자만 쓰셈.
description (required) — 클로드가 언제 이 스킬을 쓸지에 대한 설명. 1024자 제한.
allowed-tools (optional) — 이 스킬이 실행될 때 클로드가 사용할 수 있는 권한. 안적으면 제약없이 다씀.
model (optional) — 닭 잡는데 소 잡는 칼을 쓸 순 없으니, 모델 제한.
color (optional) — 서브에이전트의 색상. 
skills - 서브에이전트가 사용할 스킬 목록
```

