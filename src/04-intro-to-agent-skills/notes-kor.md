
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

