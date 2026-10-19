# crawlora-tiktok — TikTok API client for Python

Python client for Crawlora's hosted TikTok API. It exposes 28 API endpoints covering video, user, and hashtag search; profiles and posts; comments; trends; Creative Center; and Top Ads data. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-python-homepage); the package does not run a browser or scrape
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
| `GET` | `/tiktok/mobile/feed` | `tiktok-mobile-feed` | Retrieve the TikTok mobile For You feed |
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
