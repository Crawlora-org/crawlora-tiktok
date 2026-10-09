# TikTok client usage

The `@crawlora-org/tiktok` and `crawlora-tiktok` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape TikTok locally; Crawlora is independent from and not endorsed by TikTok or its owners.

The package tracks the public API contract revision `sha256:54cbbf627ce0c1a21749439fd3c7fe474e0c855da0977c70674aa93de7e1e8be` bundled with release `0.1.1`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 25 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `tiktok` group and the generated `Client` alias.

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
| `creativeCenterHashtags` / `creative_center_hashtags` | `GET /tiktok/creative-center/hashtags` | `country_code` (query, required), `period` (query, optional; values: `7`, `30`) | Retrieve TikTok Creative Center trending hashtags |
| `creativeCenterVideos` / `creative_center_videos` | `GET /tiktok/creative-center/videos` | `country_code` (query, required), `period` (query, optional; values: `7`, `30`), `sort_by` (query, optional; values: `views`, `engagement`, `six_second_views`), `content_label_id` (query, optional), `organic_only` (query, optional) | Retrieve TikTok Creative Center trending videos |
| `explore` / `explore` | `GET /tiktok/explore/{id}` | `id` (path, required) | Retrieve the TikTok explore feed for a category |
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
