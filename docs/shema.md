`docs/schema.md`:

```md
# DB 설계 초안

PostgreSQL을 사용한다. 게임 ID는 Steam 앱 ID를 그대로 사용한다.

| 테이블 | 주요 데이터 | 역할 |
| --- | --- | --- |
| games | app_id, name | 지원하는 게임 |
| source_reviews | recommendation_id, app_id, body, voted_up, created_at, playtime_at_review | Steam에서 수집한 리뷰 |
| feedback | id, app_id, body, status, created_at | 사용자가 입력한 새 피드백 |
| predictions | id, feedback_id, negative_probability, model_version | 모델의 예측 결과 |

## 관계

- 게임 하나에는 Steam 리뷰가 여러 개 있다.
- 게임 하나에는 사용자가 입력한 피드백이 여러 개 있다.
- 피드백 하나에는 예측 결과가 연결된다.

## 데이터 처리 규칙

- `recommendation_id`는 중복 저장되지 않도록 고유값으로 관리한다.
- `voted_up`은 학습할 때 정답값으로 사용한다. 모델 입력값에는 넣지 않는다.
- 유사 리뷰 검색용 벡터는 해당 기능을 개발할 때 추가한다.
- 실제 자료형과 필수 여부는 Steam API 응답을 확인한 뒤 확정한다.
