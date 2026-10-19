# TikTok clients for Crawlora

Official Crawlora client packages for the hosted TikTok API. Access 28 API endpoints covering video, user, and hashtag search; profiles and posts; comments; trends; Creative Center; and Top Ads data from JavaScript/TypeScript, Python, Go, Ruby, Java, and PHP. These clients call Crawlora's hosted API; they do not scrape TikTok locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by TikTok or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/tiktok`](javascript/README.md)
- Python: [`crawlora-tiktok`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-tiktok`](go.mod)
- Ruby: [`crawlora-tiktok`](ruby/README.md)
- Java: [`net.crawlora:crawlora-tiktok:0.3.0`](java/README.md)
- PHP: [`crawlora/tiktok`](php/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The six language clients provide access to all 28 selected public TikTok API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
