# TikTok API endpoint reference and client usage

This reference lists all 90 public TikTok API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/tiktok`, `crawlora-tiktok`, and `crawlora-tiktok` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape TikTok locally; Crawlora is independent from and not endorsed by TikTok or its owners.

The package tracks the public API contract revision `sha256:5823222daa31ec6f43dbc20c0ebf31a2e341cdbf1e93509f340d2126c102421f` bundled with release `0.5.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

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
| `mobileCollectionDetail` | `mobile_collection_detail` | `tiktok.mobile_collection_detail` | `GET /tiktok/mobile/collection/detail` | `collection_id` (query, required) | Get TikTok collection detail on the mobile API |
| `mobileCollectionList` | `mobile_collection_list` | `tiktok.mobile_collection_list` | `GET /tiktok/mobile/collection/list` | `user_id` (query, required), `cursor` (query, optional), `count` (query, optional) | List TikTok collections on the mobile API |
| `mobileCollectionVideos` | `mobile_collection_videos` | `tiktok.mobile_collection_videos` | `GET /tiktok/mobile/collection/videos` | `collection_id` (query, required), `cursor` (query, optional), `count` (query, optional) | Get videos in a TikTok collection on the mobile API |
| `mobileCommentReplies` | `mobile_comment_replies` | `tiktok.mobile_comment_replies` | `GET /tiktok/mobile/comment/replies` | `aweme_id` (query, required), `comment_id` (query, required), `cursor` (query, optional), `count` (query, optional) | Retrieve replies to a TikTok comment |
| `mobileComments` | `mobile_comments` | `tiktok.mobile_comments` | `GET /tiktok/mobile/comments` | `aweme_id` (query, required), `cursor` (query, optional), `count` (query, optional) | Retrieve comments for a TikTok video |
| `mobileFeed` | `mobile_feed` | `tiktok.mobile_feed` | `GET /tiktok/mobile/feed` | `count` (query, optional), `cursor` (query, optional) | Retrieve the TikTok mobile For You feed |
| `mobileFeedOffline` | `mobile_feed_offline` | `tiktok.mobile_feed_offline` | `GET /tiktok/mobile/feed/offline` | `pull_type` (query, optional), `count` (query, optional) | Fetch the app's cached-pull offline feed (protobuf) decoded without a schema |
| `mobileFeedPost` | `mobile_feed_post` | `tiktok.mobile_feed_post` | `GET /tiktok/mobile/feed/post` | — | Fetch the app's primary feed call (POST, protobuf) decoded without a schema |
| `mobileHashtag` | `mobile_hashtag` | `tiktok.mobile_hashtag` | `GET /tiktok/mobile/hashtag` | `name` (query, required) | Retrieve a TikTok hashtag |
| `mobileHashtagPosts` | `mobile_hashtag_posts` | `tiktok.mobile_hashtag_posts` | `GET /tiktok/mobile/hashtag/posts` | `name` (query, required), `sort` (query, optional; values: `fresh`, `popular`), `count` (query, optional), `cursor` (query, optional) | Retrieve videos for a TikTok hashtag |
| `mobileHashtags` | `mobile_hashtags` | `tiktok.mobile_hashtags` | `GET /tiktok/mobile/hashtags` | `keyword` (query, required), `count` (query, optional), `cursor` (query, optional) | Search TikTok hashtags |
| `mobileLiveEffects` | `mobile_live_effects` | `tiktok.mobile_live_effects` | `GET /tiktok/mobile/live/effects` | — | Retrieve TikTok LIVE effects |
| `mobileLiveGifts` | `mobile_live_gifts` | `tiktok.mobile_live_gifts` | `GET /tiktok/mobile/live/gifts` | — | Retrieve TikTok LIVE gifts |
| `mobileLiveHashtags` | `mobile_live_hashtags` | `tiktok.mobile_live_hashtags` | `GET /tiktok/mobile/live/hashtags` | — | LIVE category/game reference catalogue (hashtags, live-studio/voice/third-party tags, game tags) |
| `mobileLiveRoom` | `mobile_live_room` | `tiktok.mobile_live_room` | `GET /tiktok/mobile/live/room` | `room_id` (query, required) | LIVE room detail: status, viewers, owner, stream URLs, cover |
| `mobileLiveRoomByUser` | `mobile_live_room_by_user` | `tiktok.mobile_live_room_by_user` | `GET /tiktok/mobile/live/room-by-user` | `user_id` (query, required) | LIVE room by user: the room a user is currently streaming |
| `mobileLiveSearch` | `mobile_live_search` | `tiktok.mobile_live_search` | `GET /tiktok/mobile/live/search` | `keyword` (query, required), `count` (query, optional) | Search TikTok LIVE streams |
| `mobileLiveTabs` | `mobile_live_tabs` | `tiktok.mobile_live_tabs` | `GET /tiktok/mobile/live/tabs` | — | Fetch the LIVE tab catalogue |
| `mobileMusicBeats` | `mobile_music_beats` | `tiktok.mobile_music_beats` | `GET /tiktok/mobile/music/beats` | `count` (query, optional) | Retrieve TikTok music beats |
| `mobileMusicChart` | `mobile_music_chart` | `tiktok.mobile_music_chart` | `GET /tiktok/mobile/music/chart` | `chart_region` (query, optional; values: `AE`, `BR`, `CA`, `DE`, `EG`, `FR`, `JP`, `KR`, `LB`, `MX`, `NG`, `SA`, `TR`, `US`, `ZA`), `cursor` (query, optional), `count` (query, optional) | List a regional TikTok sound chart |
| `mobileMusicChoices` | `mobile_music_choices` | `tiktok.mobile_music_choices` | `GET /tiktok/mobile/music/choices` | — | Recommended sounds for video creation |
| `mobileMusicCollectionList` | `mobile_music_collection_list` | `tiktok.mobile_music_collection_list` | `GET /tiktok/mobile/music/collection-list` | `count` (query, optional), `cursor` (query, optional) | Music collection list (paged browse) |
| `mobileMusicCollections` | `mobile_music_collections` | `tiktok.mobile_music_collections` | `GET /tiktok/mobile/music/collections` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok music collections |
| `mobileMusicDetail` | `mobile_music_detail` | `tiktok.mobile_music_detail` | `GET /tiktok/mobile/music/detail` | `music_id` (query, required) | Retrieve one TikTok sound |
| `mobileMusicPick` | `mobile_music_pick` | `tiktok.mobile_music_pick` | `GET /tiktok/mobile/music/pick` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok sound chart picks |
| `mobileMusicPosts` | `mobile_music_posts` | `tiktok.mobile_music_posts` | `GET /tiktok/mobile/music/posts` | `music_id` (query, required), `sort` (query, optional; values: `fresh`, `popular`), `count` (query, optional), `cursor` (query, optional) | Retrieve videos for a TikTok sound |
| `mobileMusicRelated` | `mobile_music_related` | `tiktok.mobile_music_related` | `GET /tiktok/mobile/music/related` | `aweme_id` (query, required), `count` (query, optional), `cursor` (query, optional) | Retrieve sounds related to a TikTok video |
| `mobileMusicTrending` | `mobile_music_trending` | `tiktok.mobile_music_trending` | `GET /tiktok/mobile/music/trending` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok trending sounds |
| `mobileMvVideos` | `mobile_mv_videos` | `tiktok.mobile_mv_videos` | `GET /tiktok/mobile/mv/videos` | `mv_id` (query, required), `cursor` (query, optional) | MV channel feed: the app's music-video tab, paged |
| `mobilePlaceDetail` | `mobile_place_detail` | `tiktok.mobile_place_detail` | `GET /tiktok/mobile/place/detail` | `poi_id` (query, required), `review_count` (query, optional), `review_cursor` (query, optional), `merged_count` (query, optional), `video_cursor` (query, optional), `enter_from` (query, optional) | Place (POI) detail from the mobile app's Places surface |
| `mobilePlaceInfo` | `mobile_place_info` | `tiktok.mobile_place_info` | `GET /tiktok/mobile/place/info` | `poi_id` (query, required) | Compact place (POI) record: address, coordinates, rating, hours, counters |
| `mobilePlaceMedia` | `mobile_place_media` | `tiktok.mobile_place_media` | `GET /tiktok/mobile/place/media` | `poi_id` (query, required), `cursor` (query, optional), `size` (query, optional), `data_version` (query, optional) | List a TikTok place's mixed media |
| `mobilePlacePhotos` | `mobile_place_photos` | `tiktok.mobile_place_photos` | `GET /tiktok/mobile/place/photos` | `poi_id` (query, required) | Place photo album with per-photo attribution |
| `mobilePlaceReviews` | `mobile_place_reviews` | `tiktok.mobile_place_reviews` | `GET /tiktok/mobile/place/reviews` | `poi_id` (query, required), `cursor` (query, optional), `count` (query, optional), `sort_type` (query, optional; values: `1`, `2`) | List a TikTok place's reviews |
| `mobilePlaceVideos` | `mobile_place_videos` | `tiktok.mobile_place_videos` | `GET /tiktok/mobile/place/videos` | `poi_id` (query, required), `count` (query, optional), `cursor` (query, optional) | Videos posted at one place (paged) |
| `mobilePlaylistDetail` | `mobile_playlist_detail` | `tiktok.mobile_playlist_detail` | `GET /tiktok/mobile/playlist/detail` | `mix_id` (query, required), `user_id` (query, optional), `sec_user_id` (query, optional) | Retrieve one TikTok playlist |
| `mobilePlaylistList` | `mobile_playlist_list` | `tiktok.mobile_playlist_list` | `GET /tiktok/mobile/playlist/list` | `user_id` (query, optional), `sec_user_id` (query, optional), `cursor` (query, optional) | List a creator's TikTok playlists |
| `mobilePlaylistVideos` | `mobile_playlist_videos` | `tiktok.mobile_playlist_videos` | `GET /tiktok/mobile/playlist/videos` | `mix_id` (query, required), `cursor` (query, optional), `count` (query, optional) | List a playlist's videos |
| `mobileSearch` | `mobile_search` | `tiktok.mobile_search` | `GET /tiktok/mobile/search` | `keyword` (query, required), `count` (query, optional), `offset` (query, optional), `search_id` (query, optional) | Search TikTok videos on the mobile API |
| `mobileSearchEffects` | `mobile_search_effects` | `tiktok.mobile_search_effects` | `GET /tiktok/mobile/search/effects` | `keyword` (query, required), `count` (query, optional), `cursor` (query, optional), `search_id` (query, optional) | Search TikTok effects/stickers by keyword |
| `mobileSearchHashtags` | `mobile_search_hashtags` | `tiktok.mobile_search_hashtags` | `GET /tiktok/mobile/search/hashtags` | `keyword` (query, required), `count` (query, optional) | Hashtag suggestions for a keyword (hashtag typeahead) |
| `mobileSearchMusic` | `mobile_search_music` | `tiktok.mobile_search_music` | `GET /tiktok/mobile/search/music` | `keyword` (query, required), `count` (query, optional), `offset` (query, optional) | Search TikTok sounds on the mobile API |
| `mobileSearchPhotos` | `mobile_search_photos` | `tiktok.mobile_search_photos` | `GET /tiktok/mobile/search/photos` | `keyword` (query, required), `count` (query, optional), `offset` (query, optional), `sort_type` (query, optional), `publish_time` (query, optional), `search_source` (query, optional) | Search the mobile app's photo-post tab |
| `mobileSearchPlace` | `mobile_search_place` | `tiktok.mobile_search_place` | `GET /tiktok/mobile/search/place` | `keyword` (query, required), `count` (query, optional) | Search TikTok places |
| `mobileSearchPreInfo` | `mobile_search_pre_info` | `tiktok.mobile_search_pre_info` | `GET /tiktok/mobile/search/pre-info` | `keyword` (query, optional), `count` (query, optional) | Pre-search info token for a search session |
| `mobileSearchStream` | `mobile_search_stream` | `tiktok.mobile_search_stream` | `GET /tiktok/mobile/search/stream` | `keyword` (query, required), `count` (query, optional), `offset` (query, optional), `search_source` (query, optional), `sort_type` (query, optional; values: `0`, `1`, `3`), `publish_time` (query, optional), `filter_selected` (query, optional) | Run the app's primary (streaming) general search |
| `mobileSearchSug` | `mobile_search_sug` | `tiktok.mobile_search_sug` | `GET /tiktok/mobile/search/sug` | `keyword` (query, required), `count` (query, optional) | Retrieve TikTok search suggestions |
| `mobileSearchTabs` | `mobile_search_tabs` | `tiktok.mobile_search_tabs` | `GET /tiktok/mobile/search/tabs` | `keyword` (query, required) | Search tabs available for a keyword |
| `mobileSearchUser` | `mobile_search_user` | `tiktok.mobile_search_user` | `GET /tiktok/mobile/search/user` | `keyword` (query, required), `count` (query, optional), `cursor` (query, optional) | Search TikTok users on the mobile API |
| `mobileSearchVideos` | `mobile_search_videos` | `tiktok.mobile_search_videos` | `GET /tiktok/mobile/search/videos` | `keyword` (query, required), `count` (query, optional), `offset` (query, optional), `sort_type` (query, optional; values: `0`, `1`, `3`), `publish_time` (query, optional), `search_source` (query, optional), `search_id` (query, optional) | Search TikTok videos on the mobile API (video tab) |
| `mobileTranslationDescription` | `mobile_translation_description` | `tiktok.mobile_translation_description` | `GET /tiktok/mobile/translation/description` | `item_id` (query, required), `target_lang` (query, optional) | Translate one TikTok video caption |
| `mobileTrendingCategories` | `mobile_trending_categories` | `tiktok.mobile_trending_categories` | `GET /tiktok/mobile/trending/categories` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok trending categories |
| `mobileTrendingEffects` | `mobile_trending_effects` | `tiktok.mobile_trending_effects` | `GET /tiktok/mobile/trending/effects` | `count` (query, optional), `cursor` (query, optional) | Retrieve TikTok trending effects |
| `mobileUserFollowers` | `mobile_user_followers` | `tiktok.mobile_user_followers` | `GET /tiktok/mobile/user/followers` | `user_id` (query, required), `count` (query, optional), `cursor` (query, optional) | Retrieve the followers of a TikTok creator |
| `mobileUserFollowing` | `mobile_user_following` | `tiktok.mobile_user_following` | `GET /tiktok/mobile/user/following` | `user_id` (query, required), `count` (query, optional), `cursor` (query, optional) | Retrieve the accounts a TikTok creator follows |
| `mobileUserOriginalEffects` | `mobile_user_original_effects` | `tiktok.mobile_user_original_effects` | `GET /tiktok/mobile/user/original-effects` | `user_id` (query, required), `cursor` (query, optional), `count` (query, optional) | List a creator's original TikTok effects |
| `mobileUserOriginalMusic` | `mobile_user_original_music` | `tiktok.mobile_user_original_music` | `GET /tiktok/mobile/user/original-music` | `user_id` (query, required), `cursor` (query, optional), `count` (query, optional) | List a creator's original TikTok sounds |
| `mobileUserPosts` | `mobile_user_posts` | `tiktok.mobile_user_posts` | `GET /tiktok/mobile/user/posts` | `user_id` (query, optional), `sec_user_id` (query, optional), `count` (query, optional), `cursor` (query, optional), `sort_type` (query, optional) | Retrieve the videos posted by a TikTok creator |
| `mobileUserProfile` | `mobile_user_profile` | `tiktok.mobile_user_profile` | `GET /tiktok/mobile/user/profile` | `user_id` (query, optional), `sec_user_id` (query, optional) | Retrieve a TikTok creator profile |
| `mobileUserRecommendations` | `mobile_user_recommendations` | `tiktok.mobile_user_recommendations` | `GET /tiktok/mobile/user/recommendations` | `count` (query, optional) | Recommended creators on the mobile app's Following page |
| `mobileVideoDetail` | `mobile_video_detail` | `tiktok.mobile_video_detail` | `GET /tiktok/mobile/video/detail` | `aweme_id` (query, required) | Retrieve one TikTok video |
| `mobileVideoSubtitles` | `mobile_video_subtitles` | `tiktok.mobile_video_subtitles` | `GET /tiktok/mobile/video/subtitles` | `video_id` (query, required), `language` (query, required) | Video captions translated into a target language |
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
