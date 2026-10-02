import requests
import json 
from pathlib import Path

def fetch_review_page(app_id, cursor="*"):
    url = f"https://store.steampowered.com/appreviews/{app_id}"

    params = {
        "json": 1,
        "filter": "recent",
        "language": "koreana",
        "purchase_type": "all",
        "num_per_page": 10,
        "cursor": cursor,
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if data.get("success") != 1:
        raise RuntimeError("Steam 리뷰 요청에 실패했습니다.")

    return data

def collect_reviews(app_id, max_pages=3):
    cursor = "*"
    all_reviews = []
    seen_ids = set()

    for page in range(1, max_pages + 1):
        try:
            data = fetch_review_page(app_id, cursor)
        except (requests.RequestException, ValueError, RuntimeError) as error:
            print(f"{page}페이지 요청 실패: {error}")
            raise

        reviews = data.get("reviews")

        if not isinstance(reviews, list):
            raise RuntimeError("응답의 reviews가 목록 형식이 아닙니다.")

        if not reviews:
            print("더 가져올 리뷰가 없습니다.")
            break

        added_count = 0

        for review in reviews:
            review_id = review.get("recommendationid")

            if not review_id:
                print("리뷰 ID가 없는 항목을 건너뜁니다.")
                continue

            if review_id in seen_ids:
                continue

            seen_ids.add(review_id)
            all_reviews.append(review)
            added_count += 1

        print(
            f"{page}페이지: 받은 리뷰 {len(reviews)}개, "
            f"새로 추가 {added_count}개"
        )

        next_cursor = data.get("cursor")

        if not next_cursor or next_cursor == cursor:
            print("다음 페이지로 이동할 수 없어 종료합니다.")
            break

        cursor = next_cursor

    return all_reviews

def save_reviews(app_id, reviews):
    # 실행 위치와 관계없이 프로젝트의 data/raw에 저장
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / f"{app_id}.json"

    existing_reviews = []

    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as file:
            existing_reviews = json.load(file)

        if not isinstance(existing_reviews, list):
            raise ValueError("기존 파일이 리뷰 목록 형식이 아닙니다.")

    # 같은 ID는 한 번만 저장하고, 새로 받은 내용으로 갱신
    merged = {}

    for review in existing_reviews + reviews:
        merged[review["recommendationid"]] = review

    saved_reviews = list(merged.values())

    # 임시 파일에 쓴 뒤 교체
    temp_path = file_path.with_suffix(".json.tmp")

    with temp_path.open("w", encoding="utf-8") as file:
        json.dump(saved_reviews, file, ensure_ascii=False, indent=2)

    temp_path.replace(file_path)

    print(f"기존 {len(existing_reviews)}개 → 저장 {len(saved_reviews)}개")
    print(f"저장 위치: {file_path}")

if __name__ == "__main__":
    games = {
        2357570: "오버워치 2",
        1049590: "이터널 리턴",
    }

    for app_id, name in games.items():
        print(f"\n[{name}]")
        reviews = collect_reviews(app_id)
        print(f"이번에 수집한 리뷰: {len(reviews)}개")
        save_reviews(app_id, reviews)