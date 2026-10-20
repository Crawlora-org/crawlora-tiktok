# crawlora-tiktok — TikTok API client for Python

Python client for Crawlora's hosted TikTok API. It exposes 53 API endpoints covering video, user, and hashtag search; profiles and posts; comments; trends; Creative Center; and Top Ads data. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-python-homepage); the package does not run a browser or scrape
TikTok locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
TikTok or its owners.

## Install

```sh
python -m pip install crawlora-tiktok
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_tiktok import TikTokClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with TikTokClient(api_key=api_key) as client:
    result_1 = client.search(keyword='science')
    print(result_1)
    result_2 = client.trending()
    print(result_2)
```

The package also exports `Client` as an alias for `TikTokClient`. Operation
methods are available directly in snake_case and through the `tiktok`
group. The async package client is `AsyncTikTokClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-tiktok/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-tiktok/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_tiktok import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.search(keyword='science')
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-tiktok/blob/main/examples/python.py) for a complete usage example.

## Supported TikTok API endpoints

This package exposes every route below through direct snake_case methods and the `tiktok` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-tiktok/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/tiktok/category` | `tiktok-category` | List TikTok explore categories |
| `GET` | `/tiktok/comments` | `tiktok-video-comments` | Retrieve TikTok video comments |
| `GET` | `/tiktok/creative-center/filters` | `tiktok-creative-center-filters` | Retrieve TikTok Creative Center filter taxonomy |
| `GET` | `/tiktok/creative-center/hashtags` | `tiktok-creative-center-hashtags` | Retrieve TikTok Creative Center trending hashtags |
| `GET` | `/tiktok/creative-center/top-content` | `tiktok-creative-center-top-content` | Retrieve TikTok Creative Center top content |
| `GET` | `/tiktok/creative-center/videos` | `tiktok-creative-center-videos` | Retrieve TikTok Creative Center trending videos |
| `GET` | `/tiktok/explore/{id}` | `tiktok-explore` | Retrieve the TikTok explore feed for a category |
| `GET` | `/tiktok/hashtag/{name}` | `tiktok-challenge` | Retrieve TikTok hashtag details |
| `GET` | `/tiktok/hashtags` | `tiktok-challenge-list` | Retrieve TikTok hashtag posts |
| `GET` | `/tiktok/mobile/anchor/list` | `tiktok-mobile-anchor-list` | Anchor catalogue used by the video composer |
| `GET` | `/tiktok/mobile/comment/replies` | `tiktok-mobile-comment-replies` | Retrieve replies to a TikTok comment |
| `GET` | `/tiktok/mobile/comments` | `tiktok-mobile-comments` | Retrieve comments for a TikTok video |
| `GET` | `/tiktok/mobile/feed` | `tiktok-mobile-feed` | Retrieve the TikTok mobile For You feed |
| `GET` | `/tiktok/mobile/feed/post` | `tiktok-mobile-feed-post` | Fetch the app's primary feed call (POST, protobuf) decoded without a schema |
| `GET` | `/tiktok/mobile/hashtag` | `tiktok-mobile-hashtag` | Retrieve a TikTok hashtag |
| `GET` | `/tiktok/mobile/hashtag/posts` | `tiktok-mobile-hashtag-posts` | Retrieve videos for a TikTok hashtag |
| `GET` | `/tiktok/mobile/hashtags` | `tiktok-mobile-hashtags` | Search TikTok hashtags |
| `GET` | `/tiktok/mobile/live/effects` | `tiktok-mobile-live-effects` | Retrieve TikTok LIVE effects |
| `GET` | `/tiktok/mobile/live/gifts` | `tiktok-mobile-live-gifts` | Retrieve TikTok LIVE gifts |
| `GET` | `/tiktok/mobile/live/search` | `tiktok-mobile-live-search` | Search TikTok LIVE streams |
| `GET` | `/tiktok/mobile/music/beats` | `tiktok-mobile-music-beats` | Retrieve TikTok music beats |
| `GET` | `/tiktok/mobile/music/collections` | `tiktok-mobile-music-collections` | Retrieve TikTok music collections |
| `GET` | `/tiktok/mobile/music/pick` | `tiktok-mobile-music-pick` | Retrieve TikTok sound chart picks |
| `GET` | `/tiktok/mobile/music/posts` | `tiktok-mobile-music-posts` | Retrieve videos for a TikTok sound |
| `GET` | `/tiktok/mobile/music/related` | `tiktok-mobile-music-related` | Retrieve sounds related to a TikTok video |
| `GET` | `/tiktok/mobile/music/trending` | `tiktok-mobile-music-trending` | Retrieve TikTok trending sounds |
| `GET` | `/tiktok/mobile/search` | `tiktok-mobile-search` | Search TikTok videos on the mobile API |
| `GET` | `/tiktok/mobile/search/music` | `tiktok-mobile-search-music` | Search TikTok sounds on the mobile API |
| `GET` | `/tiktok/mobile/search/place` | `tiktok-mobile-search-place` | Search TikTok places |
| `GET` | `/tiktok/mobile/search/pre-info` | `tiktok-mobile-search-pre-info` | Pre-search info token for a search session |
| `GET` | `/tiktok/mobile/search/sug` | `tiktok-mobile-search-sug` | Retrieve TikTok search suggestions |
| `GET` | `/tiktok/mobile/search/tabs` | `tiktok-mobile-search-tabs` | Search tabs available for a keyword |
| `GET` | `/tiktok/mobile/search/user` | `tiktok-mobile-search-user` | Search TikTok users on the mobile API |
| `GET` | `/tiktok/mobile/trending/categories` | `tiktok-mobile-trending-categories` | Retrieve TikTok trending categories |
| `GET` | `/tiktok/mobile/trending/effects` | `tiktok-mobile-trending-effects` | Retrieve TikTok trending effects |
| `GET` | `/tiktok/popular-trend/country-industry-meta` | `tiktok-popular-trend-country-industry-meta` | Retrieve TikTok popular-trend country and industry metadata |
| `GET` | `/tiktok/post/{id}` | `tiktok-post` | Retrieve TikTok video details |
| `GET` | `/tiktok/posts` | `tiktok-profile-post` | Retrieve posts from a TikTok profile |
| `GET` | `/tiktok/profile/{handler}` | `tiktok-profile` | Retrieve a TikTok profile |
| `GET` | `/tiktok/search` | `tiktok-search` | Search TikTok videos |
| `GET` | `/tiktok/search/hashtag` | `tiktok-search-hashtag` | Search TikTok hashtags |
| `GET` | `/tiktok/search/user` | `tiktok-search-user` | Search TikTok users |
| `GET` | `/tiktok/top-ads/analysis` | `tiktok-top-ads-analysis` | Retrieve TikTok Top Ads interactive time analysis |
| `GET` | `/tiktok/top-ads/detail` | `tiktok-top-ads-detail` | Retrieve TikTok Top Ads detail |
| `GET` | `/tiktok/top-ads/filters` | `tiktok-top-ads-filters` | Retrieve TikTok Top Ads filters |
| `GET` | `/tiktok/top-ads/list` | `tiktok-top-ads-list` | Retrieve TikTok Top Ads |
| `GET` | `/tiktok/top-ads/location-info` | `tiktok-top-ads-location-info` | Retrieve TikTok Top Ads location info |
| `GET` | `/tiktok/top-ads/locations` | `tiktok-top-ads-locations` | Retrieve TikTok Top Ads locations |
| `GET` | `/tiktok/top-ads/recommend` | `tiktok-top-ads-recommend` | Retrieve TikTok Top Ads recommendations |
| `GET` | `/tiktok/top-ads/safety` | `tiktok-top-ads-safety` | Retrieve TikTok Top Ads safety configuration |
| `GET` | `/tiktok/top-ads/spotlight` | `tiktok-top-ads-spotlight` | Retrieve TikTok Top Ads Spotlight |
| `GET` | `/tiktok/top-ads/suggestions` | `tiktok-top-ads-suggestions` | Retrieve TikTok Top Ads suggestions |
| `GET` | `/tiktok/trending` | `tiktok-trending` | Retrieve TikTok trending posts |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
