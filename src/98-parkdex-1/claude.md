# CLAUDE.md — 바이브코딩 효율 극대화 템플릿
> 이 파일은 Claude Code가 프로젝트를 이해하고 올바르게 동작하기 위한 핵심 지침서입니다.
> 새 프로젝트를 시작할 때 이 템플릿을 복사한 후 `[ ]` 안의 내용을 실제 프로젝트 정보로 교체하세요.

---

## 절대 규칙 — 위반하면 안 되는 금지 사항 (맨 위에 배치)

> **왜 필요한가:** Claude가 빠른 바이브코딩 중 파괴적 명령을 실수로 실행하면 복구 비용이 크다.
> 가장 먼저 읽히는 위치에 금지 사항을 명시해 오작동을 사전 차단한다.

### 🚫 파일 시스템
- 파일 삭제 또는 덮어쓰기 전에 **반드시 사용자에게 확인**을 받는다.
- `rm -rf`, `del /f /s` 등 재귀 삭제 명령은 명시적 승인 없이 실행하지 않는다.
- `[ 직접 수정 금지 폴더 경로, 예: dist/, build/, generated/ ]` 폴더는 수동 편집 금지 — 빌드 산출물임.

### 🚫 Git 명령
- `git push --force` (또는 `--force-with-lease`) 는 사용자가 명시적으로 요청한 경우에만 실행한다.
- `git reset --hard`, `git checkout -- .` 등 로컬 변경사항을 폐기하는 명령은 실행 전 확인한다.
- `git rebase -i` 등 게시된 커밋을 수정하는 작업은 항상 경고 후 진행한다.

### 🚫 보안 / 시크릿
- `.env`, `.env.local`, `*.pem`, `*.key`, `secrets.*` 파일은 절대 커밋하지 않는다.
- API 키, 비밀번호, 토큰을 소스 코드에 하드코딩하지 않는다. 환경변수로 처리한다.
- `console.log`로 민감 정보(토큰, 사용자 PII)를 출력하지 않는다.

### 🚫 프로젝트 고유 금지 사항
```
# 예시 — 실제 프로젝트에 맞게 교체
- src/legacy/ 폴더는 리팩터링 대상이므로 새 코드에서 import하지 않는다.
- DB 스키마 마이그레이션 파일(db/migrations/)은 직접 수정하지 않는다. 새 파일을 생성한다.
- [ 프로젝트 고유 금지 패턴 추가 ]
```

---

## 아키텍처 — 폴더 구조, 기술 스택

> **왜 필요한가:** Claude가 파일 탐색에 시간을 낭비하지 않고 올바른 위치에 바로 코드를 작성할 수 있게 한다.

### 핵심 폴더 구조
```
[ 프로젝트명 ]/
├── src/
│   ├── app/           # [ 역할 설명, 예: Next.js App Router 페이지 ]
│   ├── components/    # [ 역할 설명, 예: 재사용 가능한 UI 컴포넌트 ]
│   ├── features/      # [ 역할 설명, 예: 도메인별 기능 묶음 (feature-sliced) ]
│   ├── lib/           # [ 역할 설명, 예: 서드파티 라이브러리 래퍼, 유틸리티 ]
│   ├── hooks/         # [ 역할 설명, 예: 커스텀 React 훅 ]
│   └── types/         # [ 역할 설명, 예: 전역 TypeScript 타입 정의 ]
├── public/            # 정적 에셋 (이미지, 폰트)
├── tests/             # 테스트 파일 (유닛 / E2E)
├── .env.example       # 환경변수 템플릿 (실제 값 없음)
└── [ 기타 디렉토리 ]
```

### 진입점(Entry Point)
- **앱 시작점**: `[ 예: src/app/layout.tsx 또는 src/index.ts ]`
- **API 라우트**: `[ 예: src/app/api/ ]`
- **환경변수 로딩**: `[ 예: src/lib/env.ts — zod로 검증 ]`

