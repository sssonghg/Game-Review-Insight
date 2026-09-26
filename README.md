# Game Review Insight

오버워치 2와 이터널 리턴의 한국어 Steam 리뷰를 분석하는 서비스입니다.

## 핵심 기능

1. 게임별 리뷰 수와 추천·비추천 흐름을 보여줍니다.
2. 새 피드백을 입력하면 직접 학습한 모델로 추천·비추천 가능성을 예측합니다.
3. 입력한 피드백과 의미가 비슷한 기존 리뷰를 찾아줍니다.

## 대상 게임

| 게임 | Steam 앱 ID |
| --- | --- |
| 오버워치 2 | 2357570 |
| 이터널 리턴 | 1049590 |

## 기술 구성

- Frontend: React, Vite
- Backend: Spring Boot, JPA
- 데이터 수집·모델 학습: Python
- 모델 예측 API: FastAPI
- Database: PostgreSQL, pgvector
- 이후 확장: Airflow, Kafka, Redis, MLflow, Docker, 로컬 Kubernetes

## 진행 상태

- [x] GitHub 저장소 및 `dev` 브랜치 생성
- [x] 프로젝트 폴더 구조 생성
- [ ] Steam 리뷰 응답 확인
- [ ] 리뷰 수집기 구현
- [ ] DB·API·화면 구현
- [ ] 모델 학습·평가 및 예측 기능 구현