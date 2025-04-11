import os
import csv
import argparse
from datetime import datetime
from googleapiclient.discovery import build


def get_trending_videos(api_key, region_code='VN', max_results=50):#mặc định là VN và 50 video
    """Lấy danh sách video trending từ YouTube API."""
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        chart="mostPopular",
        regionCode=region_code,
        maxResults=min(max_results, 50)
    )
    response = request.execute()
    # Lấy thông tin video từ phản hồi
    videos = []
    for video in response.get("items", []):
        snippet = video.get("snippet", {})
        stats = video.get("statistics", {})
        details = video.get("contentDetails", {})
        videos.append({
            "videoId": video.get("id", ""),
            "title": snippet.get("title", ""),
            "channel": snippet.get("channelTitle", ""),
            "publishedAt": snippet.get("publishedAt", ""),
            "views": stats.get("viewCount", "0"),
            "likes": stats.get("likeCount", "0"),
            "comments": stats.get("commentCount", "0"),
            "duration": details.get("duration", "")
        })
    return videos

# Lưu danh sách video vào file CSV
def save_to_csv(videos, region_code):
    if not videos:
        print("Không có video nào để lưu.")
        return
    
    os.makedirs("output", exist_ok=True)
    filename = f"output/youtube_trending_{region_code}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=videos[0].keys())
        writer.writeheader()
        writer.writerows(videos)
    
    print(f"Dữ liệu đã được lưu vào: {filename}")


def main():
    parser = argparse.ArgumentParser(description="Lấy video trending từ YouTube API")
    parser.add_argument("--api_key", required=True, help="YouTube API Key")
    parser.add_argument("--region", default="US", help="Mã quốc gia (ISO 3166-1 alpha-2)")
    parser.add_argument("--max_results", type=int, default=50, help="Số video tối đa")
    args = parser.parse_args()
    
    videos = get_trending_videos(args.api_key, args.region, args.max_results)
    save_to_csv(videos, args.region)

if __name__ == "__main__":
    main()
