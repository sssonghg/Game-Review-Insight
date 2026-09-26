# Steam 리뷰 응답 확인

## 확인 대상

| 게임 | Steam 앱 ID | 한국어 리뷰 확인 |
| --- | ---: | --- |
| 오버워치 2 | 2357570 | 리뷰 응답 확인 |
| 이터널 리턴 | 1049590 | 리뷰 응답 확인 |

## 리뷰 필드 확인 결과

두 게임의 리뷰 응답에서 아래 5개 필드를 모두 확인했다.

| 필드 | 의미 | 오버워치 2 | 이터널 리턴 |
| --- | --- | --- | --- |
| `recommendationid` | 리뷰 고유 ID | 있음 | 있음 |
| `review` | 리뷰 본문 | 있음 | 있음 |
| `voted_up` | 추천 여부 | 있음 | 있음 |
| `timestamp_created` | 리뷰 작성 시각 | 있음 | 있음 |
| `author.playtime_at_review` | 리뷰 작성 당시 플레이 시간 | 있음 | 있음 |

## 수집에 사용할 데이터

- `recommendationid`: 같은 리뷰가 중복 저장되지 않도록 식별하는 데 사용한다.
- `review`: 화면에 표시하고, 분류 모델의 입력 데이터로 사용한다.
- `voted_up`: 모델 학습·평가에 사용할 정답값이다. 모델 입력에는 넣지 않는다.
- `timestamp_created`: 날짜별 리뷰 흐름을 계산하고, 과거 학습·최근 평가 데이터를 나누는 데 사용한다.
- `author.playtime_at_review`: 플레이 시간과 평가의 관계를 살펴보는 추가 분석에 사용한다.

## 다음 작업

Python으로 두 게임의 리뷰를 요청해 `recommendationid`, `review`,
`voted_up`, `timestamp_created`, `author.playtime_at_review`를 출력한다.
이후 여러 페이지를 수집할 때 중복 리뷰와 누락된 값의 처리 방법을 정한다.