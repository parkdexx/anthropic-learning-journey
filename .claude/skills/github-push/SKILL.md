
---
name: github-push
description:
 - 사용자가 github 에 push 를 요청하면 사용.
 - 깃 푸시해줘, 깃허브 푸시해줘, git push 해줘 라고 줄여 말할 수 있음.
 - 연결된 레포지토리에 add → commit → push 를 한 번에 수행함.
 - 푸시 계정은 반드시 soohyeok.park@gmail.com 으로 진행.
 - git config 의 soohyeok.park@shinshinsa.com 으로 진행하지 말 것.
---

## 역할
연결된 GitHub 원격 저장소에 현재 브랜치를 push한다.
변경사항이 있으면 자동으로 `git add → commit → push` 를 순서대로 처리한다.
사용자 승인 없이 즉시 실행한다.

## 고정 설정
- **Push 계정 이메일**: `soohyeok.park@gmail.com`
- **커밋 메시지**: 자동 생성 (영어, 간결하고 직관적으로)

## 실행 절차

### 1단계 — 사전 확인
다음 항목을 순서대로 확인한다:
- 현재 브랜치 이름 (`git branch --show-current`)
- 변경사항 존재 여부 (`git status`)
- 원격 저장소 연결 여부 (`git remote -v`)
- 로컬이 원격보다 앞서 있는 커밋 수 (`git log origin/<branch>..HEAD --oneline`)

### 2단계 — 변경사항 스테이징
untracked 파일 또는 수정된 파일이 있을 경우 `git add -A` 로 전체 스테이징한다.

### 3단계 — 커밋 메시지 자동 생성
`git diff --cached --stat` 와 변경 파일 목록을 분석하여 커밋 메시지를 자동 생성한다.
- 형식: `<type>: <short description>` (영어, 50자 이내)
- type 예시: `feat`, `fix`, `docs`, `refactor`, `chore`
- 예시: `feat: add agent skills intro module and skill files`

### 4단계 — Add → Commit → Push 실행
사용자 승인 없이 즉시 순서대로 실행한다:
1. `git add -A`
2. `git -c user.email="soohyeok.park@gmail.com" commit -m "<자동생성 메시지>"`
3. `git push` (필요 시 `git push -u origin <브랜치명>`)

### 6단계 — 결과 보고
성공 시: 푸시 계정정보와, push된 브랜치와 커밋 메시지를 간단히 요약한다.
실패 시: 에러 메시지를 그대로 보여주고 원인을 설명한다.

## 에러 케이스
| 상황 | 대응 |
|------|------|
| 원격 저장소 미설정 | `git remote add origin <URL>` 명령을 안내 |
| 원격이 로컬보다 앞서 있음 (rejected) | `git pull` 후 재시도를 안내 |
| 인증 실패 | SSH 키 또는 토큰 설정을 확인하도록 안내 |
| force push 요청 | 위험성을 경고하고 사용자에게 재확인 |
