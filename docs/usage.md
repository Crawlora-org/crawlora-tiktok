# TikTok API endpoint reference and client usage

This reference lists all 53 public TikTok API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/tiktok`, `crawlora-tiktok`, and `crawlora-tiktok` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape TikTok locally; Crawlora is independent from and not endorsed by TikTok or its owners.

The package tracks the public API contract revision `sha256:a027d217d59233b22a7523eb4b5063fa5ec396297a0cfdae9f87f7deaad2402f` bundled with release `0.4.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `tiktok`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `category` | `category` | `tiktok.category` | `GET /tiktok/category` | — | List TikTok explore categories |
| `challenge` | `challenge` | `tiktok.challenge` | `GET /tiktok/hashtag/{name}` | `name` (path, required) | Retrieve TikTok hashtag details |
| `challengeList` | `challenge_list` | `tiktok.challenge_list` | `GET /tiktok/hashtags` | `id` (query, required), `cursor` (query, optional) | Retrieve TikTok hashtag posts |
| `creativeCenterFilters` | `creative_center_filters` | `tiktok.creative_center_filters` | `GET /tiktok/creative-center/filters` | — | Retrieve TikTok Creative Center filter taxonomy |
| `creativeCenterHashtags` | `creative_center_hashtags` | `tiktok.creative_center_hashtags` | `GET /tiktok/creative-center/hashtags` | `country_code` (query, required), `period` (query, optional; values: `7`, `30`, `90`), `industry_id` (query, optional; values: `10000000000`, `11000000000`, `12000000000`, `13000000000`, `14000000000`, `15000000000`, `17000000000`, `18000000000`, `19000000000`, `21000000000`, `22000000000`, `23000000000`, `24000000000`, `25000000000`, `26000000000`, `27000000000`, `28000000000`, `29000000000`) | Retrieve TikTok Creative Center trending hashtags |
| `creativeCenterTopContent` | `creative_center_top_content` | `tiktok.creative_center_top_content` | `GET /tiktok/creative-center/top-content` | `include_comments` (query, optional) | Retrieve TikTok Creative Center top content |
| `creativeCenterVideos` | `creative_center_videos` | `tiktok.creative_center_videos` | `GET /tiktok/creative-center/videos` | `country_code` (query, required), `period` (query, optional; values: `7`, `30`), `sort_by` (query, optional; values: `views`, `engagement`, `six_second_views`), `content_label_id` (query, optional), `content_label_ids` (query, optional; values: `11002`, `11003`, `11010`, `11013`, `11015`), `organic_only` (query, optional) | Retrieve TikTok Creative Center trending videos |
| `explore` | `explore` | `tiktok.explore` | `GET /tiktok/explore/{id}` | `id` (path, required) | Retrieve the TikTok explore feed for a category |
| `mobileAnchorList` | `mobile_anchor_list` | `tiktok.mobile_anchor_list` | `GET /tiktok/mobile/anchor/list` | — | Anchor catalogue used by the video composer |
| `mobileCommentReplies` | `mobile_comment_replies` | `tiktok.mobile_comment_replies` | `GET /tiktok/mobile/comment/replies` | `aweme_id` (query, required), `comment_id` (query, required), `cursor` (query, optional), `count` (query, optional) | Retrieve replies to a TikTok comment |
| `mobileComments` | `mobile_comments` | `tiktok.mobile_comments` | `GET /tiktok/mobile/comments` | `aweme_id` (query, required), `cursor` (query, optional), `count` (query, optional) | Retrieve comments for a TikTok video |
| `mobileFeed` | `mobile_feed` | `tiktok.mobile_feed` | `GET /tiktok/mobile/feed` | `count` (query, optional), `cursor` (query, optional) | Retrieve the TikTok mobile For You feed |
| `mobileFeedPost` | `mobile_feed_post` | `tiktok.mobile_feed_post` | `GET /tiktok/mobile/feed/post` | — | Fetch the app's primary feed call (POST, protobuf) decoded without a schema |
| `mobileHashtag` | `mobile_hashtag` | `tiktok.mobile_hashtag` | `GET /tiktok/mobile/hashtag` | `name` (query, required) | Retrieve a TikTok hashtag |
| `mobileHashtagPosts` | `mobile_hashtag_posts` | `tiktok.mobile_hashtag_posts` | `GET /tiktok/mobile/hashtag/posts` | `name` (query, required), `sort` (query, optional; values: `fresh`, `popular`), `count` (query, optional), `cursor` (query, optional) | Retrieve videos for a TikTok hashtag |
| `mobileHashtags` | `mobile_hashtags` | `tiktok.mobile_hashtags` | `GET /tiktok/mobile/hashtags` | `keyword` (query, required), `count` (query, optional), `cursor` (query, optional) | Search TikTok hashtags |
| `mobileLiveEffects` | `mobile_live_effects` | `tiktok.mobile_live_effects` | `GET /tiktok/mobile/live/effects` | — | Retrieve TikTok LIVE effects |
| `mobileLiveGifts` | `mobile_live_gifts` | `tiktok.mobile_live_gifts` | `GET /tiktok/mobile/live/gifts` | — | Retrieve TikTok LIVE gifts |
| `mobileLiveSearch` | `mobile_live_search` | `tiktok.mobile_live_search` | `GET /tiktok/mobile/live/search` | `keyword` (query, required), `count` (query, optional) | Search TikTok LIVE streams |
| `mobileMusicBeats` | `mobile_music_beats` | `tiktok.mobile_music_beats` | `GET /tiktok/mobile/music/beats` | `count` (query, optional) | Retrieve TikTok music beats |
| `mobileMusicCollections` | `mobile_music_collections` | `tiktok.mobile_music_collections` | `GET /tiktok/mobile/music/collections` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok music collections |
| `mobileMusicPick` | `mobile_music_pick` | `tiktok.mobile_music_pick` | `GET /tiktok/mobile/music/pick` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok sound chart picks |
| `mobileMusicPosts` | `mobile_music_posts` | `tiktok.mobile_music_posts` | `GET /tiktok/mobile/music/posts` | `music_id` (query, required), `count` (query, optional), `cursor` (query, optional) | Retrieve videos for a TikTok sound |
| `mobileMusicRelated` | `mobile_music_related` | `tiktok.mobile_music_related` | `GET /tiktok/mobile/music/related` | `aweme_id` (query, required), `count` (query, optional), `cursor` (query, optional) | Retrieve sounds related to a TikTok video |
| `mobileMusicTrending` | `mobile_music_trending` | `tiktok.mobile_music_trending` | `GET /tiktok/mobile/music/trending` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok trending sounds |
| `mobileSearch` | `mobile_search` | `tiktok.mobile_search` | `GET /tiktok/mobile/search` | `keyword` (query, required), `count` (query, optional), `offset` (query, optional) | Search TikTok videos on the mobile API |
| `mobileSearchMusic` | `mobile_search_music` | `tiktok.mobile_search_music` | `GET /tiktok/mobile/search/music` | `keyword` (query, required), `count` (query, optional), `offset` (query, optional) | Search TikTok sounds on the mobile API |
| `mobileSearchPlace` | `mobile_search_place` | `tiktok.mobile_search_place` | `GET /tiktok/mobile/search/place` | `keyword` (query, required), `count` (query, optional) | Search TikTok places |
| `mobileSearchPreInfo` | `mobile_search_pre_info` | `tiktok.mobile_search_pre_info` | `GET /tiktok/mobile/search/pre-info` | `keyword` (query, optional), `count` (query, optional) | Pre-search info token for a search session |
| `mobileSearchSug` | `mobile_search_sug` | `tiktok.mobile_search_sug` | `GET /tiktok/mobile/search/sug` | `keyword` (query, required), `count` (query, optional) | Retrieve TikTok search suggestions |
| `mobileSearchTabs` | `mobile_search_tabs` | `tiktok.mobile_search_tabs` | `GET /tiktok/mobile/search/tabs` | `keyword` (query, required) | Search tabs available for a keyword |
| `mobileSearchUser` | `mobile_search_user` | `tiktok.mobile_search_user` | `GET /tiktok/mobile/search/user` | `keyword` (query, required), `count` (query, optional), `cursor` (query, optional) | Search TikTok users on the mobile API |
| `mobileTrendingCategories` | `mobile_trending_categories` | `tiktok.mobile_trending_categories` | `GET /tiktok/mobile/trending/categories` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok trending categories |
| `mobileTrendingEffects` | `mobile_trending_effects` | `tiktok.mobile_trending_effects` | `GET /tiktok/mobile/trending/effects` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok trending effects |
| `popularTrendCountryIndustryMeta` | `popular_trend_country_industry_meta` | `tiktok.popular_trend_country_industry_meta` | `GET /tiktok/popular-trend/country-industry-meta` | — | Retrieve TikTok popular-trend country and industry metadata |
| `post` | `post` | `tiktok.post` | `GET /tiktok/post/{id}` | `id` (path, required) | Retrieve TikTok video details |
| `profile` | `profile` | `tiktok.profile` | `GET /tiktok/profile/{handler}` | `handler` (path, required) | Retrieve a TikTok profile |
| `profilePost` | `profile_post` | `tiktok.profile_post` | `GET /tiktok/posts` | `secUid` (query, required), `cursor` (query, optional), `sort_type` (query, optional; values: `0`, `1`, `2`) | Retrieve posts from a TikTok profile |
| `search` | `search` | `tiktok.search` | `GET /tiktok/search` | `keyword` (query, required), `cursor` (query, optional), `count` (query, optional) | Search TikTok videos |
| `searchHashtag` | `search_hashtag` | `tiktok.search_hashtag` | `GET /tiktok/search/hashtag` | `keyword` (query, required), `cursor` (query, optional), `count` (query, optional) | Search TikTok hashtags |
| `searchUser` | `search_user` | `tiktok.search_user` | `GET /tiktok/search/user` | `keyword` (query, required), `cursor` (query, optional) | Search TikTok users |
| `topAdsAnalysis` | `top_ads_analysis` | `tiktok.top_ads_analysis` | `GET /tiktok/top-ads/analysis` | `material_id` (query, required), `metric` (query, optional; values: `retain_ctr`, `retain_cvr`, `click_cnt`, `convert_cnt`, `play_retain_cnt`), `period_type` (query, optional; values: `7`, `30`, `180`) | Retrieve TikTok Top Ads interactive time analysis |
| `topAdsDetail` | `top_ads_detail` | `tiktok.top_ads_detail` | `GET /tiktok/top-ads/detail` | `material_id` (query, required) | Retrieve TikTok Top Ads detail |
| `topAdsFilters` | `top_ads_filters` | `tiktok.top_ads_filters` | `GET /tiktok/top-ads/filters` | — | Retrieve TikTok Top Ads filters |
| `topAdsList` | `top_ads_list` | `tiktok.top_ads_list` | `GET /tiktok/top-ads/list` | `period` (query, optional; values: `7`, `30`, `180`), `page` (query, optional), `limit` (query, optional), `order_by` (query, optional; values: `for_you`, `impression`, `ctr`, `play_2s_rate`, `play_6s_rate`, `cvr`, `like`), `country_code` (query, optional), `keyword` (query, optional), `industry` (query, optional), `objective` (query, optional), `ad_language` (query, optional), `pattern_label` (query, optional), `duration` (query, optional; values: `time-2`, `time-3`, `time-4`, `time-5`, `time-6`, `time-7`), `like` (query, optional; values: `1`, `2`, `3`, `4`, `5`), `ad_format` (query, optional; values: `1`, `2`) | Retrieve TikTok Top Ads |
| `topAdsLocationInfo` | `top_ads_location_info` | `tiktok.top_ads_location_info` | `GET /tiktok/top-ads/location-info` | `module` (query, optional) | Retrieve TikTok Top Ads location info |
| `topAdsLocations` | `top_ads_locations` | `tiktok.top_ads_locations` | `GET /tiktok/top-ads/locations` | — | Retrieve TikTok Top Ads locations |
| `topAdsRecommend` | `top_ads_recommend` | `tiktok.top_ads_recommend` | `GET /tiktok/top-ads/recommend` | `material_id` (query, required), `page` (query, optional), `limit` (query, optional) | Retrieve TikTok Top Ads recommendations |
| `topAdsSafety` | `top_ads_safety` | `tiktok.top_ads_safety` | `GET /tiktok/top-ads/safety` | — | Retrieve TikTok Top Ads safety configuration |
| `topAdsSpotlight` | `top_ads_spotlight` | `tiktok.top_ads_spotlight` | `GET /tiktok/top-ads/spotlight` | `page` (query, optional), `limit` (query, optional) | Retrieve TikTok Top Ads Spotlight |
| `topAdsSuggestions` | `top_ads_suggestions` | `tiktok.top_ads_suggestions` | `GET /tiktok/top-ads/suggestions` | `count` (query, optional), `scenario` (query, optional) | Retrieve TikTok Top Ads suggestions |
| `trending` | `trending` | `tiktok.trending` | `GET /tiktok/trending` | — | Retrieve TikTok trending posts |
| `videoComments` | `video_comments` | `tiktok.video_comments` | `GET /tiktok/comments` | `aweme_id` (query, required), `cursor` (query, optional) | Retrieve TikTok video comments |

## Client forms

- JavaScript: import `TikTokClient` (also exported as `Client`) from `@crawlora-org/tiktok`; use `new TikTokClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `TikTokClient` (also exported as `Client`) from `crawlora_tiktok`; use `with TikTokClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncTikTokClient`, used with `async with` and `await`.
- Rust: add `crawlora-tiktok` with Cargo; import `Client` and the generated operation parameter struct, then call `client.tiktok.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-tiktok/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