### 기술 스택
| 레이어 | 기술 | 버전 |
|--------|------|------|
| 런타임 | [ 예: Node.js ] | [ 예: 20.x ] |
| 프레임워크 | [ 예: Next.js ] | [ 예: 14.x ] |
| 언어 | [ 예: TypeScript ] | [ 예: 5.x ] |
| 데이터베이스 | [ 예: PostgreSQL + Prisma ] | [ 예: 5.x ] |
| 상태관리 | [ 예: Zustand ] | [ 예: 4.x ] |
| 스타일링 | [ 예: Tailwind CSS ] | [ 예: 3.x ] |
| 테스트 | [ 예: Vitest + Playwright ] | [ 예: 1.x ] |

### 외부 서비스 / API 의존성
```
# 예시 — 실제 프로젝트에 맞게 교체
- Supabase: 인증(Auth) + 데이터베이스
- Stripe: 결제 처리 (webhook: /api/webhooks/stripe)
- Resend: 트랜잭션 이메일 발송
- Cloudinary: 이미지 업로드 및 최적화
- [ 서비스명: 역할 ]
```

---

## 빌드/테스트 — 개발 서버, 테스트, 배포 명령어

> **왜 필요한가:** Claude가 코드 작성 후 스스로 검증할 수 있어야 반복 질문 없이 세션이 진행된다.

### 개발 환경 실행
```bash
# 의존성 설치
[ 예: npm install ]

# 개발 서버 시작 (기본 포트: [ 예: 3000 ])
[ 예: npm run dev ]

# 환경변수 설정 (최초 1회)
cp .env.example .env.local
# .env.local 파일에 실제 값 입력
```

### 테스트
```bash
# 전체 테스트 실행
[ 예: npm test ]

# 단일 파일 테스트
[ 예: npm test -- src/features/auth/auth.test.ts ]

# Watch 모드 (개발 중 자동 재실행)
[ 예: npm run test:watch ]

# E2E 테스트
[ 예: npm run test:e2e ]

# 커버리지 리포트 생성
[ 예: npm run test:coverage ]
```

### 빌드 & 배포
```bash
# 프로덕션 빌드
[ 예: npm run build ]

# 빌드 결과물 로컬 실행 (배포 전 검증)
[ 예: npm run start ]

# 배포 (예: Vercel)
[ 예: vercel --prod ]

# DB 마이그레이션 실행
[ 예: npm run db:migrate ]
```

### 자주 쓰는 스크립트
```bash
# 코드 포맷팅
[ 예: npm run format ]        # Prettier 적용

# 린트 검사
[ 예: npm run lint ]          # ESLint 실행
[ 예: npm run lint:fix ]      # 자동 수정 가능한 오류 수정

# 타입 체크 (빌드 없이)
[ 예: npm run typecheck ]

# DB 스키마 시각화
[ 예: npm run db:studio ]     # Prisma Studio 실행
```

---

## 도메인 컨텍스트 — 비즈니스 용어, 데이터 흐름

> **왜 필요한가:** 비즈니스 용어를 모르면 Claude가 잘못된 가정으로 로직을 짠다.
> 짧은 용어집 하나가 큰 구조적 오류를 막는다.

### 핵심 비즈니스 용어 (Glossary)
```
# 예시 — 실제 도메인 용어로 교체 (3~10개 권장)
- Order(주문): 사용자가 상품을 구매하기 위해 생성한 거래 단위. 상태: PENDING → PAID → SHIPPED → DELIVERED
- Product(상품): 판매 가능한 아이템. 재고(Stock)와 분리된 개념.
- Inventory(재고): 특정 창고(Warehouse)에 보관된 Product의 수량.
- Merchant(판매자): 상품을 등록하고 판매하는 사업자. User와 별도 엔티티.
- [ 용어: 정의 ]
```

### 주요 데이터 모델 및 관계
```
# 예시 — 실제 모델로 교체 (텍스트 다이어그램 또는 간단한 목록)
User (1) ──< Order (N)       # 한 사용자는 여러 주문을 가질 수 있음
Order (1) ──< OrderItem (N)  # 한 주문에 여러 상품 포함 가능
OrderItem >── Product (1)    # 각 주문 항목은 하나의 상품을 참조

핵심 필드:
- User: id, email, role(CUSTOMER|ADMIN), createdAt
- Order: id, userId, status, totalAmount, paidAt
- Product: id, merchantId, name, price, isActive
```

