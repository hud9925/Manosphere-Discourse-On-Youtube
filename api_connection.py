import sqlite3
import sys
sys.stdout.reconfigure(encoding='utf-8')
from googleapiclient.discovery import build
import re
# import environment variables; google api key
from dotenv import load_dotenv
import os




#connect to SQLite database
conn = sqlite3.connect("youtube_data.db")
cursor = conn.cursor()


cursor.execute("PRAGMA table_info(Videos)")
for row in cursor.fetchall():
    print(row)

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Videos (
    video_id TEXT PRIMARY KEY,
    title TEXT,
    description TEXT,
    hashtags TEXT,
    publish_date DATE,
    view_count INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Comments (
    comment_id TEXT PRIMARY KEY,
    video_id TEXT,
    text TEXT,
    like_count INTEGER,
    publish_date DATE,
    FOREIGN KEY (video_id) REFERENCES Videos (video_id)
)
''')



api_key = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=api_key)

# setting up youtube api


def fetch_video_data(video_id):
    try:
        # Get video details
        video_request = youtube.videos().list(part="snippet,statistics", id=video_id)
        video_response = video_request.execute()
        
        video_info = video_response["items"][0]
        snippet = video_info["snippet"]
        statistics = video_info.get("statistics", {})
        
        title = snippet["title"]
        description = snippet["description"]
        hashtags = re.findall(r"#\w+", description)  # Extract hashtags
        publish_date = snippet.get("publishedAt", "").split("T")[0]  # ISO format to YYYY-MM-DD
        view_count = statistics.get("viewCount", 0)
        
        return {
            "video_id": video_id,
            "title": title,
            "description": description,
            "hashtags": ", ".join(hashtags),
            "publish_date": publish_date,
            "view_count": int(view_count)
        }
    except Exception as e:
        print(f"Error fetching video data for {video_id}: {e}")
        return None


def fetch_comments(video_id):
    try:
        comments = []
        comments_request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            order="relevance"
        )
        comments_response = comments_request.execute()
        
        for item in comments_response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]
            comment_id = item["id"]
            text = comment["textDisplay"]
            like_count = comment.get("likeCount", 0)
            publish_date = comment.get("publishedAt", "").split("T")[0]
            
            comments.append({
                "comment_id": comment_id,
                "video_id": video_id,
                "text": text,
                "like_count": int(like_count),
                "publish_date": publish_date
            })
        
        return comments
    except Exception as e:
        print(f"Error fetching comments for {video_id}: {e}")
        return []

# Save data to SQLite
def save_video_data(video_data):
    cursor.execute('''
    INSERT OR REPLACE INTO Videos (video_id, title, description, hashtags, publish_date, view_count)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        video_data["video_id"],
        video_data["title"],
        video_data["description"],
        video_data["hashtags"],
        video_data["publish_date"],
        video_data["view_count"]
    ))
    conn.commit()

def save_comments_data(comments):
    for comment in comments:
        cursor.execute('''
        INSERT OR REPLACE INTO Comments (comment_id, video_id, text, like_count, publish_date)
        VALUES (?, ?, ?, ?, ?)
        ''', (
            comment["comment_id"],
            comment["video_id"],
            comment["text"],
            comment["like_count"],
            comment["publish_date"]
        ))
    conn.commit()
# Example video IDs
video_ids = [
    "wxnZp3OiN8U",
    "lZ3dzn_Gas0"
]


# Process each video
for video_id in video_ids:
    print(f"Processing video: {video_id}")
    video_data = fetch_video_data(video_id)
    if video_data:
        save_video_data(video_data)
        comments = fetch_comments(video_id)
        save_comments_data(comments)

# Close database connection
conn.close()

