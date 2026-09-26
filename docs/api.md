# API 명세 초안

기본 경로: `/api/v1`

| 메서드 | 경로 | 기능 |
| --- | --- | --- |
| GET | `/games` | 지원하는 게임 목록 조회 |
| GET | `/games/{appId}/reviews` | 게임별 리뷰 목록 조회 |
| GET | `/games/{appId}/stats` | 게임별 날짜별 리뷰 수·추천율 조회 |
| POST | `/feedback` | 새 피드백 등록 및 분석 요청 |
| GET | `/feedback/{id}` | 예측 결과와 유사 리뷰 조회 |

## 입력 예시

`GET /games/2357570/reviews?page=0&size=20`

`POST /feedback`

```json
{
  "appId": 2357570,
  "text": "탱커 밸런스가 아쉬워요."
}

## 결과 예시
{
  "id": 1,
  "status": "DONE",
  "prediction": {
    "negativeProbability": 0.73,
    "modelVersion": "v1"
  },
  "similarReviews": []
}
