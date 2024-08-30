from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Debug: Print all environment variables to check if they are loaded
print(f"Environment Variables: {os.environ}")

api_key = os.getenv('AIzaSyC1GPad5ekwSP0VWDfN3O3sGBmzp_1HgTs')
if not api_key:
    raise ValueError("API key not found in environment variables")

print(f"Loaded API key: {api_key}")  # Debug statement

youtube = build('youtube', 'v3', developerKey=api_key)

def fetch_comments(video_id):
    comments = []
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText'
    ).execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments
