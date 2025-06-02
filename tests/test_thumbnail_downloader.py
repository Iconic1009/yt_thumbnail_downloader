import unittest
import os
from yt_thumbnail_downloader import YouTubeThumbnailDownloader

class TestYouTubeThumbnailDownloader(unittest.TestCase):
    def setUp(self):
        self.downloader = YouTubeThumbnailDownloader()

    def test_get_video_id(self):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        video_id = self.downloader.get_video_id(url)
        self.assertEqual(video_id, "dQw4w9WgXcQ")

    def test_invalid_url(self):
        with self.assertRaises(ValueError):
            self.downloader.get_video_id("https://invalid.com")

    def test_get_thumbnail_url(self):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        thumbnail_url = self.downloader.get_thumbnail_url(url)
        self.assertTrue(thumbnail_url.startswith("https://"))
        self.assertIn("ytimg.com", thumbnail_url)

    def test_download_thumbnail(self):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        save_path = "test_thumbnail.jpg"
        result = self.downloader.download_thumbnail(url, save_path)
        self.assertTrue(os.path.exists(save_path))
        os.remove(save_path)  # Clean up

if __name__ == "__main__":
    unittest.main()
