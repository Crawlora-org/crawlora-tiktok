import os

from crawlora_tiktok import TikTokClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with TikTokClient(api_key=api_key) as client:
    search = client.search(keyword='science')
    print('search', search)
    trending = client.trending()
    print('trending', trending)
