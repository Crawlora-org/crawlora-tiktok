# TikTok clients for Crawlora

Official Crawlora client packages for the hosted TikTok API. Access 53 API endpoints covering video, user, and hashtag search; profiles and posts; comments; trends; Creative Center; and Top Ads data from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape TikTok locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by TikTok or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/tiktok`](javascript/README.md)
- Python: [`crawlora-tiktok`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-tiktok`](go.mod)
- Ruby: [`crawlora-tiktok`](ruby/README.md)
- Java: [`net.crawlora:crawlora-tiktok:0.4.0`](java/README.md)
- PHP: [`crawlora/tiktok`](php/README.md)
- Rust: [`crawlora-tiktok`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 53 selected public TikTok API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