### 중요한 비즈니스 규칙
```
# 예시 — 실제 규칙으로 교체
1. 주문은 PAID 상태가 되기 전까지 취소(CANCELLED) 가능.
2. 재고가 0인 상품은 주문 불가 — 주문 생성 시 재고 차감은 트랜잭션으로 처리.
3. 판매자(Merchant)는 자신의 상품만 수정 가능. ADMIN은 모든 상품 수정 가능.
4. 이메일 인증이 완료되지 않은 User는 주문 생성 불가.
5. [ 비즈니스 규칙 추가 ]
```

---

## 코딩 컨벤션 — 네이밍, 커밋, 패턴 규칙

> **왜 필요한가:** 반복 지시 없이 일관된 코드 스타일을 유지하게 한다.
> Claude가 기존 코드와 동일한 패턴으로 새 코드를 작성할 수 있다.

### 네이밍 규칙
```
# 변수 / 함수: camelCase
const userId = '...'
async function fetchOrderById(orderId) { ... }

# 클래스 / 컴포넌트 / 타입 / 인터페이스: PascalCase
class OrderService { ... }
function OrderCard({ order }: OrderCardProps) { ... }
type UserRole = 'ADMIN' | 'CUSTOMER'
interface CreateOrderInput { ... }

# 상수 (불변 값): UPPER_SNAKE_CASE
const MAX_RETRY_COUNT = 3
const DEFAULT_PAGE_SIZE = 20

# 파일명: kebab-case (컴포넌트 제외)
order-service.ts
use-order.ts
# React 컴포넌트 파일: PascalCase
OrderCard.tsx

# 불리언 변수: is/has/can 접두사
const isLoading = false
const hasPermission = true
```

### 커밋 메시지 형식 (Conventional Commits)
```
<type>(<scope>): <subject>

type 목록:
- feat: 새로운 기능 추가
- fix: 버그 수정
- refactor: 기능 변경 없는 코드 개선
- docs: 문서 수정
- test: 테스트 추가/수정
- chore: 빌드, 설정 파일 변경

예시:
feat(order): 주문 취소 API 엔드포인트 추가
fix(auth): 토큰 만료 시 자동 로그아웃 오류 수정
refactor(product): ProductService 클래스로 로직 분리
```

### 선호 패턴
```typescript
// ✅ async/await 사용 (Promise chain 지양)
const order = await orderService.findById(orderId)

// ✅ 에러 핸들링: try-catch + 커스텀 에러 클래스
try {
  const result = await createOrder(input)
  return result
} catch (error) {
  if (error instanceof OutOfStockError) {
    throw new BadRequestError('재고 부족')
  }
  throw error
}

// ✅ 조기 반환(early return)으로 중첩 줄이기
if (!user) return null
if (!user.isVerified) throw new ForbiddenError()
// 이후 핵심 로직

// ✅ 함수 인자가 3개 이상이면 객체로 묶기
// 🚫 createOrder(userId, productId, quantity, couponCode)
// ✅
createOrder({ userId, productId, quantity, couponCode })
```

### 피해야 할 안티패턴
```
# 🚫 any 타입 남용 (TypeScript 사용 시)
const data: any = await fetch(...)   // 금지
const data: OrderResponse = await fetch(...)  // 권장

# 🚫 마법 숫자(Magic Number) 직접 사용
if (retryCount > 3) { ... }          // 금지
if (retryCount > MAX_RETRY_COUNT) { ... }  // 권장

# 🚫 callback hell — async/await 또는 Promise.all 사용
# 🚫 컴포넌트 내 비즈니스 로직 작성 — custom hook 또는 service로 분리
# 🚫 전역 변수 사용 — 모듈 스코프 또는 context/store로 관리
# 🚫 [ 프로젝트 고유 안티패턴 추가 ]
```

---

> **사용 팁:** 이 파일은 Claude Code가 세션 시작 시 자동으로 읽습니다.
> 프로젝트가 성장하면서 규칙이 바뀌면 이 파일도 함께 업데이트하세요.
> 분량이 너무 길어지면 섹션별로 별도 파일(`ARCHITECTURE.md`, `CONVENTIONS.md`)로 분리하고
> 이 파일에서 링크로 참조하는 방식을 권장합니다.
