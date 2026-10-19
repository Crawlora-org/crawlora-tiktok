# TikTok API endpoint reference and client usage

This reference lists all 28 public TikTok API endpoints exposed by the `@crawlora-org/tiktok` and `crawlora-tiktok` packages, covering video, user, and hashtag search; profiles and posts; comments; trends; Creative Center; and Top Ads data. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape TikTok locally; Crawlora is independent from and not endorsed by TikTok or its owners.

The package tracks the public API contract revision `sha256:2150afc166e71c20642dfa0a7cb0e5b654c55e529f65420d6a4a502aeba8604b` bundled with release `0.3.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 28 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `tiktok` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `category` / `category` | `GET /tiktok/category` | — | List TikTok explore categories |
| `challenge` / `challenge` | `GET /tiktok/hashtag/{name}` | `name` (path, required) | Retrieve TikTok hashtag details |
| `challengeList` / `challenge_list` | `GET /tiktok/hashtags` | `id` (query, required), `cursor` (query, optional) | Retrieve TikTok hashtag posts |
| `creativeCenterFilters` / `creative_center_filters` | `GET /tiktok/creative-center/filters` | — | Retrieve TikTok Creative Center filter taxonomy |
| `creativeCenterHashtags` / `creative_center_hashtags` | `GET /tiktok/creative-center/hashtags` | `country_code` (query, required), `period` (query, optional; values: `7`, `30`, `90`), `industry_id` (query, optional; values: `10000000000`, `11000000000`, `12000000000`, `13000000000`, `14000000000`, `15000000000`, `17000000000`, `18000000000`, `19000000000`, `21000000000`, `22000000000`, `23000000000`, `24000000000`, `25000000000`, `26000000000`, `27000000000`, `28000000000`, `29000000000`) | Retrieve TikTok Creative Center trending hashtags |
| `creativeCenterTopContent` / `creative_center_top_content` | `GET /tiktok/creative-center/top-content` | `include_comments` (query, optional) | Retrieve TikTok Creative Center top content |
| `creativeCenterVideos` / `creative_center_videos` | `GET /tiktok/creative-center/videos` | `country_code` (query, required), `period` (query, optional; values: `7`, `30`), `sort_by` (query, optional; values: `views`, `engagement`, `six_second_views`), `content_label_id` (query, optional), `content_label_ids` (query, optional; values: `11002`, `11003`, `11010`, `11013`, `11015`), `organic_only` (query, optional) | Retrieve TikTok Creative Center trending videos |
| `explore` / `explore` | `GET /tiktok/explore/{id}` | `id` (path, required) | Retrieve the TikTok explore feed for a category |
| `mobileFeed` / `mobile_feed` | `GET /tiktok/mobile/feed` | `count` (query, optional), `cursor` (query, optional) | Retrieve the TikTok mobile For You feed |
| `popularTrendCountryIndustryMeta` / `popular_trend_country_industry_meta` | `GET /tiktok/popular-trend/country-industry-meta` | — | Retrieve TikTok popular-trend country and industry metadata |
| `post` / `post` | `GET /tiktok/post/{id}` | `id` (path, required) | Retrieve TikTok video details |
| `profile` / `profile` | `GET /tiktok/profile/{handler}` | `handler` (path, required) | Retrieve a TikTok profile |
| `profilePost` / `profile_post` | `GET /tiktok/posts` | `secUid` (query, required), `cursor` (query, optional), `sort_type` (query, optional; values: `0`, `1`, `2`) | Retrieve posts from a TikTok profile |
| `search` / `search` | `GET /tiktok/search` | `keyword` (query, required), `cursor` (query, optional), `count` (query, optional) | Search TikTok videos |
| `searchHashtag` / `search_hashtag` | `GET /tiktok/search/hashtag` | `keyword` (query, required), `cursor` (query, optional), `count` (query, optional) | Search TikTok hashtags |
| `searchUser` / `search_user` | `GET /tiktok/search/user` | `keyword` (query, required), `cursor` (query, optional) | Search TikTok users |
| `topAdsAnalysis` / `top_ads_analysis` | `GET /tiktok/top-ads/analysis` | `material_id` (query, required), `metric` (query, optional; values: `retain_ctr`, `retain_cvr`, `click_cnt`, `convert_cnt`, `play_retain_cnt`), `period_type` (query, optional; values: `7`, `30`, `180`) | Retrieve TikTok Top Ads interactive time analysis |
| `topAdsDetail` / `top_ads_detail` | `GET /tiktok/top-ads/detail` | `material_id` (query, required) | Retrieve TikTok Top Ads detail |
| `topAdsFilters` / `top_ads_filters` | `GET /tiktok/top-ads/filters` | — | Retrieve TikTok Top Ads filters |
| `topAdsList` / `top_ads_list` | `GET /tiktok/top-ads/list` | `period` (query, optional; values: `7`, `30`, `180`), `page` (query, optional), `limit` (query, optional), `order_by` (query, optional; values: `for_you`, `impression`, `ctr`, `play_2s_rate`, `play_6s_rate`, `cvr`, `like`), `country_code` (query, optional), `keyword` (query, optional), `industry` (query, optional), `objective` (query, optional), `ad_language` (query, optional), `pattern_label` (query, optional), `duration` (query, optional; values: `time-2`, `time-3`, `time-4`, `time-5`, `time-6`, `time-7`), `like` (query, optional; values: `1`, `2`, `3`, `4`, `5`), `ad_format` (query, optional; values: `1`, `2`) | Retrieve TikTok Top Ads |
| `topAdsLocationInfo` / `top_ads_location_info` | `GET /tiktok/top-ads/location-info` | `module` (query, optional) | Retrieve TikTok Top Ads location info |
| `topAdsLocations` / `top_ads_locations` | `GET /tiktok/top-ads/locations` | — | Retrieve TikTok Top Ads locations |
| `topAdsRecommend` / `top_ads_recommend` | `GET /tiktok/top-ads/recommend` | `material_id` (query, required), `page` (query, optional), `limit` (query, optional) | Retrieve TikTok Top Ads recommendations |
| `topAdsSafety` / `top_ads_safety` | `GET /tiktok/top-ads/safety` | — | Retrieve TikTok Top Ads safety configuration |
| `topAdsSpotlight` / `top_ads_spotlight` | `GET /tiktok/top-ads/spotlight` | `page` (query, optional), `limit` (query, optional) | Retrieve TikTok Top Ads Spotlight |
| `topAdsSuggestions` / `top_ads_suggestions` | `GET /tiktok/top-ads/suggestions` | `count` (query, optional), `scenario` (query, optional) | Retrieve TikTok Top Ads suggestions |
| `trending` / `trending` | `GET /tiktok/trending` | — | Retrieve TikTok trending posts |
| `videoComments` / `video_comments` | `GET /tiktok/comments` | `aweme_id` (query, required), `cursor` (query, optional) | Retrieve TikTok video comments |

## Client forms

- JavaScript: import `TikTokClient` (also exported as `Client`) from `@crawlora-org/tiktok`; use `new TikTokClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `TikTokClient` (also exported as `Client`) from `crawlora_tiktok`; use `with TikTokClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncTikTokClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
