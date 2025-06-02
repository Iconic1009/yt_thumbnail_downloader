import requests
import re
import os

class YouTubeThumbnailDownloader:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def get_video_id(self, url):
        """Extract video ID from YouTube URL."""
        patterns = [
            r"(?:v=|youtu\.be/|embed/|shorts/)([a-zA-Z0-9_-]{11})",
            r"watch\?v=([a-zA-Z0-9_-]{11})"
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        raise ValueError("Invalid YouTube URL or video ID not found")

    def get_thumbnail_url(self, url):
        """Scrape the YouTube video page to extract the thumbnail URL."""
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                raise Exception(f"Failed to fetch video page. Status code: {response.status_code}")

            # Search for og:image meta tag
            match = re.search(r'<meta property="og:image" content="([^"]+)"', response.text)
            if match:
                thumbnail_url = match.group(1)
                # Ensure the URL is complete
                if not thumbnail_url.startswith("http"):
                    thumbnail_url = "https:" + thumbnail_url
                return thumbnail_url
            raise Exception("Thumbnail URL not found in page")
        except Exception as e:
            raise Exception(f"Error scraping thumbnail URL: {str(e)}")

    def download_thumbnail(self, url, save_path="thumbnail.jpg"):
        """Download the thumbnail from the YouTube URL to the specified path."""
        try:
            thumbnail_url = self.get_thumbnail_url(url)
            response = requests.get(thumbnail_url, headers=self.headers, stream=True)
            if response.status_code == 200:
                with open(save_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                return save_path
            else:
                raise Exception(f"Failed to download thumbnail. Status code: {response.status_code}")
        except Exception as e:
            raise Exception(f"Error downloading thumbnail: {str(e)}")
