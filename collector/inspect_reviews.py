import pandas as pd
import requests

url = "https://store.steampowered.com/appreviews/2357570"

# 해당 파라미터는 Steam API 참고
params = {
    "json": 1,
    "filter": "recent",
    "language": "koreana",
    "purchase_type": "all",
    "num_per_page": 10,
}

data = requests.get(url, params=params, timeout=10).json()
df = pd.json_normalize(data["reviews"])

print("받은 리뷰:", len(df))
print("추천/비추천:", df["voted_up"].value_counts().to_dict())
print("빈 본문:", df["review"].fillna("").str.strip().eq("").sum())
print("cursor 있음:", bool(data.get("cursor")))
print(df[[
    "recommendationid",
    "review",
    "voted_up",
    "timestamp_created",
    "author.playtime_at_review"
]])