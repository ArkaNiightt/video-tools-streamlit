from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)
from urllib.parse import urlparse, parse_qs


def extract_video_id(video_url):
    """Extracts the video ID from a YouTube URL."""
    parsed_url = urlparse(video_url)
    if "youtu.be" in parsed_url.netloc:
        return parsed_url.path.lstrip("/")
    elif "youtube.com" in parsed_url.netloc:
        query_params = parse_qs(parsed_url.query)
        return query_params.get("v", [None])[0]
    return None


def fetch_transcript(video_id, language="pt"):
    """Fetches the transcript of a YouTube video by video ID."""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(
            video_id, languages=[language]
        )
        return "\n".join([item["text"] for item in transcript_list])
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except NoTranscriptFound:
        return "No transcript found for the specified language."
    except VideoUnavailable:
        return "The video is unavailable."
    except Exception as e:
        return f"Failed to fetch transcript: {str(e)}"


def fetch_video_transcript(video_url):
    """Fetches the video transcript given a YouTube URL."""
    video_id = extract_video_id(video_url)
    if not video_id:
        return "Invalid YouTube URL."
    return fetch_transcript(video_id)
