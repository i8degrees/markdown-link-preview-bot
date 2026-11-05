# util.py:jeff
#

import os
import re
import requests

DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1")
EXPERIMENTAL = os.getenv("EXPERIMENTAL", "False").lower() in ("true", "1")
#SUPPRESS_EMBED = os.getenv("SUPPRESS_EMBED", "False").lower() in ("true", "1")

# Regex pattern to detect standard, short, and shorts YouTube links
YOUTUBE_REGEX = r'(https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+|https?://youtu\.be/[\w-]+|https?://(?:www\.)?youtube\.com/shorts/[\w-]+)'

OEMBED_API_BASE_URL: str = "https://www.youtube.com/oembed"
OEMBED_API_FORMAT: str = "json"

def get_youtube_metadata(url) -> dict:
    """Fetches the video metadata using YouTube's oEmbed API with exception handling."""
    result: dict = {
        'title': 'Unknown title',
        'author_name': 'Unknown author',
        #'thumbnail_url': "",
    }
    final_api_url: str = f'{OEMBED_API_BASE_URL}?url={url}&format={OEMBED_API_FORMAT}'
    if DEBUG:
        print(f'final_api_url: {final_api_url}')

    try:
        response = requests.get(final_api_url, timeout=5)
        # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()
        res = response.json()

        result["title"] = res.get("title", "Unknown title")
        result["author_name"] = res.get("author_name", "Unknown author")
        #if bool(EXPERIMENTAL) == True:
            #result["thumbnail_url"] = res.get("thumbnail_url", "")
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error fetching YouTube title for {url}: {e}")
        return None
    except (ValueError, KeyError) as e:
        print(f"Error parsing API response for {url}: {e}")
        return None
    pass

def split_response_lines(lines, limit=1900) -> list:
    """Chunks a list of lines into chunks that stay safely under the character limit."""
    chunks = []
    current_chunk = []
    current_length = 0

    for line in lines:
        # +1 accounts for the newline character added during joining
        if current_length + len(line) + 1 > limit:
            chunks.append("\n".join(current_chunk))
            current_chunk = [line]
            current_length = len(line)
        else:
            current_chunk.append(line)
            current_length += len(line) + 1

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks
