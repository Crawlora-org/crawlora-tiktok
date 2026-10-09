# Crawlora TikTok JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `25`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tiktok | `tiktok.category` | `tiktok-category` | `GET /tiktok/category` | none | `ApiKeyAuth` | `TiktokCategoryResponse` |  |
| tiktok | `tiktok.videoComments` | `tiktok-video-comments` | `GET /tiktok/comments` | `aweme_id` (query string required)<br>`cursor` (query number) | `ApiKeyAuth` | `TiktokVideoCommentsResponse` |  |
| tiktok | `tiktok.creativeCenterHashtags` | `tiktok-creative-center-hashtags` | `GET /tiktok/creative-center/hashtags` | `country_code` (query string required)<br>`period` (query "7" \| "30") | `ApiKeyAuth` | `TiktokCreativeCenterHashtagsResponse` |  |
| tiktok | `tiktok.creativeCenterVideos` | `tiktok-creative-center-videos` | `GET /tiktok/creative-center/videos` | `country_code` (query string required)<br>`period` (query "7" \| "30")<br>`sort_by` (query "views" \| "engagement" \| "six_second_views")<br>`content_label_id` (query string)<br>`organic_only` (query boolean) | `ApiKeyAuth` | `TiktokCreativeCenterVideosResponse` |  |
| tiktok | `tiktok.explore` | `tiktok-explore` | `GET /tiktok/explore/{id}` | `id` (path number required) | `ApiKeyAuth` | `TiktokExploreResponse` |  |
| tiktok | `tiktok.challenge` | `tiktok-challenge` | `GET /tiktok/hashtag/{name}` | `name` (path string required) | `ApiKeyAuth` | `TiktokChallengeResponse` |  |
| tiktok | `tiktok.challengeList` | `tiktok-challenge-list` | `GET /tiktok/hashtags` | `id` (query string required)<br>`cursor` (query number) | `ApiKeyAuth` | `TiktokChallengeListResponse` |  |
| tiktok | `tiktok.popularTrendCountryIndustryMeta` | `tiktok-popular-trend-country-industry-meta` | `GET /tiktok/popular-trend/country-industry-meta` | none | `ApiKeyAuth` | `TiktokPopularTrendCountryIndustryMetaResponse` |  |
| tiktok | `tiktok.post` | `tiktok-post` | `GET /tiktok/post/{id}` | `id` (path string required) | `ApiKeyAuth` | `TiktokPostResponse` |  |
| tiktok | `tiktok.profilePost` | `tiktok-profile-post` | `GET /tiktok/posts` | `secUid` (query string required)<br>`cursor` (query number)<br>`sort_type` (query "0" \| "1" \| "2") | `ApiKeyAuth` | `TiktokProfilePostResponse` |  |
| tiktok | `tiktok.profile` | `tiktok-profile` | `GET /tiktok/profile/{handler}` | `handler` (path string required) | `ApiKeyAuth` | `TiktokProfileResponse` |  |
| tiktok | `tiktok.search` | `tiktok-search` | `GET /tiktok/search` | `keyword` (query string required)<br>`cursor` (query number)<br>`count` (query number) | `ApiKeyAuth` | `TiktokSearchResponse` |  |
| tiktok | `tiktok.searchHashtag` | `tiktok-search-hashtag` | `GET /tiktok/search/hashtag` | `keyword` (query string required)<br>`cursor` (query number)<br>`count` (query number) | `ApiKeyAuth` | `TiktokSearchHashtagResponse` |  |
| tiktok | `tiktok.searchUser` | `tiktok-search-user` | `GET /tiktok/search/user` | `keyword` (query string required)<br>`cursor` (query number) | `ApiKeyAuth` | `TiktokSearchUserResponse` |  |
| tiktok | `tiktok.topAdsAnalysis` | `tiktok-top-ads-analysis` | `GET /tiktok/top-ads/analysis` | `material_id` (query string required)<br>`metric` (query "retain_ctr" \| "retain_cvr" \| "click_cnt" \| "convert_cnt" \| "play_retain_cnt")<br>`period_type` (query "7" \| "30" \| "180") | `ApiKeyAuth` | `TiktokTopAdsAnalysisResponse` |  |
| tiktok | `tiktok.topAdsDetail` | `tiktok-top-ads-detail` | `GET /tiktok/top-ads/detail` | `material_id` (query string required) | `ApiKeyAuth` | `TiktokTopAdsDetailResponse` |  |
| tiktok | `tiktok.topAdsFilters` | `tiktok-top-ads-filters` | `GET /tiktok/top-ads/filters` | none | `ApiKeyAuth` | `TiktokTopAdsFiltersResponse` |  |
| tiktok | `tiktok.topAdsList` | `tiktok-top-ads-list` | `GET /tiktok/top-ads/list` | `period` (query "7" \| "30" \| "180")<br>`page` (query number)<br>`limit` (query number)<br>`order_by` (query "for_you" \| "impression" \| "ctr" \| "play_2s_rate" \| "play_6s_rate" \| "cvr" \| "like")<br>`country_code` (query string)<br>`keyword` (query string)<br>`industry` (query string)<br>`objective` (query string)<br>`ad_language` (query string)<br>`pattern_label` (query string)<br>`duration` (query "time-2" \| "time-3" \| "time-4" \| "time-5" \| "time-6" \| "time-7")<br>`like` (query "1" \| "2" \| "3" \| "4" \| "5")<br>`ad_format` (query "1" \| "2") | `ApiKeyAuth` | `TiktokTopAdsListResponse` |  |
| tiktok | `tiktok.topAdsLocationInfo` | `tiktok-top-ads-location-info` | `GET /tiktok/top-ads/location-info` | `module` (query number) | `ApiKeyAuth` | `TiktokTopAdsLocationInfoResponse` |  |
| tiktok | `tiktok.topAdsLocations` | `tiktok-top-ads-locations` | `GET /tiktok/top-ads/locations` | none | `ApiKeyAuth` | `TiktokTopAdsLocationsResponse` |  |
| tiktok | `tiktok.topAdsRecommend` | `tiktok-top-ads-recommend` | `GET /tiktok/top-ads/recommend` | `material_id` (query string required)<br>`page` (query number)<br>`limit` (query number) | `ApiKeyAuth` | `TiktokTopAdsRecommendResponse` |  |
| tiktok | `tiktok.topAdsSafety` | `tiktok-top-ads-safety` | `GET /tiktok/top-ads/safety` | none | `ApiKeyAuth` | `TiktokTopAdsSafetyResponse` |  |
| tiktok | `tiktok.topAdsSpotlight` | `tiktok-top-ads-spotlight` | `GET /tiktok/top-ads/spotlight` | `page` (query number)<br>`limit` (query number) | `ApiKeyAuth` | `TiktokTopAdsSpotlightResponse` |  |
| tiktok | `tiktok.topAdsSuggestions` | `tiktok-top-ads-suggestions` | `GET /tiktok/top-ads/suggestions` | `count` (query number)<br>`scenario` (query number) | `ApiKeyAuth` | `TiktokTopAdsSuggestionsResponse` |  |
| tiktok | `tiktok.trending` | `tiktok-trending` | `GET /tiktok/trending` | none | `ApiKeyAuth` | `TiktokTrendingResponse` |  |
