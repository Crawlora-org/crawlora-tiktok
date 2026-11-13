from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelTiktokTrendingResponseDoc = TypedDict('ModelTiktokTrendingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokTrendingResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokTrendingResp = TypedDict('ModelTiktokTrendingResp', {
    'cursor': NotRequired[str],
    'extra': NotRequired[dict[str, Any]],
    'hasMore': NotRequired[bool],
    'itemList': NotRequired[list[Any]],
    'log_pb': NotRequired[dict[str, Any]],
    'statusCode': NotRequired[int],
    'statusMsg': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'trendingTopics': NotRequired[list[Any]],
}, total=False)

ModelPopulartrendTopAdsSuggestionsResponseDoc = TypedDict('ModelPopulartrendTopAdsSuggestionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsSuggestionsResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsSuggestionsResp = TypedDict('ModelPopularTrendTopAdsSuggestionsResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsSpotlightResponseDoc = TypedDict('ModelPopulartrendTopAdsSpotlightResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsSpotlightResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsSpotlightResp = TypedDict('ModelPopularTrendTopAdsSpotlightResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsPagination = TypedDict('ModelPopularTrendTopAdsPagination', {
    'has_more': NotRequired[bool],
    'page': NotRequired[int],
    'size': NotRequired[int],
    'total': NotRequired[int],
    'total_count': NotRequired[int],
}, total=False)

ModelPopularTrendTopAdsMaterial = TypedDict('ModelPopularTrendTopAdsMaterial', {
    'ad_title': NotRequired[str],
    'brand_name': NotRequired[str],
    'comment': NotRequired[int],
    'cost': NotRequired[int],
    'country_code': NotRequired[list[str]],
    'ctr': NotRequired[float],
    'favorite': NotRequired[bool],
    'has_summary': NotRequired[bool],
    'highlight': NotRequired[str],
    'highlight_text': NotRequired[str],
    'id': NotRequired[str],
    'industry_key': NotRequired[str],
    'is_search': NotRequired[bool],
    'keyword_list': NotRequired[list[str]],
    'landing_page': NotRequired[str],
    'like': NotRequired[int],
    'objective_key': NotRequired[str],
    'objectives': NotRequired[list[ModelPopularTrendTopAdsFilterItem]],
    'pattern_label': NotRequired[list[ModelPopularTrendTopAdsFilterItem]],
    'share': NotRequired[int],
    'source': NotRequired[str],
    'source_key': NotRequired[int],
    'video_info': NotRequired[ModelPopularTrendTopAdsVideoInfo],
    'voice_over': NotRequired[bool],
}, total=False)

ModelPopularTrendTopAdsVideoInfo = TypedDict('ModelPopularTrendTopAdsVideoInfo', {
    'cover': NotRequired[str],
    'duration': NotRequired[float],
    'height': NotRequired[int],
    'vid': NotRequired[str],
    'video_url': NotRequired[dict[str, str]],
    'width': NotRequired[int],
}, total=False)

ModelPopularTrendTopAdsFilterItem = TypedDict('ModelPopularTrendTopAdsFilterItem', {
    'has_conversion': NotRequired[bool],
    'id': NotRequired[dict[str, Any]],
    'label': NotRequired[str],
    'parent_id': NotRequired[dict[str, Any]],
    'value': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsSafetyResponseDoc = TypedDict('ModelPopulartrendTopAdsSafetyResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsSafetyResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsSafetyResp = TypedDict('ModelPopularTrendTopAdsSafetyResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsRecommendResponseDoc = TypedDict('ModelPopulartrendTopAdsRecommendResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsRecommendResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsRecommendResp = TypedDict('ModelPopularTrendTopAdsRecommendResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsLocationsResponseDoc = TypedDict('ModelPopulartrendTopAdsLocationsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsLocationsResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsLocationsResp = TypedDict('ModelPopularTrendTopAdsLocationsResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsLocationInfoResponseDoc = TypedDict('ModelPopulartrendTopAdsLocationInfoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsLocationInfoResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsLocationInfoResp = TypedDict('ModelPopularTrendTopAdsLocationInfoResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsListResponseDoc = TypedDict('ModelPopulartrendTopAdsListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsListResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsListResp = TypedDict('ModelPopularTrendTopAdsListResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsFiltersResponseDoc = TypedDict('ModelPopulartrendTopAdsFiltersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsFiltersResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsFiltersResp = TypedDict('ModelPopularTrendTopAdsFiltersResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsDetailResponseDoc = TypedDict('ModelPopulartrendTopAdsDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsDetailResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsDetailResp = TypedDict('ModelPopularTrendTopAdsDetailResp', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsMaterial],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopulartrendTopAdsAnalysisResponseDoc = TypedDict('ModelPopulartrendTopAdsAnalysisResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendTopAdsAnalysisResp],
    'msg': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsAnalysisResp = TypedDict('ModelPopularTrendTopAdsAnalysisResp', {
    'code': NotRequired[int],
    'data': NotRequired[dict[str, Any]],
    'msg': NotRequired[str],
    'request_id': NotRequired[str],
}, total=False)

ModelPopularTrendTopAdsAnalysisPoint = TypedDict('ModelPopularTrendTopAdsAnalysisPoint', {
    'second': NotRequired[int],
    'value': NotRequired[float],
}, total=False)

ModelTiktokSearchUserResponseDoc = TypedDict('ModelTiktokSearchUserResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokSearchUserResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokSearchUserResp = TypedDict('ModelTiktokSearchUserResp', {
    'challenge_list': NotRequired[Any],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'feedback_type': NotRequired[str],
    'global_doodle_config': NotRequired[Any],
    'has_more': NotRequired[int],
    'input_keyword': NotRequired[str],
    'log_pb': NotRequired[dict[str, Any]],
    'music_list': NotRequired[Any],
    'qc': NotRequired[str],
    'rid': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'type': NotRequired[int],
    'user_list': NotRequired[list[Any]],
}, total=False)

ModelTiktokSearchHashtagResponseDoc = TypedDict('ModelTiktokSearchHashtagResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokSearchHashtagResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokSearchHashtagResp = TypedDict('ModelTiktokSearchHashtagResp', {
    'challenge_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[int],
    'input_keyword': NotRequired[str],
    'log_pb': NotRequired[dict[str, Any]],
    'music_list': NotRequired[Any],
    'qc': NotRequired[str],
    'rid': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'type': NotRequired[int],
    'user_list': NotRequired[Any],
}, total=False)

ModelTiktokSearchResponseDoc = TypedDict('ModelTiktokSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokSearchResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokSearchResp = TypedDict('ModelTiktokSearchResp', {
    'cursor': NotRequired[int],
    'data': NotRequired[list[Any]],
    'extra': NotRequired[Any],
    'feedback_type': NotRequired[str],
    'has_more': NotRequired[int],
    'input_keyword': NotRequired[str],
    'itemList': NotRequired[list[Any]],
    'log_pb': NotRequired[dict[str, Any]],
    'qc': NotRequired[str],
    'rid': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'type': NotRequired[int],
}, total=False)

ModelTiktokProfileResponseDoc = TypedDict('ModelTiktokProfileResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokProfile],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokProfile = TypedDict('ModelTiktokProfile', {
    'stats': NotRequired[ModelTiktokProfileStats],
    'user': NotRequired[ModelTiktokUser],
}, total=False)

ModelTiktokUser = TypedDict('ModelTiktokUser', {
    'avatarLarger': NotRequired[str],
    'bioLink': NotRequired[dict[str, Any]],
    'commerceUserInfo': NotRequired[dict[str, Any]],
    'createTime': NotRequired[int],
    'id': NotRequired[str],
    'isOrganization': NotRequired[int],
    'language': NotRequired[str],
    'nickname': NotRequired[str],
    'privateAccount': NotRequired[bool],
    'region': NotRequired[str],
    'secUid': NotRequired[str],
    'secret': NotRequired[bool],
    'signature': NotRequired[str],
    'ttSeller': NotRequired[bool],
    'uniqueId': NotRequired[str],
    'verified': NotRequired[bool],
}, total=False)

ModelTiktokProfileStats = TypedDict('ModelTiktokProfileStats', {
    'diggCount': NotRequired[int],
    'followerCount': NotRequired[int],
    'followingCount': NotRequired[int],
    'friendCount': NotRequired[int],
    'heart': NotRequired[int],
    'heartCount': NotRequired[int],
    'videoCount': NotRequired[int],
}, total=False)

ModelTiktokProfilePostResponseDoc = TypedDict('ModelTiktokProfilePostResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokUserPostLinkResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokUserPostLinkResp = TypedDict('ModelTiktokUserPostLinkResp', {
    'cursor': NotRequired[str],
    'extra': NotRequired[dict[str, Any]],
    'hasMore': NotRequired[bool],
    'itemList': NotRequired[list[Any]],
    'log_pb': NotRequired[dict[str, Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokPostResponseDoc = TypedDict('ModelTiktokPostResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokVideoDetailResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokVideoDetailResp = TypedDict('ModelTiktokVideoDetailResp', {
    'extra': NotRequired[dict[str, Any]],
    'itemInfo': NotRequired[Any],
    'log_pb': NotRequired[dict[str, Any]],
    'shareMeta': NotRequired[dict[str, Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelPopulartrendCountryIndustryMetaResponseDoc = TypedDict('ModelPopulartrendCountryIndustryMetaResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelPopularTrendCountryIndustryMeta],
    'msg': NotRequired[str],
}, total=False)

ModelPopularTrendCountryIndustryMeta = TypedDict('ModelPopularTrendCountryIndustryMeta', {
    'country': NotRequired[list[ModelPopularTrendCountryIndustryMetaItem]],
    'industry': NotRequired[list[ModelPopularTrendCountryIndustryMetaItem]],
}, total=False)

ModelPopularTrendCountryIndustryMetaItem = TypedDict('ModelPopularTrendCountryIndustryMetaItem', {
    'id': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelTiktokmobileVideoSubtitlesResponseDoc = TypedDict('ModelTiktokmobileVideoSubtitlesResponseDoc', {
    'content_source': NotRequired[str],
    'cue_count': NotRequired[int],
    'cues': NotRequired[list[ModelTiktokmobileSubtitleCue]],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'language': NotRequired[str],
    'variant': NotRequired[str],
    'video_id': NotRequired[str],
    'webvtt': NotRequired[str],
}, total=False)

ModelTiktokmobileSubtitleCue = TypedDict('ModelTiktokmobileSubtitleCue', {
    'end': NotRequired[str],
    'end_ms': NotRequired[int],
    'start': NotRequired[str],
    'start_ms': NotRequired[int],
    'text': NotRequired[str],
}, total=False)

ModelTiktokmobileVideoDetailResponseDoc = TypedDict('ModelTiktokmobileVideoDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileVideoDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileVideoDetailResponse = TypedDict('ModelTiktokmobileVideoDetailResponse', {
    'aweme_detail': NotRequired[Any],
    'extra': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserRecommendationsResponseDoc = TypedDict('ModelTiktokmobileUserRecommendationsResponseDoc', {
    'extra': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'user_list': NotRequired[list[Any]],
}, total=False)

ModelTiktokmobileUserProfileResponseDoc = TypedDict('ModelTiktokmobileUserProfileResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileUserProfileResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserProfileResponse = TypedDict('ModelTiktokmobileUserProfileResponse', {
    'common': NotRequired[Any],
    'extra': NotRequired[Any],
    'header': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'nav_bar': NotRequired[Any],
    'profile_tab': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserPostsResponseDoc = TypedDict('ModelTiktokmobileUserPostsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileUserPostsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserPostsResponse = TypedDict('ModelTiktokmobileUserPostsResponse', {
    'aweme_list': NotRequired[list[Any]],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'max_cursor': NotRequired[int],
    'min_cursor': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserOriginalMusicResponseDoc = TypedDict('ModelTiktokmobileUserOriginalMusicResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileUserOriginalMusicResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserOriginalMusicResponse = TypedDict('ModelTiktokmobileUserOriginalMusicResponse', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'groups': NotRequired[list[Any]],
    'has_more': NotRequired[bool],
    'honor_label': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'music': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserOriginalEffectsResponseDoc = TypedDict('ModelTiktokmobileUserOriginalEffectsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileUserOriginalEffectsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserOriginalEffectsResponse = TypedDict('ModelTiktokmobileUserOriginalEffectsResponse', {
    'cursor': NotRequired[int],
    'effect': NotRequired[list[Any]],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserFollowingResponseDoc = TypedDict('ModelTiktokmobileUserFollowingResponseDoc', {
    'extra': NotRequired[Any],
    'followings': NotRequired[list[Any]],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'max_time': NotRequired[int],
    'min_time': NotRequired[int],
    'myself_user_id': NotRequired[Any],
    'next_page_token': NotRequired[str],
    'offset': NotRequired[int],
    'rec_has_more': NotRequired[bool],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTiktokmobileUserFollowersResponseDoc = TypedDict('ModelTiktokmobileUserFollowersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileUserFollowersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileUserFollowersResponse = TypedDict('ModelTiktokmobileUserFollowersResponse', {
    'extra': NotRequired[Any],
    'followers': NotRequired[list[Any]],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'max_time': NotRequired[int],
    'min_time': NotRequired[int],
    'myself_user_id': NotRequired[str],
    'next_page_token': NotRequired[str],
    'offset': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTiktokmobileStickerDiscoverResponseDoc = TypedDict('ModelTiktokmobileStickerDiscoverResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileStickerDiscoverResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileStickerDiscoverResponse = TypedDict('ModelTiktokmobileStickerDiscoverResponse', {
    'aweme_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'feed_session_id': NotRequired[str],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCategoryListResponseDoc = TypedDict('ModelTiktokmobileCategoryListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileCategoryListResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCategoryListResponse = TypedDict('ModelTiktokmobileCategoryListResponse', {
    'category_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'device_type': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileTranslationDescriptionResponseDoc = TypedDict('ModelTiktokmobileTranslationDescriptionResponseDoc', {
    'extra': NotRequired[Any],
    'fetched_at': NotRequired[str],
    'format': NotRequired[int],
    'host': NotRequired[str],
    'item_id': NotRequired[str],
    'log_pb': NotRequired[Any],
    'perf_metrics': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'target_lang': NotRequired[str],
    'text': NotRequired[str],
    'translated_client_text': NotRequired[Any],
    'variant': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchVideosResponseDoc = TypedDict('ModelTiktokmobileSearchVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileSearchVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchVideosResponse = TypedDict('ModelTiktokmobileSearchVideosResponse', {
    'aweme_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'feedback_type': NotRequired[str],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'search_id': NotRequired[str],
    'search_item_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchUsersResponseDoc = TypedDict('ModelTiktokmobileSearchUsersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileSearchUsersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchUsersResponse = TypedDict('ModelTiktokmobileSearchUsersResponse', {
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'user_list': NotRequired[list[Any]],
}, total=False)

ModelTiktokmobileSearchTabsResponseDoc = TypedDict('ModelTiktokmobileSearchTabsResponseDoc', {
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'is_failed': NotRequired[int],
    'keyword': NotRequired[str],
    'tabs': NotRequired[list[str]],
}, total=False)

ModelTiktokmobileSearchSuggestionResponseDoc = TypedDict('ModelTiktokmobileSearchSuggestionResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileSearchSuggestionResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchSuggestionResponse = TypedDict('ModelTiktokmobileSearchSuggestionResponse', {
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'rid': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'sug_list': NotRequired[list[ModelTiktokmobileSearchSuggestion]],
}, total=False)

ModelTiktokmobileSearchSuggestion = TypedDict('ModelTiktokmobileSearchSuggestion', {
    'content': NotRequired[str],
    'extra_info': NotRequired[Any],
    'highlight_pos': NotRequired[Any],
    'pos': NotRequired[Any],
    'rich_sug_sec_pos': NotRequired[Any],
    'sug_type': NotRequired[str],
    'word_record': NotRequired[Any],
}, total=False)

ModelTiktokmobileSearchStreamResponseDoc = TypedDict('ModelTiktokmobileSearchStreamResponseDoc', {
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'documents': NotRequired[list[Any]],
    'fetched_at': NotRequired[str],
    'frame_count': NotRequired[int],
    'frames': NotRequired[list[Any]],
    'has_more': NotRequired[bool],
    'host': NotRequired[str],
    'keyword': NotRequired[str],
    'offset': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchPreInfoResponseDoc = TypedDict('ModelTiktokmobileSearchPreInfoResponseDoc', {
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'pre_info_id': NotRequired[str],
    'ttl': NotRequired[int],
}, total=False)

ModelTiktokmobileSearchPlaceResponseDoc = TypedDict('ModelTiktokmobileSearchPlaceResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileSearchPlaceResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchPlaceResponse = TypedDict('ModelTiktokmobileSearchPlaceResponse', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'feedback_type': NotRequired[str],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'poi_info': NotRequired[ModelTiktokmobilePlacePoicontainer],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlacePoicontainer = TypedDict('ModelTiktokmobilePlacePoicontainer', {
    'poi_info': NotRequired[list[Any]],
}, total=False)

ModelTiktokmobileSearchPhotosResponseDoc = TypedDict('ModelTiktokmobileSearchPhotosResponseDoc', {
    'aweme_list': NotRequired[list[Any]],
    'backtrace': NotRequired[Any],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'feedback_type': NotRequired[str],
    'has_more': NotRequired[int],
    'log_pb': NotRequired[Any],
    'response_cropped': NotRequired[int],
    'search_item_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchMusicResponseDoc = TypedDict('ModelTiktokmobileSearchMusicResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileSearchMusicResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchMusicResponse = TypedDict('ModelTiktokmobileSearchMusicResponse', {
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'music': NotRequired[list[Any]],
    'music_info_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTiktokmobileHashtagSuggestionsResponseDoc = TypedDict('ModelTiktokmobileHashtagSuggestionsResponseDoc', {
    'extra': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'rid': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'sug_list': NotRequired[list[Any]],
    'words_query_record': NotRequired[Any],
}, total=False)

ModelTiktokmobileSearchEffectsResponseDoc = TypedDict('ModelTiktokmobileSearchEffectsResponseDoc', {
    'bind_effects': NotRequired[Any],
    'collection': NotRequired[Any],
    'cursor': NotRequired[int],
    'effects': NotRequired[list[Any]],
    'has_more': NotRequired[bool],
    'search_id': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'use_hot': NotRequired[bool],
}, total=False)

ModelTiktokmobileSearchGeneralResponseDoc = TypedDict('ModelTiktokmobileSearchGeneralResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileSearchGeneralResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileSearchGeneralResponse = TypedDict('ModelTiktokmobileSearchGeneralResponse', {
    'cursor': NotRequired[int],
    'data': NotRequired[list[Any]],
    'has_more': NotRequired[bool],
    'search_id': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaylistVideosResponseDoc = TypedDict('ModelTiktokmobilePlaylistVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobilePlaylistVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaylistVideosResponse = TypedDict('ModelTiktokmobilePlaylistVideosResponse', {
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'item_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaylistListResponseDoc = TypedDict('ModelTiktokmobilePlaylistListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobilePlaylistListResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaylistListResponse = TypedDict('ModelTiktokmobilePlaylistListResponse', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'mix_list': NotRequired[list[ModelTiktokmobilePlaylistSummary]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTiktokmobilePlaylistSummary = TypedDict('ModelTiktokmobilePlaylistSummary', {
    'author': NotRequired[Any],
    'creator_name': NotRequired[str],
    'last_add_video_timestamp': NotRequired[int],
    'mix_id': NotRequired[str],
    'mix_type': NotRequired[int],
    'name': NotRequired[str],
    'share_info': NotRequired[Any],
    'statistic': NotRequired[Any],
    'status': NotRequired[Any],
}, total=False)

ModelTiktokmobilePlaylistDetailResponseDoc = TypedDict('ModelTiktokmobilePlaylistDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobilePlaylistDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaylistDetailResponse = TypedDict('ModelTiktokmobilePlaylistDetailResponse', {
    'extra': NotRequired[Any],
    'is_collect': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'mix': NotRequired[ModelTiktokmobilePlaylistSummary],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaceVideosResponseDoc = TypedDict('ModelTiktokmobilePlaceVideosResponseDoc', {
    'aweme_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'host': NotRequired[str],
    'item_count': NotRequired[int],
    'poi_id': NotRequired[str],
    'poi_info': NotRequired[Any],
}, total=False)

ModelTiktokmobilePlaceReviewsResponseDoc = TypedDict('ModelTiktokmobilePlaceReviewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobilePlaceReviewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaceReviewsResponse = TypedDict('ModelTiktokmobilePlaceReviewsResponse', {
    'collect_info': NotRequired[Any],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'folded_cursor': NotRequired[int],
    'folded_has_more': NotRequired[bool],
    'has_more': NotRequired[bool],
    'is_hide_review_summary': NotRequired[bool],
    'landing_tab': NotRequired[int],
    'log_pb': NotRequired[Any],
    'poi_id': NotRequired[str],
    'poi_name': NotRequired[str],
    'post_review_description': NotRequired[str],
    'post_review_sub_description': NotRequired[str],
    'review_summary': NotRequired[Any],
    'review_tags': NotRequired[list[Any]],
    'reviews': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlacePhotosResponseDoc = TypedDict('ModelTiktokmobilePlacePhotosResponseDoc', {
    'categories': NotRequired[list[Any]],
    'category_tab_info': NotRequired[Any],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'photo_count': NotRequired[int],
    'poi_id': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaceMediaResponseDoc = TypedDict('ModelTiktokmobilePlaceMediaResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobilePlaceMediaResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaceMediaResponse = TypedDict('ModelTiktokmobilePlaceMediaResponse', {
    'data_version': NotRequired[str],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'item_list': NotRequired[list[Any]],
    'log_pb': NotRequired[Any],
    'next_cursor': NotRequired[str],
    'pos': NotRequired[Any],
    'post_bottom_bar_style': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelTiktokmobilePlaceInfoResponseDoc = TypedDict('ModelTiktokmobilePlaceInfoResponseDoc', {
    'address': NotRequired[str],
    'average_price': NotRequired[str],
    'category': NotRequired[str],
    'city_code': NotRequired[str],
    'claim_store_status': NotRequired[bool],
    'cover': NotRequired[Any],
    'favorite_count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'is_collected': NotRequired[bool],
    'latitude': NotRequired[str],
    'longitude': NotRequired[str],
    'name': NotRequired[str],
    'no_rating': NotRequired[bool],
    'opening_hours': NotRequired[str],
    'opening_status': NotRequired[bool],
    'parent_poi': NotRequired[Any],
    'place': NotRequired[dict[str, Any]],
    'poi_id': NotRequired[str],
    'region_code': NotRequired[str],
    'review_count': NotRequired[int],
    'review_score': NotRequired[float],
    'review_score_display': NotRequired[str],
    'share_desc': NotRequired[str],
    'share_url': NotRequired[str],
    'video_count': NotRequired[int],
}, total=False)

ModelTiktokmobilePlaceDetailResponseDoc = TypedDict('ModelTiktokmobilePlaceDetailResponseDoc', {
    'fetched_at': NotRequired[str],
    'frame_count': NotRequired[int],
    'frames': NotRequired[list[Any]],
    'has_more_posts': NotRequired[bool],
    'has_more_reviews': NotRequired[bool],
    'host': NotRequired[str],
    'layout': NotRequired[dict[str, Any]],
    'nodes': NotRequired[dict[str, Any]],
    'page_id': NotRequired[str],
    'poi_id': NotRequired[str],
    'post_count': NotRequired[int],
    'post_cursor': NotRequired[int],
    'review_count': NotRequired[int],
    'top_video_count': NotRequired[int],
}, total=False)

ModelTiktokmobileMvFeedResponseDoc = TypedDict('ModelTiktokmobileMvFeedResponseDoc', {
    'aweme_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'host': NotRequired[str],
    'item_count': NotRequired[int],
    'log_pb': NotRequired[Any],
    'mv_id': NotRequired[str],
    'original_aweme_id': NotRequired[str],
    'page_extra': NotRequired[Any],
    'top_awemes': NotRequired[list[Any]],
}, total=False)

ModelTiktokmobileHotMusicResponseDoc = TypedDict('ModelTiktokmobileHotMusicResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileHotMusicResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileHotMusicResponse = TypedDict('ModelTiktokmobileHotMusicResponse', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'msg': NotRequired[str],
    'music_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicRelatedResponseDoc = TypedDict('ModelTiktokmobileMusicRelatedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicRelatedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicRelatedResponse = TypedDict('ModelTiktokmobileMusicRelatedResponse', {
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'music_list': NotRequired[list[Any]],
    'music_type': NotRequired[int],
    'recall_info_list': NotRequired[list[Any]],
    'similar_song_ids': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicFreshAwemeResponseDoc = TypedDict('ModelTiktokmobileMusicFreshAwemeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicFreshAwemeResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicFreshAwemeResponse = TypedDict('ModelTiktokmobileMusicFreshAwemeResponse', {
    'aweme_list': NotRequired[list[Any]],
    'can_pin_video': NotRequired[Any],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'need_lazy_loading': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicPickResponseDoc = TypedDict('ModelTiktokmobileMusicPickResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicPickResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicPickResponse = TypedDict('ModelTiktokmobileMusicPickResponse', {
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'mc_list': NotRequired[list[Any]],
    'music_list': NotRequired[list[Any]],
    'radio_cursor': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicDetailResponseDoc = TypedDict('ModelTiktokmobileMusicDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicDetailResponse = TypedDict('ModelTiktokmobileMusicDetailResponse', {
    'ai_recommend_music': NotRequired[Any],
    'ai_recommend_video': NotRequired[Any],
    'behind_the_song_exist': NotRequired[bool],
    'cost_time_info': NotRequired[Any],
    'extra': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'msg': NotRequired[str],
    'music_chart_rank': NotRequired[Any],
    'music_info': NotRequired[Any],
    'rec_list': NotRequired[Any],
    'similar_music': NotRequired[Any],
    'similar_music_ids': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicCollectionFeedResponseDoc = TypedDict('ModelTiktokmobileMusicCollectionFeedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicCollectionFeedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicCollectionFeedResponse = TypedDict('ModelTiktokmobileMusicCollectionFeedResponse', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'mcf_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicCollectionListResponseDoc = TypedDict('ModelTiktokmobileMusicCollectionListResponseDoc', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'mc_list': NotRequired[list[Any]],
    'msg': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicChoicesResponseDoc = TypedDict('ModelTiktokmobileMusicChoicesResponseDoc', {
    'extra': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'music_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicChartResponseDoc = TypedDict('ModelTiktokmobileMusicChartResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicChartResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicChartResponse = TypedDict('ModelTiktokmobileMusicChartResponse', {
    'chart_info': NotRequired[Any],
    'cover_image_url': NotRequired[str],
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'msg': NotRequired[str],
    'music_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicBeatsSongsResponseDoc = TypedDict('ModelTiktokmobileMusicBeatsSongsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileMusicBeatsSongsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileMusicBeatsSongsResponse = TypedDict('ModelTiktokmobileMusicBeatsSongsResponse', {
    'extra': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'music_list': NotRequired[list[Any]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveTabsResponseDoc = TypedDict('ModelTiktokmobileLiveTabsResponseDoc', {
    'data': NotRequired[list[Any]],
    'extra': NotRequired[Any],
    'status_code': NotRequired[int],
}, total=False)

ModelTiktokmobileLiveSearchResponseDoc = TypedDict('ModelTiktokmobileLiveSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileLiveSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveSearchResponse = TypedDict('ModelTiktokmobileLiveSearchResponse', {
    'cursor': NotRequired[int],
    'data': NotRequired[list[Any]],
    'extra': NotRequired[Any],
    'extra_data': NotRequired[Any],
    'feedback_type': NotRequired[str],
    'global_doodle_config': NotRequired[Any],
    'guide_search_words': NotRequired[Any],
    'has_more': NotRequired[bool],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveRoomInfoResponseDoc = TypedDict('ModelTiktokmobileLiveRoomInfoResponseDoc', {
    'cover': NotRequired[Any],
    'create_time': NotRequired[int],
    'data': NotRequired[Any],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'owner': NotRequired[ModelTiktokmobileLiveRoomOwner],
    'room_id': NotRequired[str],
    'stats': NotRequired[ModelTiktokmobileLiveRoomStats],
    'status': NotRequired[int],
    'stream': NotRequired[ModelTiktokmobileLiveRoomStream],
    'title': NotRequired[str],
    'user_count': NotRequired[int],
    'user_id': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveRoomStream = TypedDict('ModelTiktokmobileLiveRoomStream', {
    'candidate_resolution': NotRequired[list[str]],
    'default_resolution': NotRequired[str],
    'flv_pull_url': NotRequired[dict[str, str]],
    'hls_pull_url': NotRequired[str],
    'rtmp_pull_url': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveRoomStats = TypedDict('ModelTiktokmobileLiveRoomStats', {
    'comment_count': NotRequired[int],
    'enter_count': NotRequired[int],
    'follow_count': NotRequired[int],
    'like_count': NotRequired[int],
    'replay_viewers': NotRequired[int],
    'share_count': NotRequired[int],
    'total_user': NotRequired[int],
    'watch_user_count': NotRequired[int],
}, total=False)

ModelTiktokmobileLiveRoomOwner = TypedDict('ModelTiktokmobileLiveRoomOwner', {
    'avatar': NotRequired[Any],
    'nickname': NotRequired[str],
    'user_id': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveHashtagCatalogResponseDoc = TypedDict('ModelTiktokmobileLiveHashtagCatalogResponseDoc', {
    'extra': NotRequired[Any],
    'fetched_at': NotRequired[str],
    'game_hashtag': NotRequired[ModelTiktokmobileLiveHashtag],
    'game_tag_count': NotRequired[int],
    'game_tag_list': NotRequired[list[ModelTiktokmobileLiveGameTag]],
    'hashtags': NotRequired[list[ModelTiktokmobileLiveHashtag]],
    'host': NotRequired[str],
    'live_studio_hashtags': NotRequired[list[ModelTiktokmobileLiveHashtag]],
    'live_voice_hashtags': NotRequired[list[ModelTiktokmobileLiveHashtag]],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'third_party_hashtags': NotRequired[list[ModelTiktokmobileLiveHashtag]],
}, total=False)

ModelTiktokmobileLiveHashtag = TypedDict('ModelTiktokmobileLiveHashtag', {
    'id': NotRequired[int],
    'image': NotRequired[Any],
    'namespace': NotRequired[int],
    'title': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveGameTag = TypedDict('ModelTiktokmobileLiveGameTag', {
    'bundle_id': NotRequired[str],
    'full_name': NotRequired[str],
    'game_category': NotRequired[list[ModelTiktokmobileLiveGameCategory]],
    'gar': NotRequired[list[Any]],
    'hashtag_id': NotRequired[list[Any]],
    'hashtag_list': NotRequired[list[ModelTiktokmobileLiveHashtag]],
    'id': NotRequired[int],
    'is_new_game': NotRequired[bool],
    'landscape': NotRequired[int],
    'package_name': NotRequired[str],
    'short_name': NotRequired[str],
    'show_name': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveGameCategory = TypedDict('ModelTiktokmobileLiveGameCategory', {
    'game_type': NotRequired[int],
    'title': NotRequired[str],
}, total=False)

ModelTiktokmobileLiveGiftsResponseDoc = TypedDict('ModelTiktokmobileLiveGiftsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileWebcastGiftListResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileWebcastGiftListResponse = TypedDict('ModelTiktokmobileWebcastGiftListResponse', {
    'data': NotRequired[Any],
    'extra': NotRequired[Any],
    'status_code': NotRequired[int],
}, total=False)

ModelTiktokmobileLiveEffectsResponseDoc = TypedDict('ModelTiktokmobileLiveEffectsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileWebcastEffectsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileWebcastEffectsResponse = TypedDict('ModelTiktokmobileWebcastEffectsResponse', {
    'data': NotRequired[ModelTiktokmobileWebcastEffectsData],
    'extra': NotRequired[Any],
    'status_code': NotRequired[int],
}, total=False)

ModelTiktokmobileWebcastEffectsData = TypedDict('ModelTiktokmobileWebcastEffectsData', {
    'assets': NotRequired[list[Any]],
}, total=False)

ModelTiktokmobileHashtagSearchResponseDoc = TypedDict('ModelTiktokmobileHashtagSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileHashtagSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileHashtagSearchResponse = TypedDict('ModelTiktokmobileHashtagSearchResponse', {
    'challenge_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileHashtagPostsResponseDoc = TypedDict('ModelTiktokmobileHashtagPostsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileHashtagPostsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileHashtagPostsResponse = TypedDict('ModelTiktokmobileHashtagPostsResponse', {
    'aweme_list': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileHashtagInfoResponseDoc = TypedDict('ModelTiktokmobileHashtagInfoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileHashtagInfoResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileHashtagInfoResponse = TypedDict('ModelTiktokmobileHashtagInfoResponse', {
    'ch_info': NotRequired[Any],
    'hashtag_name': NotRequired[str],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileFeedPostResponseDoc = TypedDict('ModelTiktokmobileFeedPostResponseDoc', {
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'items': NotRequired[dict[str, Any]],
    'note': NotRequired[str],
    'strings': NotRequired[list[str]],
}, total=False)

ModelTiktokmobileOfflineFeedResponseDoc = TypedDict('ModelTiktokmobileOfflineFeedResponseDoc', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'items': NotRequired[dict[str, Any]],
    'note': NotRequired[str],
    'pull_type': NotRequired[int],
    'strings': NotRequired[list[str]],
}, total=False)

ModelTiktokmobileFeedResponseDoc = TypedDict('ModelTiktokmobileFeedResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileFeedResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileFeedResponse = TypedDict('ModelTiktokmobileFeedResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
    'items': NotRequired[list[ModelTiktokmobileFeedItem]],
}, total=False)

ModelTiktokmobileFeedItem = TypedDict('ModelTiktokmobileFeedItem', {
    'author_id': NotRequired[int],
    'author_id_str': NotRequired[str],
    'aweme_id': NotRequired[str],
    'create_time': NotRequired[int],
    'share_url': NotRequired[str],
    'statistics': NotRequired[ModelTiktokmobileFeedStatistics],
}, total=False)

ModelTiktokmobileFeedStatistics = TypedDict('ModelTiktokmobileFeedStatistics', {
    'aweme_id': NotRequired[str],
    'collect_count': NotRequired[int],
    'comment_count': NotRequired[int],
    'digg_count': NotRequired[int],
    'download_count': NotRequired[int],
    'forward_count': NotRequired[int],
    'lose_comment_count': NotRequired[int],
    'lose_count': NotRequired[int],
    'play_count': NotRequired[int],
    'repost_count': NotRequired[int],
    'share_count': NotRequired[int],
    'whatsapp_share_count': NotRequired[int],
}, total=False)

ModelTiktokmobileCommentsResponseDoc = TypedDict('ModelTiktokmobileCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileCommentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCommentsResponse = TypedDict('ModelTiktokmobileCommentsResponse', {
    'comments': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTiktokmobileCommentRepliesResponseDoc = TypedDict('ModelTiktokmobileCommentRepliesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileCommentRepliesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCommentRepliesResponse = TypedDict('ModelTiktokmobileCommentRepliesResponse', {
    'comments': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'has_more': NotRequired[bool],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelTiktokmobileCollectionVideosResponseDoc = TypedDict('ModelTiktokmobileCollectionVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileCollectionVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCollectionVideosResponse = TypedDict('ModelTiktokmobileCollectionVideosResponse', {
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'items': NotRequired[list[Any]],
    'log_pb': NotRequired[Any],
    'max_cursor': NotRequired[int],
    'min_cursor': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCollectionListResponseDoc = TypedDict('ModelTiktokmobileCollectionListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileCollectionListResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCollectionListResponse = TypedDict('ModelTiktokmobileCollectionListResponse', {
    'cursor': NotRequired[int],
    'extra': NotRequired[Any],
    'has_more': NotRequired[bool],
    'item_archive_detail_list': NotRequired[list[Any]],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCollectionDetailResponseDoc = TypedDict('ModelTiktokmobileCollectionDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokmobileCollectionDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokmobileCollectionDetailResponse = TypedDict('ModelTiktokmobileCollectionDetailResponse', {
    'extra': NotRequired[Any],
    'item_archive': NotRequired[Any],
    'log_pb': NotRequired[Any],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokmobileAnchorListResponseDoc = TypedDict('ModelTiktokmobileAnchorListResponseDoc', {
    'anchors': NotRequired[list[Any]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'host': NotRequired[str],
}, total=False)

ModelTiktokChallengeListResponseDoc = TypedDict('ModelTiktokChallengeListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokChallengeListResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokChallengeListResp = TypedDict('ModelTiktokChallengeListResp', {
    'cursor': NotRequired[str],
    'extra': NotRequired[dict[str, Any]],
    'hasMore': NotRequired[bool],
    'itemList': NotRequired[list[Any]],
    'log_pb': NotRequired[dict[str, Any]],
    'statusCode': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokChallengeResponseDoc = TypedDict('ModelTiktokChallengeResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokChallengeDetailResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokChallengeDetailResp = TypedDict('ModelTiktokChallengeDetailResp', {
    'challengeInfo': NotRequired[Any],
    'extra': NotRequired[dict[str, Any]],
    'log_pb': NotRequired[dict[str, Any]],
    'shareMeta': NotRequired[dict[str, Any]],
    'statusCode': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelTiktokExploreResponseDoc = TypedDict('ModelTiktokExploreResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokExploreResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokExploreResp = TypedDict('ModelTiktokExploreResp', {
    'cursor': NotRequired[str],
    'extra': NotRequired[dict[str, Any]],
    'hasMore': NotRequired[bool],
    'itemList': NotRequired[list[Any]],
    'log_pb': NotRequired[dict[str, Any]],
    'statusCode': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
}, total=False)

ModelCreativecenterTrendingVideosResponseDoc = TypedDict('ModelCreativecenterTrendingVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCreativecenterTrendingVideosResp],
    'msg': NotRequired[str],
}, total=False)

ModelCreativecenterTrendingVideosResp = TypedDict('ModelCreativecenterTrendingVideosResp', {
    'page_count': NotRequired[int],
    'total_count': NotRequired[int],
    'videos': NotRequired[list[ModelCreativecenterTrendingVideo]],
}, total=False)

ModelCreativecenterTrendingVideo = TypedDict('ModelCreativecenterTrendingVideo', {
    'author_avatar_url': NotRequired[str],
    'author_bio': NotRequired[str],
    'author_follower_count': NotRequired[int],
    'author_handle': NotRequired[str],
    'author_id': NotRequired[str],
    'author_nickname': NotRequired[str],
    'content_tags': NotRequired[list[ModelCreativecenterTrendingVideoContentTag]],
    'content_type': NotRequired[int],
    'cover_url': NotRequired[str],
    'cover_urls': NotRequired[list[ModelCreativecenterTrendingVideoCover]],
    'create_time': NotRequired[int],
    'creator_id': NotRequired[str],
    'engagement_rate': NotRequired[float],
    'engagement_rate_lifetime': NotRequired[float],
    'item_id': NotRequired[str],
    'organic_video_views': NotRequired[int],
    'organic_video_views_lifetime': NotRequired[int],
    'six_seconds_vtr': NotRequired[float],
    'six_seconds_vtr_lifetime': NotRequired[float],
    'title': NotRequired[str],
    'video_url': NotRequired[str],
    'video_views': NotRequired[int],
    'video_views_lifetime': NotRequired[int],
}, total=False)

ModelCreativecenterTrendingVideoCover = TypedDict('ModelCreativecenterTrendingVideoCover', {
    'format': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCreativecenterTrendingVideoContentTag = TypedDict('ModelCreativecenterTrendingVideoContentTag', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelCreativecenterTopContentResponseDoc = TypedDict('ModelCreativecenterTopContentResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCreativecenterTopContentResp],
    'msg': NotRequired[str],
}, total=False)

ModelCreativecenterTopContentResp = TypedDict('ModelCreativecenterTopContentResp', {
    'last_update_time': NotRequired[int],
    'objects': NotRequired[list[ModelCreativecenterTopContentObject]],
}, total=False)

ModelCreativecenterTopContentObject = TypedDict('ModelCreativecenterTopContentObject', {
    'author': NotRequired[ModelCreativecenterTopContentAuthor],
    'comment_keywords': NotRequired[list[ModelCreativecenterTopContentCommentKeyword]],
    'comments': NotRequired[list[ModelCreativecenterTopContentComment]],
    'item': NotRequired[ModelCreativecenterTopContentItem],
    'last_update_time': NotRequired[int],
    'metrics': NotRequired[ModelCreativecenterTopContentMetrics],
    'name': NotRequired[str],
}, total=False)

ModelCreativecenterTopContentMetrics = TypedDict('ModelCreativecenterTopContentMetrics', {
    'engagement_rate': NotRequired[float],
    'six_seconds_vtr': NotRequired[float],
    'video_views': NotRequired[int],
}, total=False)

ModelCreativecenterTopContentItem = TypedDict('ModelCreativecenterTopContentItem', {
    'author_id': NotRequired[str],
    'content_type': NotRequired[int],
    'cover_url': NotRequired[str],
    'cover_urls': NotRequired[list[ModelCreativecenterTrendingVideoCover]],
    'create_time': NotRequired[int],
    'creator_id': NotRequired[str],
    'item_id': NotRequired[str],
    'title': NotRequired[str],
    'video_url': NotRequired[str],
}, total=False)

ModelCreativecenterTopContentComment = TypedDict('ModelCreativecenterTopContentComment', {
    'comment_id': NotRequired[str],
    'create_time': NotRequired[int],
    'like_count': NotRequired[int],
    'text': NotRequired[str],
    'user_avatar_url': NotRequired[str],
    'user_id': NotRequired[str],
    'user_name': NotRequired[str],
}, total=False)

ModelCreativecenterTopContentCommentKeyword = TypedDict('ModelCreativecenterTopContentCommentKeyword', {
    'keyword': NotRequired[str],
    'mention_count': NotRequired[int],
}, total=False)

ModelCreativecenterTopContentAuthor = TypedDict('ModelCreativecenterTopContentAuthor', {
    'avatar_url': NotRequired[str],
    'bio': NotRequired[str],
    'creator_type': NotRequired[int],
    'follower_count': NotRequired[int],
    'handle': NotRequired[str],
    'nickname': NotRequired[str],
    'store_region': NotRequired[str],
}, total=False)

ModelCreativecenterTrendingHashtagsResponseDoc = TypedDict('ModelCreativecenterTrendingHashtagsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCreativecenterTrendingHashtagsResp],
    'msg': NotRequired[str],
}, total=False)

ModelCreativecenterTrendingHashtagsResp = TypedDict('ModelCreativecenterTrendingHashtagsResp', {
    'hashtags': NotRequired[list[ModelCreativecenterTrendingHashtag]],
    'total_count': NotRequired[int],
}, total=False)

ModelCreativecenterTrendingHashtag = TypedDict('ModelCreativecenterTrendingHashtag', {
    'hashtag_id': NotRequired[str],
    'hashtag_name': NotRequired[str],
    'industry_ids': NotRequired[list[int]],
    'popularity_curve': NotRequired[list[ModelCreativecenterHashtagTrendPoint]],
    'publish_count': NotRequired[int],
    'rank': NotRequired[int],
    'top_creators': NotRequired[list[ModelCreativecenterHashtagTopCreator]],
    'video_views': NotRequired[int],
}, total=False)

ModelCreativecenterHashtagTopCreator = TypedDict('ModelCreativecenterHashtagTopCreator', {
    'avatar_url': NotRequired[str],
    'country_code': NotRequired[str],
    'creator_id': NotRequired[str],
    'follower_count': NotRequired[int],
    'handle': NotRequired[str],
    'nickname': NotRequired[str],
    'rank': NotRequired[int],
    'tiktok_uid': NotRequired[str],
}, total=False)

ModelCreativecenterHashtagTrendPoint = TypedDict('ModelCreativecenterHashtagTrendPoint', {
    'timestamp': NotRequired[int],
    'value': NotRequired[float],
}, total=False)

ModelCreativecenterFiltersResponseDoc = TypedDict('ModelCreativecenterFiltersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCreativecenterCreativeCenterFiltersResp],
    'msg': NotRequired[str],
}, total=False)

ModelCreativecenterCreativeCenterFiltersResp = TypedDict('ModelCreativecenterCreativeCenterFiltersResp', {
    'hashtag_countries': NotRequired[list[ModelCreativecenterCountryOption]],
    'hashtag_periods': NotRequired[list[int]],
    'industries': NotRequired[list[ModelCreativecenterIndustryOption]],
    'video_content_tags': NotRequired[list[ModelCreativecenterContentTagOption]],
    'video_countries': NotRequired[list[ModelCreativecenterCountryOption]],
    'video_periods': NotRequired[list[int]],
    'video_sort_by': NotRequired[list[ModelCreativecenterSortOption]],
}, total=False)

ModelCreativecenterSortOption = TypedDict('ModelCreativecenterSortOption', {
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelCreativecenterCountryOption = TypedDict('ModelCreativecenterCountryOption', {
    'code': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelCreativecenterContentTagOption = TypedDict('ModelCreativecenterContentTagOption', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelCreativecenterIndustryOption = TypedDict('ModelCreativecenterIndustryOption', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelTiktokCommentsResponseDoc = TypedDict('ModelTiktokCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelTiktokCommentResp],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokCommentResp = TypedDict('ModelTiktokCommentResp', {
    'alias_comment_deleted': NotRequired[bool],
    'comments': NotRequired[list[Any]],
    'cursor': NotRequired[int],
    'extra': NotRequired[dict[str, Any]],
    'has_filtered_comments': NotRequired[int],
    'has_more': NotRequired[int],
    'log_pb': NotRequired[dict[str, Any]],
    'reply_style': NotRequired[int],
    'status_code': NotRequired[int],
    'status_msg': NotRequired[str],
    'top_gifts': NotRequired[Any],
    'total': NotRequired[int],
}, total=False)

ModelTiktokCategoryResponseDoc = TypedDict('ModelTiktokCategoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[list[ModelTiktokCategory]],
    'msg': NotRequired[str],
}, total=False)

ModelTiktokCategory = TypedDict('ModelTiktokCategory', {
    'name': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

TiktokCategoryResponse = ModelTiktokCategoryResponseDoc
TiktokCategoryParams = TypedDict('TiktokCategoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokVideoCommentsResponse = ModelTiktokCommentsResponseDoc
TiktokVideoCommentsParams = TypedDict('TiktokVideoCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokCreativeCenterFiltersResponse = ModelCreativecenterFiltersResponseDoc
TiktokCreativeCenterFiltersParams = TypedDict('TiktokCreativeCenterFiltersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokCreativeCenterHashtagsResponse = ModelCreativecenterTrendingHashtagsResponseDoc
TiktokCreativeCenterHashtagsParams = TypedDict('TiktokCreativeCenterHashtagsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30', '90']],
    'industry_id': NotRequired[Literal['10000000000', '11000000000', '12000000000', '13000000000', '14000000000', '15000000000', '17000000000', '18000000000', '19000000000', '21000000000', '22000000000', '23000000000', '24000000000', '25000000000', '26000000000', '27000000000', '28000000000', '29000000000']],
}, total=False)

TiktokCreativeCenterTopContentResponse = ModelCreativecenterTopContentResponseDoc
TiktokCreativeCenterTopContentParams = TypedDict('TiktokCreativeCenterTopContentParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'include_comments': NotRequired[bool],
}, total=False)

TiktokCreativeCenterVideosResponse = ModelCreativecenterTrendingVideosResponseDoc
TiktokCreativeCenterVideosParams = TypedDict('TiktokCreativeCenterVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30']],
    'sort_by': NotRequired[Literal['views', 'engagement', 'six_second_views']],
    'content_label_id': NotRequired[str],
    'content_label_ids': NotRequired[list[Literal['11002', '11003', '11010', '11013', '11015']]],
    'organic_only': NotRequired[bool],
}, total=False)

TiktokExploreResponse = ModelTiktokExploreResponseDoc
TiktokExploreParams = TypedDict('TiktokExploreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[int],
}, total=False)

TiktokChallengeResponse = ModelTiktokChallengeResponseDoc
TiktokChallengeParams = TypedDict('TiktokChallengeParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'name': Required[str],
}, total=False)

TiktokChallengeListResponse = ModelTiktokChallengeListResponseDoc
TiktokChallengeListParams = TypedDict('TiktokChallengeListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileAnchorListResponse = ModelTiktokmobileAnchorListResponseDoc
TiktokMobileAnchorListParams = TypedDict('TiktokMobileAnchorListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileCollectionDetailResponse = ModelTiktokmobileCollectionDetailResponseDoc
TiktokMobileCollectionDetailParams = TypedDict('TiktokMobileCollectionDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'collection_id': Required[str],
}, total=False)

TiktokMobileCollectionListResponse = ModelTiktokmobileCollectionListResponseDoc
TiktokMobileCollectionListParams = TypedDict('TiktokMobileCollectionListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCollectionVideosResponse = ModelTiktokmobileCollectionVideosResponseDoc
TiktokMobileCollectionVideosParams = TypedDict('TiktokMobileCollectionVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'collection_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentRepliesResponse = ModelTiktokmobileCommentRepliesResponseDoc
TiktokMobileCommentRepliesParams = TypedDict('TiktokMobileCommentRepliesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'aweme_id': Required[str],
    'comment_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentsResponse = ModelTiktokmobileCommentsResponseDoc
TiktokMobileCommentsParams = TypedDict('TiktokMobileCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileFeedResponse = ModelTiktokmobileFeedResponseDoc
TiktokMobileFeedParams = TypedDict('TiktokMobileFeedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileFeedOfflineResponse = ModelTiktokmobileOfflineFeedResponseDoc
TiktokMobileFeedOfflineParams = TypedDict('TiktokMobileFeedOfflineParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'pull_type': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileFeedPostResponse = ModelTiktokmobileFeedPostResponseDoc
TiktokMobileFeedPostParams = TypedDict('TiktokMobileFeedPostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileHashtagResponse = ModelTiktokmobileHashtagInfoResponseDoc
TiktokMobileHashtagParams = TypedDict('TiktokMobileHashtagParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'name': Required[str],
}, total=False)

TiktokMobileHashtagPostsResponse = ModelTiktokmobileHashtagPostsResponseDoc
TiktokMobileHashtagPostsParams = TypedDict('TiktokMobileHashtagPostsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'name': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileHashtagsResponse = ModelTiktokmobileHashtagSearchResponseDoc
TiktokMobileHashtagsParams = TypedDict('TiktokMobileHashtagsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileLiveEffectsResponse = ModelTiktokmobileLiveEffectsResponseDoc
TiktokMobileLiveEffectsParams = TypedDict('TiktokMobileLiveEffectsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileLiveGiftsResponse = ModelTiktokmobileLiveGiftsResponseDoc
TiktokMobileLiveGiftsParams = TypedDict('TiktokMobileLiveGiftsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileLiveHashtagsResponse = ModelTiktokmobileLiveHashtagCatalogResponseDoc
TiktokMobileLiveHashtagsParams = TypedDict('TiktokMobileLiveHashtagsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileLiveRoomResponse = ModelTiktokmobileLiveRoomInfoResponseDoc
TiktokMobileLiveRoomParams = TypedDict('TiktokMobileLiveRoomParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'room_id': Required[str],
}, total=False)

TiktokMobileLiveRoomByUserResponse = ModelTiktokmobileLiveRoomInfoResponseDoc
TiktokMobileLiveRoomByUserParams = TypedDict('TiktokMobileLiveRoomByUserParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
}, total=False)

TiktokMobileLiveSearchResponse = ModelTiktokmobileLiveSearchResponseDoc
TiktokMobileLiveSearchParams = TypedDict('TiktokMobileLiveSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileLiveTabsResponse = ModelTiktokmobileLiveTabsResponseDoc
TiktokMobileLiveTabsParams = TypedDict('TiktokMobileLiveTabsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileMusicBeatsResponse = ModelTiktokmobileMusicBeatsSongsResponseDoc
TiktokMobileMusicBeatsParams = TypedDict('TiktokMobileMusicBeatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicChartResponse = ModelTiktokmobileMusicChartResponseDoc
TiktokMobileMusicChartParams = TypedDict('TiktokMobileMusicChartParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'chart_region': NotRequired[Literal['AE', 'BR', 'CA', 'DE', 'EG', 'FR', 'JP', 'KR', 'LB', 'MX', 'NG', 'SA', 'TR', 'US', 'ZA']],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicChoicesResponse = ModelTiktokmobileMusicChoicesResponseDoc
TiktokMobileMusicChoicesParams = TypedDict('TiktokMobileMusicChoicesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokMobileMusicCollectionListResponse = ModelTiktokmobileMusicCollectionListResponseDoc
TiktokMobileMusicCollectionListParams = TypedDict('TiktokMobileMusicCollectionListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicCollectionsResponse = ModelTiktokmobileMusicCollectionFeedResponseDoc
TiktokMobileMusicCollectionsParams = TypedDict('TiktokMobileMusicCollectionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicDetailResponse = ModelTiktokmobileMusicDetailResponseDoc
TiktokMobileMusicDetailParams = TypedDict('TiktokMobileMusicDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'music_id': Required[str],
}, total=False)

TiktokMobileMusicPickResponse = ModelTiktokmobileMusicPickResponseDoc
TiktokMobileMusicPickParams = TypedDict('TiktokMobileMusicPickParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicPostsResponse = ModelTiktokmobileMusicFreshAwemeResponseDoc
TiktokMobileMusicPostsParams = TypedDict('TiktokMobileMusicPostsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'music_id': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicRelatedResponse = ModelTiktokmobileMusicRelatedResponseDoc
TiktokMobileMusicRelatedParams = TypedDict('TiktokMobileMusicRelatedParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'aweme_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicTrendingResponse = ModelTiktokmobileHotMusicResponseDoc
TiktokMobileMusicTrendingParams = TypedDict('TiktokMobileMusicTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMvVideosResponse = ModelTiktokmobileMvFeedResponseDoc
TiktokMobileMvVideosParams = TypedDict('TiktokMobileMvVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'mv_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaceDetailResponse = ModelTiktokmobilePlaceDetailResponseDoc
TiktokMobilePlaceDetailParams = TypedDict('TiktokMobilePlaceDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'poi_id': Required[str],
    'review_count': NotRequired[int],
    'review_cursor': NotRequired[int],
    'merged_count': NotRequired[int],
    'video_cursor': NotRequired[int],
    'enter_from': NotRequired[str],
}, total=False)

TiktokMobilePlaceInfoResponse = ModelTiktokmobilePlaceInfoResponseDoc
TiktokMobilePlaceInfoParams = TypedDict('TiktokMobilePlaceInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlaceMediaResponse = ModelTiktokmobilePlaceMediaResponseDoc
TiktokMobilePlaceMediaParams = TypedDict('TiktokMobilePlaceMediaParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'poi_id': Required[str],
    'cursor': NotRequired[str],
    'size': NotRequired[int],
    'data_version': NotRequired[str],
}, total=False)

TiktokMobilePlacePhotosResponse = ModelTiktokmobilePlacePhotosResponseDoc
TiktokMobilePlacePhotosParams = TypedDict('TiktokMobilePlacePhotosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlaceReviewsResponse = ModelTiktokmobilePlaceReviewsResponseDoc
TiktokMobilePlaceReviewsParams = TypedDict('TiktokMobilePlaceReviewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'poi_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
    'sort_type': NotRequired[Literal['1', '2']],
}, total=False)

TiktokMobilePlaceVideosResponse = ModelTiktokmobilePlaceVideosResponseDoc
TiktokMobilePlaceVideosParams = TypedDict('TiktokMobilePlaceVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'poi_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaylistDetailResponse = ModelTiktokmobilePlaylistDetailResponseDoc
TiktokMobilePlaylistDetailParams = TypedDict('TiktokMobilePlaylistDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'mix_id': Required[str],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobilePlaylistListResponse = ModelTiktokmobilePlaylistListResponseDoc
TiktokMobilePlaylistListParams = TypedDict('TiktokMobilePlaylistListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaylistVideosResponse = ModelTiktokmobilePlaylistVideosResponseDoc
TiktokMobilePlaylistVideosParams = TypedDict('TiktokMobilePlaylistVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'mix_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchResponse = ModelTiktokmobileSearchGeneralResponseDoc
TiktokMobileSearchParams = TypedDict('TiktokMobileSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchEffectsResponse = ModelTiktokmobileSearchEffectsResponseDoc
TiktokMobileSearchEffectsParams = TypedDict('TiktokMobileSearchEffectsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchHashtagsResponse = ModelTiktokmobileHashtagSuggestionsResponseDoc
TiktokMobileSearchHashtagsParams = TypedDict('TiktokMobileSearchHashtagsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchMusicResponse = ModelTiktokmobileSearchMusicResponseDoc
TiktokMobileSearchMusicParams = TypedDict('TiktokMobileSearchMusicParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

TiktokMobileSearchPhotosResponse = ModelTiktokmobileSearchPhotosResponseDoc
TiktokMobileSearchPhotosParams = TypedDict('TiktokMobileSearchPhotosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[int],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
}, total=False)

TiktokMobileSearchPlaceResponse = ModelTiktokmobileSearchPlaceResponseDoc
TiktokMobileSearchPlaceParams = TypedDict('TiktokMobileSearchPlaceParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchPreInfoResponse = ModelTiktokmobileSearchPreInfoResponseDoc
TiktokMobileSearchPreInfoParams = TypedDict('TiktokMobileSearchPreInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': NotRequired[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchStreamResponse = ModelTiktokmobileSearchStreamResponseDoc
TiktokMobileSearchStreamParams = TypedDict('TiktokMobileSearchStreamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_source': NotRequired[str],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'filter_selected': NotRequired[str],
}, total=False)

TiktokMobileSearchSugResponse = ModelTiktokmobileSearchSuggestionResponseDoc
TiktokMobileSearchSugParams = TypedDict('TiktokMobileSearchSugParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchTabsResponse = ModelTiktokmobileSearchTabsResponseDoc
TiktokMobileSearchTabsParams = TypedDict('TiktokMobileSearchTabsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
}, total=False)

TiktokMobileSearchUserResponse = ModelTiktokmobileSearchUsersResponseDoc
TiktokMobileSearchUserParams = TypedDict('TiktokMobileSearchUserParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileSearchVideosResponse = ModelTiktokmobileSearchVideosResponseDoc
TiktokMobileSearchVideosParams = TypedDict('TiktokMobileSearchVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileTranslationDescriptionResponse = ModelTiktokmobileTranslationDescriptionResponseDoc
TiktokMobileTranslationDescriptionParams = TypedDict('TiktokMobileTranslationDescriptionParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'item_id': Required[str],
    'target_lang': NotRequired[str],
}, total=False)

TiktokMobileTrendingCategoriesResponse = ModelTiktokmobileCategoryListResponseDoc
TiktokMobileTrendingCategoriesParams = TypedDict('TiktokMobileTrendingCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileTrendingEffectsResponse = ModelTiktokmobileStickerDiscoverResponseDoc
TiktokMobileTrendingEffectsParams = TypedDict('TiktokMobileTrendingEffectsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowersResponse = ModelTiktokmobileUserFollowersResponseDoc
TiktokMobileUserFollowersParams = TypedDict('TiktokMobileUserFollowersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowingResponse = ModelTiktokmobileUserFollowingResponseDoc
TiktokMobileUserFollowingParams = TypedDict('TiktokMobileUserFollowingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalEffectsResponse = ModelTiktokmobileUserOriginalEffectsResponseDoc
TiktokMobileUserOriginalEffectsParams = TypedDict('TiktokMobileUserOriginalEffectsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalMusicResponse = ModelTiktokmobileUserOriginalMusicResponseDoc
TiktokMobileUserOriginalMusicParams = TypedDict('TiktokMobileUserOriginalMusicParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserPostsResponse = ModelTiktokmobileUserPostsResponseDoc
TiktokMobileUserPostsParams = TypedDict('TiktokMobileUserPostsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[int],
}, total=False)

TiktokMobileUserProfileResponse = ModelTiktokmobileUserProfileResponseDoc
TiktokMobileUserProfileParams = TypedDict('TiktokMobileUserProfileParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobileUserRecommendationsResponse = ModelTiktokmobileUserRecommendationsResponseDoc
TiktokMobileUserRecommendationsParams = TypedDict('TiktokMobileUserRecommendationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileVideoDetailResponse = ModelTiktokmobileVideoDetailResponseDoc
TiktokMobileVideoDetailParams = TypedDict('TiktokMobileVideoDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'aweme_id': Required[str],
}, total=False)

TiktokMobileVideoSubtitlesResponse = ModelTiktokmobileVideoSubtitlesResponseDoc
TiktokMobileVideoSubtitlesParams = TypedDict('TiktokMobileVideoSubtitlesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'video_id': Required[str],
    'language': Required[str],
}, total=False)

TiktokPopularTrendCountryIndustryMetaResponse = ModelPopulartrendCountryIndustryMetaResponseDoc
TiktokPopularTrendCountryIndustryMetaParams = TypedDict('TiktokPopularTrendCountryIndustryMetaParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokPostResponse = ModelTiktokPostResponseDoc
TiktokPostParams = TypedDict('TiktokPostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

TiktokProfilePostResponse = ModelTiktokProfilePostResponseDoc
TiktokProfilePostParams = TypedDict('TiktokProfilePostParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'secUid': Required[str],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '2']],
}, total=False)

TiktokProfileResponse = ModelTiktokProfileResponseDoc
TiktokProfileParams = TypedDict('TiktokProfileParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'handler': Required[str],
}, total=False)

TiktokSearchResponse = ModelTiktokSearchResponseDoc
TiktokSearchParams = TypedDict('TiktokSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokSearchHashtagResponse = ModelTiktokSearchHashtagResponseDoc
TiktokSearchHashtagParams = TypedDict('TiktokSearchHashtagParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokSearchUserResponse = ModelTiktokSearchUserResponseDoc
TiktokSearchUserParams = TypedDict('TiktokSearchUserParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokTopAdsAnalysisResponse = ModelPopulartrendTopAdsAnalysisResponseDoc
TiktokTopAdsAnalysisParams = TypedDict('TiktokTopAdsAnalysisParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'material_id': Required[str],
    'metric': NotRequired[Literal['retain_ctr', 'retain_cvr', 'click_cnt', 'convert_cnt', 'play_retain_cnt']],
    'period_type': NotRequired[Literal['7', '30', '180']],
}, total=False)

TiktokTopAdsDetailResponse = ModelPopulartrendTopAdsDetailResponseDoc
TiktokTopAdsDetailParams = TypedDict('TiktokTopAdsDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'material_id': Required[str],
}, total=False)

TiktokTopAdsFiltersResponse = ModelPopulartrendTopAdsFiltersResponseDoc
TiktokTopAdsFiltersParams = TypedDict('TiktokTopAdsFiltersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokTopAdsListResponse = ModelPopulartrendTopAdsListResponseDoc
TiktokTopAdsListParams = TypedDict('TiktokTopAdsListParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'period': NotRequired[Literal['7', '30', '180']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'order_by': NotRequired[Literal['for_you', 'impression', 'ctr', 'play_2s_rate', 'play_6s_rate', 'cvr', 'like']],
    'country_code': NotRequired[str],
    'keyword': NotRequired[str],
    'industry': NotRequired[str],
    'objective': NotRequired[str],
    'ad_language': NotRequired[str],
    'pattern_label': NotRequired[str],
    'duration': NotRequired[Literal['time-2', 'time-3', 'time-4', 'time-5', 'time-6', 'time-7']],
    'like': NotRequired[Literal['1', '2', '3', '4', '5']],
    'ad_format': NotRequired[Literal['1', '2']],
}, total=False)

TiktokTopAdsLocationInfoResponse = ModelPopulartrendTopAdsLocationInfoResponseDoc
TiktokTopAdsLocationInfoParams = TypedDict('TiktokTopAdsLocationInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'module': NotRequired[int],
}, total=False)

TiktokTopAdsLocationsResponse = ModelPopulartrendTopAdsLocationsResponseDoc
TiktokTopAdsLocationsParams = TypedDict('TiktokTopAdsLocationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokTopAdsRecommendResponse = ModelPopulartrendTopAdsRecommendResponseDoc
TiktokTopAdsRecommendParams = TypedDict('TiktokTopAdsRecommendParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'material_id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

TiktokTopAdsSafetyResponse = ModelPopulartrendTopAdsSafetyResponseDoc
TiktokTopAdsSafetyParams = TypedDict('TiktokTopAdsSafetyParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

TiktokTopAdsSpotlightResponse = ModelPopulartrendTopAdsSpotlightResponseDoc
TiktokTopAdsSpotlightParams = TypedDict('TiktokTopAdsSpotlightParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

TiktokTopAdsSuggestionsResponse = ModelPopulartrendTopAdsSuggestionsResponseDoc
TiktokTopAdsSuggestionsParams = TypedDict('TiktokTopAdsSuggestionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'count': NotRequired[int],
    'scenario': NotRequired[int],
}, total=False)

TiktokTrendingResponse = ModelTiktokTrendingResponseDoc
TiktokTrendingParams = TypedDict('TiktokTrendingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

class TiktokGroup:
    @overload
    def category(self, **params: Unpack[TiktokCategoryStreamParams]) -> BinaryIO: ...
    @overload
    def category(self, **params: Unpack[TiktokCategoryTextResponseParams]) -> str: ...
    @overload
    def category(self, **params: Unpack[TiktokCategoryDefaultParams]) -> TiktokCategoryResponse: ...
    @overload
    def video_comments(self, **params: Unpack[TiktokVideoCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def video_comments(self, **params: Unpack[TiktokVideoCommentsTextResponseParams]) -> str: ...
    @overload
    def video_comments(self, **params: Unpack[TiktokVideoCommentsDefaultParams]) -> TiktokVideoCommentsResponse: ...
    @overload
    def creative_center_filters(self, **params: Unpack[TiktokCreativeCenterFiltersStreamParams]) -> BinaryIO: ...
    @overload
    def creative_center_filters(self, **params: Unpack[TiktokCreativeCenterFiltersTextResponseParams]) -> str: ...
    @overload
    def creative_center_filters(self, **params: Unpack[TiktokCreativeCenterFiltersDefaultParams]) -> TiktokCreativeCenterFiltersResponse: ...
    @overload
    def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsTextResponseParams]) -> str: ...
    @overload
    def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsDefaultParams]) -> TiktokCreativeCenterHashtagsResponse: ...
    @overload
    def creative_center_top_content(self, **params: Unpack[TiktokCreativeCenterTopContentStreamParams]) -> BinaryIO: ...
    @overload
    def creative_center_top_content(self, **params: Unpack[TiktokCreativeCenterTopContentTextResponseParams]) -> str: ...
    @overload
    def creative_center_top_content(self, **params: Unpack[TiktokCreativeCenterTopContentDefaultParams]) -> TiktokCreativeCenterTopContentResponse: ...
    @overload
    def creative_center_videos(self, **params: Unpack[TiktokCreativeCenterVideosStreamParams]) -> BinaryIO: ...
    @overload
    def creative_center_videos(self, **params: Unpack[TiktokCreativeCenterVideosTextResponseParams]) -> str: ...
    @overload
    def creative_center_videos(self, **params: Unpack[TiktokCreativeCenterVideosDefaultParams]) -> TiktokCreativeCenterVideosResponse: ...
    @overload
    def explore(self, **params: Unpack[TiktokExploreStreamParams]) -> BinaryIO: ...
    @overload
    def explore(self, **params: Unpack[TiktokExploreTextResponseParams]) -> str: ...
    @overload
    def explore(self, **params: Unpack[TiktokExploreDefaultParams]) -> TiktokExploreResponse: ...
    @overload
    def challenge(self, **params: Unpack[TiktokChallengeStreamParams]) -> BinaryIO: ...
    @overload
    def challenge(self, **params: Unpack[TiktokChallengeTextResponseParams]) -> str: ...
    @overload
    def challenge(self, **params: Unpack[TiktokChallengeDefaultParams]) -> TiktokChallengeResponse: ...
    @overload
    def challenge_list(self, **params: Unpack[TiktokChallengeListStreamParams]) -> BinaryIO: ...
    @overload
    def challenge_list(self, **params: Unpack[TiktokChallengeListTextResponseParams]) -> str: ...
    @overload
    def challenge_list(self, **params: Unpack[TiktokChallengeListDefaultParams]) -> TiktokChallengeListResponse: ...
    @overload
    def mobile_anchor_list(self, **params: Unpack[TiktokMobileAnchorListStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_anchor_list(self, **params: Unpack[TiktokMobileAnchorListTextResponseParams]) -> str: ...
    @overload
    def mobile_anchor_list(self, **params: Unpack[TiktokMobileAnchorListDefaultParams]) -> TiktokMobileAnchorListResponse: ...
    @overload
    def mobile_collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailTextResponseParams]) -> str: ...
    @overload
    def mobile_collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailDefaultParams]) -> TiktokMobileCollectionDetailResponse: ...
    @overload
    def mobile_collection_list(self, **params: Unpack[TiktokMobileCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_collection_list(self, **params: Unpack[TiktokMobileCollectionListTextResponseParams]) -> str: ...
    @overload
    def mobile_collection_list(self, **params: Unpack[TiktokMobileCollectionListDefaultParams]) -> TiktokMobileCollectionListResponse: ...
    @overload
    def mobile_collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosTextResponseParams]) -> str: ...
    @overload
    def mobile_collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosDefaultParams]) -> TiktokMobileCollectionVideosResponse: ...
    @overload
    def mobile_comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesTextResponseParams]) -> str: ...
    @overload
    def mobile_comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesDefaultParams]) -> TiktokMobileCommentRepliesResponse: ...
    @overload
    def mobile_comments(self, **params: Unpack[TiktokMobileCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_comments(self, **params: Unpack[TiktokMobileCommentsTextResponseParams]) -> str: ...
    @overload
    def mobile_comments(self, **params: Unpack[TiktokMobileCommentsDefaultParams]) -> TiktokMobileCommentsResponse: ...
    @overload
    def mobile_feed(self, **params: Unpack[TiktokMobileFeedStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_feed(self, **params: Unpack[TiktokMobileFeedTextResponseParams]) -> str: ...
    @overload
    def mobile_feed(self, **params: Unpack[TiktokMobileFeedDefaultParams]) -> TiktokMobileFeedResponse: ...
    @overload
    def mobile_feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineTextResponseParams]) -> str: ...
    @overload
    def mobile_feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineDefaultParams]) -> TiktokMobileFeedOfflineResponse: ...
    @overload
    def mobile_feed_post(self, **params: Unpack[TiktokMobileFeedPostStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_feed_post(self, **params: Unpack[TiktokMobileFeedPostTextResponseParams]) -> str: ...
    @overload
    def mobile_feed_post(self, **params: Unpack[TiktokMobileFeedPostDefaultParams]) -> TiktokMobileFeedPostResponse: ...
    @overload
    def mobile_hashtag(self, **params: Unpack[TiktokMobileHashtagStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_hashtag(self, **params: Unpack[TiktokMobileHashtagTextResponseParams]) -> str: ...
    @overload
    def mobile_hashtag(self, **params: Unpack[TiktokMobileHashtagDefaultParams]) -> TiktokMobileHashtagResponse: ...
    @overload
    def mobile_hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsTextResponseParams]) -> str: ...
    @overload
    def mobile_hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsDefaultParams]) -> TiktokMobileHashtagPostsResponse: ...
    @overload
    def mobile_hashtags(self, **params: Unpack[TiktokMobileHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_hashtags(self, **params: Unpack[TiktokMobileHashtagsTextResponseParams]) -> str: ...
    @overload
    def mobile_hashtags(self, **params: Unpack[TiktokMobileHashtagsDefaultParams]) -> TiktokMobileHashtagsResponse: ...
    @overload
    def mobile_live_effects(self, **params: Unpack[TiktokMobileLiveEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_effects(self, **params: Unpack[TiktokMobileLiveEffectsTextResponseParams]) -> str: ...
    @overload
    def mobile_live_effects(self, **params: Unpack[TiktokMobileLiveEffectsDefaultParams]) -> TiktokMobileLiveEffectsResponse: ...
    @overload
    def mobile_live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsTextResponseParams]) -> str: ...
    @overload
    def mobile_live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsDefaultParams]) -> TiktokMobileLiveGiftsResponse: ...
    @overload
    def mobile_live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsTextResponseParams]) -> str: ...
    @overload
    def mobile_live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsDefaultParams]) -> TiktokMobileLiveHashtagsResponse: ...
    @overload
    def mobile_live_room(self, **params: Unpack[TiktokMobileLiveRoomStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_room(self, **params: Unpack[TiktokMobileLiveRoomTextResponseParams]) -> str: ...
    @overload
    def mobile_live_room(self, **params: Unpack[TiktokMobileLiveRoomDefaultParams]) -> TiktokMobileLiveRoomResponse: ...
    @overload
    def mobile_live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserTextResponseParams]) -> str: ...
    @overload
    def mobile_live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserDefaultParams]) -> TiktokMobileLiveRoomByUserResponse: ...
    @overload
    def mobile_live_search(self, **params: Unpack[TiktokMobileLiveSearchStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_search(self, **params: Unpack[TiktokMobileLiveSearchTextResponseParams]) -> str: ...
    @overload
    def mobile_live_search(self, **params: Unpack[TiktokMobileLiveSearchDefaultParams]) -> TiktokMobileLiveSearchResponse: ...
    @overload
    def mobile_live_tabs(self, **params: Unpack[TiktokMobileLiveTabsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_tabs(self, **params: Unpack[TiktokMobileLiveTabsTextResponseParams]) -> str: ...
    @overload
    def mobile_live_tabs(self, **params: Unpack[TiktokMobileLiveTabsDefaultParams]) -> TiktokMobileLiveTabsResponse: ...
    @overload
    def mobile_music_beats(self, **params: Unpack[TiktokMobileMusicBeatsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_beats(self, **params: Unpack[TiktokMobileMusicBeatsTextResponseParams]) -> str: ...
    @overload
    def mobile_music_beats(self, **params: Unpack[TiktokMobileMusicBeatsDefaultParams]) -> TiktokMobileMusicBeatsResponse: ...
    @overload
    def mobile_music_chart(self, **params: Unpack[TiktokMobileMusicChartStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_chart(self, **params: Unpack[TiktokMobileMusicChartTextResponseParams]) -> str: ...
    @overload
    def mobile_music_chart(self, **params: Unpack[TiktokMobileMusicChartDefaultParams]) -> TiktokMobileMusicChartResponse: ...
    @overload
    def mobile_music_choices(self, **params: Unpack[TiktokMobileMusicChoicesStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_choices(self, **params: Unpack[TiktokMobileMusicChoicesTextResponseParams]) -> str: ...
    @overload
    def mobile_music_choices(self, **params: Unpack[TiktokMobileMusicChoicesDefaultParams]) -> TiktokMobileMusicChoicesResponse: ...
    @overload
    def mobile_music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListTextResponseParams]) -> str: ...
    @overload
    def mobile_music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListDefaultParams]) -> TiktokMobileMusicCollectionListResponse: ...
    @overload
    def mobile_music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsTextResponseParams]) -> str: ...
    @overload
    def mobile_music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsDefaultParams]) -> TiktokMobileMusicCollectionsResponse: ...
    @overload
    def mobile_music_detail(self, **params: Unpack[TiktokMobileMusicDetailStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_detail(self, **params: Unpack[TiktokMobileMusicDetailTextResponseParams]) -> str: ...
    @overload
    def mobile_music_detail(self, **params: Unpack[TiktokMobileMusicDetailDefaultParams]) -> TiktokMobileMusicDetailResponse: ...
    @overload
    def mobile_music_pick(self, **params: Unpack[TiktokMobileMusicPickStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_pick(self, **params: Unpack[TiktokMobileMusicPickTextResponseParams]) -> str: ...
    @overload
    def mobile_music_pick(self, **params: Unpack[TiktokMobileMusicPickDefaultParams]) -> TiktokMobileMusicPickResponse: ...
    @overload
    def mobile_music_posts(self, **params: Unpack[TiktokMobileMusicPostsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_posts(self, **params: Unpack[TiktokMobileMusicPostsTextResponseParams]) -> str: ...
    @overload
    def mobile_music_posts(self, **params: Unpack[TiktokMobileMusicPostsDefaultParams]) -> TiktokMobileMusicPostsResponse: ...
    @overload
    def mobile_music_related(self, **params: Unpack[TiktokMobileMusicRelatedStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_related(self, **params: Unpack[TiktokMobileMusicRelatedTextResponseParams]) -> str: ...
    @overload
    def mobile_music_related(self, **params: Unpack[TiktokMobileMusicRelatedDefaultParams]) -> TiktokMobileMusicRelatedResponse: ...
    @overload
    def mobile_music_trending(self, **params: Unpack[TiktokMobileMusicTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_trending(self, **params: Unpack[TiktokMobileMusicTrendingTextResponseParams]) -> str: ...
    @overload
    def mobile_music_trending(self, **params: Unpack[TiktokMobileMusicTrendingDefaultParams]) -> TiktokMobileMusicTrendingResponse: ...
    @overload
    def mobile_mv_videos(self, **params: Unpack[TiktokMobileMvVideosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_mv_videos(self, **params: Unpack[TiktokMobileMvVideosTextResponseParams]) -> str: ...
    @overload
    def mobile_mv_videos(self, **params: Unpack[TiktokMobileMvVideosDefaultParams]) -> TiktokMobileMvVideosResponse: ...
    @overload
    def mobile_place_detail(self, **params: Unpack[TiktokMobilePlaceDetailStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_place_detail(self, **params: Unpack[TiktokMobilePlaceDetailTextResponseParams]) -> str: ...
    @overload
    def mobile_place_detail(self, **params: Unpack[TiktokMobilePlaceDetailDefaultParams]) -> TiktokMobilePlaceDetailResponse: ...
    @overload
    def mobile_place_info(self, **params: Unpack[TiktokMobilePlaceInfoStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_place_info(self, **params: Unpack[TiktokMobilePlaceInfoTextResponseParams]) -> str: ...
    @overload
    def mobile_place_info(self, **params: Unpack[TiktokMobilePlaceInfoDefaultParams]) -> TiktokMobilePlaceInfoResponse: ...
    @overload
    def mobile_place_media(self, **params: Unpack[TiktokMobilePlaceMediaStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_place_media(self, **params: Unpack[TiktokMobilePlaceMediaTextResponseParams]) -> str: ...
    @overload
    def mobile_place_media(self, **params: Unpack[TiktokMobilePlaceMediaDefaultParams]) -> TiktokMobilePlaceMediaResponse: ...
    @overload
    def mobile_place_photos(self, **params: Unpack[TiktokMobilePlacePhotosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_place_photos(self, **params: Unpack[TiktokMobilePlacePhotosTextResponseParams]) -> str: ...
    @overload
    def mobile_place_photos(self, **params: Unpack[TiktokMobilePlacePhotosDefaultParams]) -> TiktokMobilePlacePhotosResponse: ...
    @overload
    def mobile_place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsTextResponseParams]) -> str: ...
    @overload
    def mobile_place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsDefaultParams]) -> TiktokMobilePlaceReviewsResponse: ...
    @overload
    def mobile_place_videos(self, **params: Unpack[TiktokMobilePlaceVideosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_place_videos(self, **params: Unpack[TiktokMobilePlaceVideosTextResponseParams]) -> str: ...
    @overload
    def mobile_place_videos(self, **params: Unpack[TiktokMobilePlaceVideosDefaultParams]) -> TiktokMobilePlaceVideosResponse: ...
    @overload
    def mobile_playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailTextResponseParams]) -> str: ...
    @overload
    def mobile_playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailDefaultParams]) -> TiktokMobilePlaylistDetailResponse: ...
    @overload
    def mobile_playlist_list(self, **params: Unpack[TiktokMobilePlaylistListStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_playlist_list(self, **params: Unpack[TiktokMobilePlaylistListTextResponseParams]) -> str: ...
    @overload
    def mobile_playlist_list(self, **params: Unpack[TiktokMobilePlaylistListDefaultParams]) -> TiktokMobilePlaylistListResponse: ...
    @overload
    def mobile_playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosTextResponseParams]) -> str: ...
    @overload
    def mobile_playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosDefaultParams]) -> TiktokMobilePlaylistVideosResponse: ...
    @overload
    def mobile_search(self, **params: Unpack[TiktokMobileSearchResponseStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search(self, **params: Unpack[TiktokMobileSearchTextResponseParams]) -> str: ...
    @overload
    def mobile_search(self, **params: Unpack[TiktokMobileSearchDefaultParams]) -> TiktokMobileSearchResponse: ...
    @overload
    def mobile_search_effects(self, **params: Unpack[TiktokMobileSearchEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_effects(self, **params: Unpack[TiktokMobileSearchEffectsTextResponseParams]) -> str: ...
    @overload
    def mobile_search_effects(self, **params: Unpack[TiktokMobileSearchEffectsDefaultParams]) -> TiktokMobileSearchEffectsResponse: ...
    @overload
    def mobile_search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsTextResponseParams]) -> str: ...
    @overload
    def mobile_search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsDefaultParams]) -> TiktokMobileSearchHashtagsResponse: ...
    @overload
    def mobile_search_music(self, **params: Unpack[TiktokMobileSearchMusicStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_music(self, **params: Unpack[TiktokMobileSearchMusicTextResponseParams]) -> str: ...
    @overload
    def mobile_search_music(self, **params: Unpack[TiktokMobileSearchMusicDefaultParams]) -> TiktokMobileSearchMusicResponse: ...
    @overload
    def mobile_search_photos(self, **params: Unpack[TiktokMobileSearchPhotosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_photos(self, **params: Unpack[TiktokMobileSearchPhotosTextResponseParams]) -> str: ...
    @overload
    def mobile_search_photos(self, **params: Unpack[TiktokMobileSearchPhotosDefaultParams]) -> TiktokMobileSearchPhotosResponse: ...
    @overload
    def mobile_search_place(self, **params: Unpack[TiktokMobileSearchPlaceStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_place(self, **params: Unpack[TiktokMobileSearchPlaceTextResponseParams]) -> str: ...
    @overload
    def mobile_search_place(self, **params: Unpack[TiktokMobileSearchPlaceDefaultParams]) -> TiktokMobileSearchPlaceResponse: ...
    @overload
    def mobile_search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoTextResponseParams]) -> str: ...
    @overload
    def mobile_search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoDefaultParams]) -> TiktokMobileSearchPreInfoResponse: ...
    @overload
    def mobile_search_stream(self, **params: Unpack[TiktokMobileSearchStreamStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_stream(self, **params: Unpack[TiktokMobileSearchStreamTextResponseParams]) -> str: ...
    @overload
    def mobile_search_stream(self, **params: Unpack[TiktokMobileSearchStreamDefaultParams]) -> TiktokMobileSearchStreamResponse: ...
    @overload
    def mobile_search_sug(self, **params: Unpack[TiktokMobileSearchSugStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_sug(self, **params: Unpack[TiktokMobileSearchSugTextResponseParams]) -> str: ...
    @overload
    def mobile_search_sug(self, **params: Unpack[TiktokMobileSearchSugDefaultParams]) -> TiktokMobileSearchSugResponse: ...
    @overload
    def mobile_search_tabs(self, **params: Unpack[TiktokMobileSearchTabsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_tabs(self, **params: Unpack[TiktokMobileSearchTabsTextResponseParams]) -> str: ...
    @overload
    def mobile_search_tabs(self, **params: Unpack[TiktokMobileSearchTabsDefaultParams]) -> TiktokMobileSearchTabsResponse: ...
    @overload
    def mobile_search_user(self, **params: Unpack[TiktokMobileSearchUserStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_user(self, **params: Unpack[TiktokMobileSearchUserTextResponseParams]) -> str: ...
    @overload
    def mobile_search_user(self, **params: Unpack[TiktokMobileSearchUserDefaultParams]) -> TiktokMobileSearchUserResponse: ...
    @overload
    def mobile_search_videos(self, **params: Unpack[TiktokMobileSearchVideosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_videos(self, **params: Unpack[TiktokMobileSearchVideosTextResponseParams]) -> str: ...
    @overload
    def mobile_search_videos(self, **params: Unpack[TiktokMobileSearchVideosDefaultParams]) -> TiktokMobileSearchVideosResponse: ...
    @overload
    def mobile_translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionTextResponseParams]) -> str: ...
    @overload
    def mobile_translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionDefaultParams]) -> TiktokMobileTranslationDescriptionResponse: ...
    @overload
    def mobile_trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesTextResponseParams]) -> str: ...
    @overload
    def mobile_trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesDefaultParams]) -> TiktokMobileTrendingCategoriesResponse: ...
    @overload
    def mobile_trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsTextResponseParams]) -> str: ...
    @overload
    def mobile_trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsDefaultParams]) -> TiktokMobileTrendingEffectsResponse: ...
    @overload
    def mobile_user_followers(self, **params: Unpack[TiktokMobileUserFollowersStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_followers(self, **params: Unpack[TiktokMobileUserFollowersTextResponseParams]) -> str: ...
    @overload
    def mobile_user_followers(self, **params: Unpack[TiktokMobileUserFollowersDefaultParams]) -> TiktokMobileUserFollowersResponse: ...
    @overload
    def mobile_user_following(self, **params: Unpack[TiktokMobileUserFollowingStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_following(self, **params: Unpack[TiktokMobileUserFollowingTextResponseParams]) -> str: ...
    @overload
    def mobile_user_following(self, **params: Unpack[TiktokMobileUserFollowingDefaultParams]) -> TiktokMobileUserFollowingResponse: ...
    @overload
    def mobile_user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsTextResponseParams]) -> str: ...
    @overload
    def mobile_user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsDefaultParams]) -> TiktokMobileUserOriginalEffectsResponse: ...
    @overload
    def mobile_user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicTextResponseParams]) -> str: ...
    @overload
    def mobile_user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicDefaultParams]) -> TiktokMobileUserOriginalMusicResponse: ...
    @overload
    def mobile_user_posts(self, **params: Unpack[TiktokMobileUserPostsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_posts(self, **params: Unpack[TiktokMobileUserPostsTextResponseParams]) -> str: ...
    @overload
    def mobile_user_posts(self, **params: Unpack[TiktokMobileUserPostsDefaultParams]) -> TiktokMobileUserPostsResponse: ...
    @overload
    def mobile_user_profile(self, **params: Unpack[TiktokMobileUserProfileStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_profile(self, **params: Unpack[TiktokMobileUserProfileTextResponseParams]) -> str: ...
    @overload
    def mobile_user_profile(self, **params: Unpack[TiktokMobileUserProfileDefaultParams]) -> TiktokMobileUserProfileResponse: ...
    @overload
    def mobile_user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsTextResponseParams]) -> str: ...
    @overload
    def mobile_user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsDefaultParams]) -> TiktokMobileUserRecommendationsResponse: ...
    @overload
    def mobile_video_detail(self, **params: Unpack[TiktokMobileVideoDetailStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_video_detail(self, **params: Unpack[TiktokMobileVideoDetailTextResponseParams]) -> str: ...
    @overload
    def mobile_video_detail(self, **params: Unpack[TiktokMobileVideoDetailDefaultParams]) -> TiktokMobileVideoDetailResponse: ...
    @overload
    def mobile_video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesTextResponseParams]) -> str: ...
    @overload
    def mobile_video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesDefaultParams]) -> TiktokMobileVideoSubtitlesResponse: ...
    @overload
    def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaStreamParams]) -> BinaryIO: ...
    @overload
    def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaTextResponseParams]) -> str: ...
    @overload
    def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaDefaultParams]) -> TiktokPopularTrendCountryIndustryMetaResponse: ...
    @overload
    def post(self, **params: Unpack[TiktokPostStreamParams]) -> BinaryIO: ...
    @overload
    def post(self, **params: Unpack[TiktokPostTextResponseParams]) -> str: ...
    @overload
    def post(self, **params: Unpack[TiktokPostDefaultParams]) -> TiktokPostResponse: ...
    @overload
    def profile_post(self, **params: Unpack[TiktokProfilePostStreamParams]) -> BinaryIO: ...
    @overload
    def profile_post(self, **params: Unpack[TiktokProfilePostTextResponseParams]) -> str: ...
    @overload
    def profile_post(self, **params: Unpack[TiktokProfilePostDefaultParams]) -> TiktokProfilePostResponse: ...
    @overload
    def profile(self, **params: Unpack[TiktokProfileStreamParams]) -> BinaryIO: ...
    @overload
    def profile(self, **params: Unpack[TiktokProfileTextResponseParams]) -> str: ...
    @overload
    def profile(self, **params: Unpack[TiktokProfileDefaultParams]) -> TiktokProfileResponse: ...
    @overload
    def search(self, **params: Unpack[TiktokSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[TiktokSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[TiktokSearchDefaultParams]) -> TiktokSearchResponse: ...
    @overload
    def search_hashtag(self, **params: Unpack[TiktokSearchHashtagStreamParams]) -> BinaryIO: ...
    @overload
    def search_hashtag(self, **params: Unpack[TiktokSearchHashtagTextResponseParams]) -> str: ...
    @overload
    def search_hashtag(self, **params: Unpack[TiktokSearchHashtagDefaultParams]) -> TiktokSearchHashtagResponse: ...
    @overload
    def search_user(self, **params: Unpack[TiktokSearchUserStreamParams]) -> BinaryIO: ...
    @overload
    def search_user(self, **params: Unpack[TiktokSearchUserTextResponseParams]) -> str: ...
    @overload
    def search_user(self, **params: Unpack[TiktokSearchUserDefaultParams]) -> TiktokSearchUserResponse: ...
    @overload
    def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisTextResponseParams]) -> str: ...
    @overload
    def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisDefaultParams]) -> TiktokTopAdsAnalysisResponse: ...
    @overload
    def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailTextResponseParams]) -> str: ...
    @overload
    def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailDefaultParams]) -> TiktokTopAdsDetailResponse: ...
    @overload
    def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersTextResponseParams]) -> str: ...
    @overload
    def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersDefaultParams]) -> TiktokTopAdsFiltersResponse: ...
    @overload
    def top_ads_list(self, **params: Unpack[TiktokTopAdsListStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_list(self, **params: Unpack[TiktokTopAdsListTextResponseParams]) -> str: ...
    @overload
    def top_ads_list(self, **params: Unpack[TiktokTopAdsListDefaultParams]) -> TiktokTopAdsListResponse: ...
    @overload
    def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoTextResponseParams]) -> str: ...
    @overload
    def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoDefaultParams]) -> TiktokTopAdsLocationInfoResponse: ...
    @overload
    def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsTextResponseParams]) -> str: ...
    @overload
    def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsDefaultParams]) -> TiktokTopAdsLocationsResponse: ...
    @overload
    def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendTextResponseParams]) -> str: ...
    @overload
    def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendDefaultParams]) -> TiktokTopAdsRecommendResponse: ...
    @overload
    def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyTextResponseParams]) -> str: ...
    @overload
    def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyDefaultParams]) -> TiktokTopAdsSafetyResponse: ...
    @overload
    def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightTextResponseParams]) -> str: ...
    @overload
    def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightDefaultParams]) -> TiktokTopAdsSpotlightResponse: ...
    @overload
    def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsTextResponseParams]) -> str: ...
    @overload
    def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsDefaultParams]) -> TiktokTopAdsSuggestionsResponse: ...
    @overload
    def trending(self, **params: Unpack[TiktokTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def trending(self, **params: Unpack[TiktokTrendingTextResponseParams]) -> str: ...
    @overload
    def trending(self, **params: Unpack[TiktokTrendingDefaultParams]) -> TiktokTrendingResponse: ...

OperationId = Literal[
    'tiktok-category',
    'tiktok-video-comments',
    'tiktok-creative-center-filters',
    'tiktok-creative-center-hashtags',
    'tiktok-creative-center-top-content',
    'tiktok-creative-center-videos',
    'tiktok-explore',
    'tiktok-challenge',
    'tiktok-challenge-list',
    'tiktok-mobile-anchor-list',
    'tiktok-mobile-collection-detail',
    'tiktok-mobile-collection-list',
    'tiktok-mobile-collection-videos',
    'tiktok-mobile-comment-replies',
    'tiktok-mobile-comments',
    'tiktok-mobile-feed',
    'tiktok-mobile-feed-offline',
    'tiktok-mobile-feed-post',
    'tiktok-mobile-hashtag',
    'tiktok-mobile-hashtag-posts',
    'tiktok-mobile-hashtags',
    'tiktok-mobile-live-effects',
    'tiktok-mobile-live-gifts',
    'tiktok-mobile-live-hashtags',
    'tiktok-mobile-live-room',
    'tiktok-mobile-live-room-by-user',
    'tiktok-mobile-live-search',
    'tiktok-mobile-live-tabs',
    'tiktok-mobile-music-beats',
    'tiktok-mobile-music-chart',
    'tiktok-mobile-music-choices',
    'tiktok-mobile-music-collection-list',
    'tiktok-mobile-music-collections',
    'tiktok-mobile-music-detail',
    'tiktok-mobile-music-pick',
    'tiktok-mobile-music-posts',
    'tiktok-mobile-music-related',
    'tiktok-mobile-music-trending',
    'tiktok-mobile-mv-videos',
    'tiktok-mobile-place-detail',
    'tiktok-mobile-place-info',
    'tiktok-mobile-place-media',
    'tiktok-mobile-place-photos',
    'tiktok-mobile-place-reviews',
    'tiktok-mobile-place-videos',
    'tiktok-mobile-playlist-detail',
    'tiktok-mobile-playlist-list',
    'tiktok-mobile-playlist-videos',
    'tiktok-mobile-search',
    'tiktok-mobile-search-effects',
    'tiktok-mobile-search-hashtags',
    'tiktok-mobile-search-music',
    'tiktok-mobile-search-photos',
    'tiktok-mobile-search-place',
    'tiktok-mobile-search-pre-info',
    'tiktok-mobile-search-stream',
    'tiktok-mobile-search-sug',
    'tiktok-mobile-search-tabs',
    'tiktok-mobile-search-user',
    'tiktok-mobile-search-videos',
    'tiktok-mobile-translation-description',
    'tiktok-mobile-trending-categories',
    'tiktok-mobile-trending-effects',
    'tiktok-mobile-user-followers',
    'tiktok-mobile-user-following',
    'tiktok-mobile-user-original-effects',
    'tiktok-mobile-user-original-music',
    'tiktok-mobile-user-posts',
    'tiktok-mobile-user-profile',
    'tiktok-mobile-user-recommendations',
    'tiktok-mobile-video-detail',
    'tiktok-mobile-video-subtitles',
    'tiktok-popular-trend-country-industry-meta',
    'tiktok-post',
    'tiktok-profile-post',
    'tiktok-profile',
    'tiktok-search',
    'tiktok-search-hashtag',
    'tiktok-search-user',
    'tiktok-top-ads-analysis',
    'tiktok-top-ads-detail',
    'tiktok-top-ads-filters',
    'tiktok-top-ads-list',
    'tiktok-top-ads-location-info',
    'tiktok-top-ads-locations',
    'tiktok-top-ads-recommend',
    'tiktok-top-ads-safety',
    'tiktok-top-ads-spotlight',
    'tiktok-top-ads-suggestions',
    'tiktok-trending',
]

class CrawloraClient:
    tiktok: TiktokGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-category'],
        params: TiktokCategoryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokCategoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-video-comments'],
        params: TiktokVideoCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokVideoCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-creative-center-filters'],
        params: TiktokCreativeCenterFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokCreativeCenterFiltersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-creative-center-hashtags'],
        params: TiktokCreativeCenterHashtagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokCreativeCenterHashtagsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-creative-center-top-content'],
        params: TiktokCreativeCenterTopContentParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokCreativeCenterTopContentResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-creative-center-videos'],
        params: TiktokCreativeCenterVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokCreativeCenterVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-explore'],
        params: TiktokExploreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokExploreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-challenge'],
        params: TiktokChallengeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokChallengeResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-challenge-list'],
        params: TiktokChallengeListParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokChallengeListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-anchor-list'],
        params: TiktokMobileAnchorListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileAnchorListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-collection-detail'],
        params: TiktokMobileCollectionDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCollectionDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-collection-list'],
        params: TiktokMobileCollectionListParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCollectionListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-collection-videos'],
        params: TiktokMobileCollectionVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCollectionVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-comment-replies'],
        params: TiktokMobileCommentRepliesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCommentRepliesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-comments'],
        params: TiktokMobileCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-feed'],
        params: TiktokMobileFeedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileFeedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-feed-offline'],
        params: TiktokMobileFeedOfflineParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileFeedOfflineResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-feed-post'],
        params: TiktokMobileFeedPostParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileFeedPostResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-hashtag'],
        params: TiktokMobileHashtagParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileHashtagResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-hashtag-posts'],
        params: TiktokMobileHashtagPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileHashtagPostsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-hashtags'],
        params: TiktokMobileHashtagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileHashtagsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-effects'],
        params: TiktokMobileLiveEffectsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveEffectsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-gifts'],
        params: TiktokMobileLiveGiftsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveGiftsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-hashtags'],
        params: TiktokMobileLiveHashtagsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveHashtagsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-room'],
        params: TiktokMobileLiveRoomParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveRoomResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-room-by-user'],
        params: TiktokMobileLiveRoomByUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveRoomByUserResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-search'],
        params: TiktokMobileLiveSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-live-tabs'],
        params: TiktokMobileLiveTabsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveTabsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-beats'],
        params: TiktokMobileMusicBeatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicBeatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-chart'],
        params: TiktokMobileMusicChartParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicChartResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-choices'],
        params: TiktokMobileMusicChoicesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicChoicesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-collection-list'],
        params: TiktokMobileMusicCollectionListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicCollectionListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-collections'],
        params: TiktokMobileMusicCollectionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicCollectionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-detail'],
        params: TiktokMobileMusicDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-pick'],
        params: TiktokMobileMusicPickParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicPickResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-posts'],
        params: TiktokMobileMusicPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicPostsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-related'],
        params: TiktokMobileMusicRelatedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicRelatedResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-music-trending'],
        params: TiktokMobileMusicTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicTrendingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-mv-videos'],
        params: TiktokMobileMvVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMvVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-place-detail'],
        params: TiktokMobilePlaceDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-place-info'],
        params: TiktokMobilePlaceInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-place-media'],
        params: TiktokMobilePlaceMediaParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceMediaResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-place-photos'],
        params: TiktokMobilePlacePhotosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlacePhotosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-place-reviews'],
        params: TiktokMobilePlaceReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceReviewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-place-videos'],
        params: TiktokMobilePlaceVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-playlist-detail'],
        params: TiktokMobilePlaylistDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaylistDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-playlist-list'],
        params: TiktokMobilePlaylistListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaylistListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-playlist-videos'],
        params: TiktokMobilePlaylistVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaylistVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search'],
        params: TiktokMobileSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-effects'],
        params: TiktokMobileSearchEffectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchEffectsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-hashtags'],
        params: TiktokMobileSearchHashtagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchHashtagsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-music'],
        params: TiktokMobileSearchMusicParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchMusicResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-photos'],
        params: TiktokMobileSearchPhotosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchPhotosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-place'],
        params: TiktokMobileSearchPlaceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchPlaceResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-pre-info'],
        params: TiktokMobileSearchPreInfoParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchPreInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-stream'],
        params: TiktokMobileSearchStreamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchStreamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-sug'],
        params: TiktokMobileSearchSugParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchSugResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-tabs'],
        params: TiktokMobileSearchTabsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchTabsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-user'],
        params: TiktokMobileSearchUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchUserResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-search-videos'],
        params: TiktokMobileSearchVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-translation-description'],
        params: TiktokMobileTranslationDescriptionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileTranslationDescriptionResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-trending-categories'],
        params: TiktokMobileTrendingCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileTrendingCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-trending-effects'],
        params: TiktokMobileTrendingEffectsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileTrendingEffectsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-followers'],
        params: TiktokMobileUserFollowersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserFollowersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-following'],
        params: TiktokMobileUserFollowingParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserFollowingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-original-effects'],
        params: TiktokMobileUserOriginalEffectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserOriginalEffectsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-original-music'],
        params: TiktokMobileUserOriginalMusicParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserOriginalMusicResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-posts'],
        params: TiktokMobileUserPostsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserPostsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-profile'],
        params: TiktokMobileUserProfileParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserProfileResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-user-recommendations'],
        params: TiktokMobileUserRecommendationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserRecommendationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-video-detail'],
        params: TiktokMobileVideoDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileVideoDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-mobile-video-subtitles'],
        params: TiktokMobileVideoSubtitlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileVideoSubtitlesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-popular-trend-country-industry-meta'],
        params: TiktokPopularTrendCountryIndustryMetaParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokPopularTrendCountryIndustryMetaResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-post'],
        params: TiktokPostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokPostResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-profile-post'],
        params: TiktokProfilePostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokProfilePostResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-profile'],
        params: TiktokProfileParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokProfileResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-search'],
        params: TiktokSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-search-hashtag'],
        params: TiktokSearchHashtagParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokSearchHashtagResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-search-user'],
        params: TiktokSearchUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokSearchUserResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-analysis'],
        params: TiktokTopAdsAnalysisParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsAnalysisResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-detail'],
        params: TiktokTopAdsDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-filters'],
        params: TiktokTopAdsFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsFiltersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-list'],
        params: TiktokTopAdsListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsListResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-location-info'],
        params: TiktokTopAdsLocationInfoParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsLocationInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-locations'],
        params: TiktokTopAdsLocationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsLocationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-recommend'],
        params: TiktokTopAdsRecommendParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsRecommendResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-safety'],
        params: TiktokTopAdsSafetyParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsSafetyResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-spotlight'],
        params: TiktokTopAdsSpotlightParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsSpotlightResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-top-ads-suggestions'],
        params: TiktokTopAdsSuggestionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsSuggestionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['tiktok-trending'],
        params: TiktokTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTrendingResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-category'],
        params: TiktokCategoryParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokCategoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-video-comments'],
        params: TiktokVideoCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokVideoCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-creative-center-filters'],
        params: TiktokCreativeCenterFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokCreativeCenterFiltersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-creative-center-hashtags'],
        params: TiktokCreativeCenterHashtagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokCreativeCenterHashtagsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-creative-center-top-content'],
        params: TiktokCreativeCenterTopContentParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokCreativeCenterTopContentResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-creative-center-videos'],
        params: TiktokCreativeCenterVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokCreativeCenterVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-explore'],
        params: TiktokExploreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokExploreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-challenge'],
        params: TiktokChallengeParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokChallengeResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-challenge-list'],
        params: TiktokChallengeListParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokChallengeListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-anchor-list'],
        params: TiktokMobileAnchorListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileAnchorListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-collection-detail'],
        params: TiktokMobileCollectionDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCollectionDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-collection-list'],
        params: TiktokMobileCollectionListParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCollectionListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-collection-videos'],
        params: TiktokMobileCollectionVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCollectionVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-comment-replies'],
        params: TiktokMobileCommentRepliesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCommentRepliesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-comments'],
        params: TiktokMobileCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-feed'],
        params: TiktokMobileFeedParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileFeedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-feed-offline'],
        params: TiktokMobileFeedOfflineParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileFeedOfflineResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-feed-post'],
        params: TiktokMobileFeedPostParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileFeedPostResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-hashtag'],
        params: TiktokMobileHashtagParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileHashtagResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-hashtag-posts'],
        params: TiktokMobileHashtagPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileHashtagPostsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-hashtags'],
        params: TiktokMobileHashtagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileHashtagsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-effects'],
        params: TiktokMobileLiveEffectsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveEffectsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-gifts'],
        params: TiktokMobileLiveGiftsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveGiftsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-hashtags'],
        params: TiktokMobileLiveHashtagsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveHashtagsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-room'],
        params: TiktokMobileLiveRoomParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveRoomResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-room-by-user'],
        params: TiktokMobileLiveRoomByUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveRoomByUserResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-search'],
        params: TiktokMobileLiveSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-live-tabs'],
        params: TiktokMobileLiveTabsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileLiveTabsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-beats'],
        params: TiktokMobileMusicBeatsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicBeatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-chart'],
        params: TiktokMobileMusicChartParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicChartResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-choices'],
        params: TiktokMobileMusicChoicesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicChoicesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-collection-list'],
        params: TiktokMobileMusicCollectionListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicCollectionListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-collections'],
        params: TiktokMobileMusicCollectionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicCollectionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-detail'],
        params: TiktokMobileMusicDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-pick'],
        params: TiktokMobileMusicPickParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicPickResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-posts'],
        params: TiktokMobileMusicPostsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicPostsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-related'],
        params: TiktokMobileMusicRelatedParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicRelatedResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-music-trending'],
        params: TiktokMobileMusicTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMusicTrendingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-mv-videos'],
        params: TiktokMobileMvVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileMvVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-place-detail'],
        params: TiktokMobilePlaceDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-place-info'],
        params: TiktokMobilePlaceInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-place-media'],
        params: TiktokMobilePlaceMediaParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceMediaResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-place-photos'],
        params: TiktokMobilePlacePhotosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlacePhotosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-place-reviews'],
        params: TiktokMobilePlaceReviewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceReviewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-place-videos'],
        params: TiktokMobilePlaceVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaceVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-playlist-detail'],
        params: TiktokMobilePlaylistDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaylistDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-playlist-list'],
        params: TiktokMobilePlaylistListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaylistListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-playlist-videos'],
        params: TiktokMobilePlaylistVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobilePlaylistVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search'],
        params: TiktokMobileSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-effects'],
        params: TiktokMobileSearchEffectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchEffectsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-hashtags'],
        params: TiktokMobileSearchHashtagsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchHashtagsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-music'],
        params: TiktokMobileSearchMusicParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchMusicResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-photos'],
        params: TiktokMobileSearchPhotosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchPhotosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-place'],
        params: TiktokMobileSearchPlaceParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchPlaceResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-pre-info'],
        params: TiktokMobileSearchPreInfoParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchPreInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-stream'],
        params: TiktokMobileSearchStreamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchStreamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-sug'],
        params: TiktokMobileSearchSugParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchSugResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-tabs'],
        params: TiktokMobileSearchTabsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchTabsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-user'],
        params: TiktokMobileSearchUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchUserResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-search-videos'],
        params: TiktokMobileSearchVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileSearchVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-translation-description'],
        params: TiktokMobileTranslationDescriptionParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileTranslationDescriptionResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-trending-categories'],
        params: TiktokMobileTrendingCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileTrendingCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-trending-effects'],
        params: TiktokMobileTrendingEffectsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileTrendingEffectsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-followers'],
        params: TiktokMobileUserFollowersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserFollowersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-following'],
        params: TiktokMobileUserFollowingParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserFollowingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-original-effects'],
        params: TiktokMobileUserOriginalEffectsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserOriginalEffectsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-original-music'],
        params: TiktokMobileUserOriginalMusicParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserOriginalMusicResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-posts'],
        params: TiktokMobileUserPostsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserPostsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-profile'],
        params: TiktokMobileUserProfileParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserProfileResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-user-recommendations'],
        params: TiktokMobileUserRecommendationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileUserRecommendationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-video-detail'],
        params: TiktokMobileVideoDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileVideoDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-mobile-video-subtitles'],
        params: TiktokMobileVideoSubtitlesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokMobileVideoSubtitlesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-popular-trend-country-industry-meta'],
        params: TiktokPopularTrendCountryIndustryMetaParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokPopularTrendCountryIndustryMetaResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-post'],
        params: TiktokPostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokPostResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-profile-post'],
        params: TiktokProfilePostParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokProfilePostResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-profile'],
        params: TiktokProfileParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokProfileResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-search'],
        params: TiktokSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-search-hashtag'],
        params: TiktokSearchHashtagParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokSearchHashtagResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-search-user'],
        params: TiktokSearchUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokSearchUserResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-analysis'],
        params: TiktokTopAdsAnalysisParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsAnalysisResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-detail'],
        params: TiktokTopAdsDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-filters'],
        params: TiktokTopAdsFiltersParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsFiltersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-list'],
        params: TiktokTopAdsListParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsListResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-location-info'],
        params: TiktokTopAdsLocationInfoParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsLocationInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-locations'],
        params: TiktokTopAdsLocationsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsLocationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-recommend'],
        params: TiktokTopAdsRecommendParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsRecommendResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-safety'],
        params: TiktokTopAdsSafetyParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsSafetyResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-spotlight'],
        params: TiktokTopAdsSpotlightParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsSpotlightResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-top-ads-suggestions'],
        params: TiktokTopAdsSuggestionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTopAdsSuggestionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['tiktok-trending'],
        params: TiktokTrendingParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> TiktokTrendingResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class TikTokClient(CrawloraClient):
    def __enter__(self) -> TikTokClient: ...
    @overload
    def category(self, **params: Unpack[TiktokCategoryStreamParams]) -> BinaryIO: ...
    @overload
    def category(self, **params: Unpack[TiktokCategoryTextResponseParams]) -> str: ...
    @overload
    def category(self, **params: Unpack[TiktokCategoryDefaultParams]) -> TiktokCategoryResponse: ...
    @overload
    def video_comments(self, **params: Unpack[TiktokVideoCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def video_comments(self, **params: Unpack[TiktokVideoCommentsTextResponseParams]) -> str: ...
    @overload
    def video_comments(self, **params: Unpack[TiktokVideoCommentsDefaultParams]) -> TiktokVideoCommentsResponse: ...
    @overload
    def creative_center_filters(self, **params: Unpack[TiktokCreativeCenterFiltersStreamParams]) -> BinaryIO: ...
    @overload
    def creative_center_filters(self, **params: Unpack[TiktokCreativeCenterFiltersTextResponseParams]) -> str: ...
    @overload
    def creative_center_filters(self, **params: Unpack[TiktokCreativeCenterFiltersDefaultParams]) -> TiktokCreativeCenterFiltersResponse: ...
    @overload
    def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsTextResponseParams]) -> str: ...
    @overload
    def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsDefaultParams]) -> TiktokCreativeCenterHashtagsResponse: ...
    @overload
    def creative_center_top_content(self, **params: Unpack[TiktokCreativeCenterTopContentStreamParams]) -> BinaryIO: ...
    @overload
    def creative_center_top_content(self, **params: Unpack[TiktokCreativeCenterTopContentTextResponseParams]) -> str: ...
    @overload
    def creative_center_top_content(self, **params: Unpack[TiktokCreativeCenterTopContentDefaultParams]) -> TiktokCreativeCenterTopContentResponse: ...
    @overload
    def creative_center_videos(self, **params: Unpack[TiktokCreativeCenterVideosStreamParams]) -> BinaryIO: ...
    @overload
    def creative_center_videos(self, **params: Unpack[TiktokCreativeCenterVideosTextResponseParams]) -> str: ...
    @overload
    def creative_center_videos(self, **params: Unpack[TiktokCreativeCenterVideosDefaultParams]) -> TiktokCreativeCenterVideosResponse: ...
    @overload
    def explore(self, **params: Unpack[TiktokExploreStreamParams]) -> BinaryIO: ...
    @overload
    def explore(self, **params: Unpack[TiktokExploreTextResponseParams]) -> str: ...
    @overload
    def explore(self, **params: Unpack[TiktokExploreDefaultParams]) -> TiktokExploreResponse: ...
    @overload
    def challenge(self, **params: Unpack[TiktokChallengeStreamParams]) -> BinaryIO: ...
    @overload
    def challenge(self, **params: Unpack[TiktokChallengeTextResponseParams]) -> str: ...
    @overload
    def challenge(self, **params: Unpack[TiktokChallengeDefaultParams]) -> TiktokChallengeResponse: ...
    @overload
    def challenge_list(self, **params: Unpack[TiktokChallengeListStreamParams]) -> BinaryIO: ...
    @overload
    def challenge_list(self, **params: Unpack[TiktokChallengeListTextResponseParams]) -> str: ...
    @overload
    def challenge_list(self, **params: Unpack[TiktokChallengeListDefaultParams]) -> TiktokChallengeListResponse: ...
    @overload
    def mobile_anchor_list(self, **params: Unpack[TiktokMobileAnchorListStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_anchor_list(self, **params: Unpack[TiktokMobileAnchorListTextResponseParams]) -> str: ...
    @overload
    def mobile_anchor_list(self, **params: Unpack[TiktokMobileAnchorListDefaultParams]) -> TiktokMobileAnchorListResponse: ...
    @overload
    def mobile_collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailTextResponseParams]) -> str: ...
    @overload
    def mobile_collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailDefaultParams]) -> TiktokMobileCollectionDetailResponse: ...
    @overload
    def mobile_collection_list(self, **params: Unpack[TiktokMobileCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_collection_list(self, **params: Unpack[TiktokMobileCollectionListTextResponseParams]) -> str: ...
    @overload
    def mobile_collection_list(self, **params: Unpack[TiktokMobileCollectionListDefaultParams]) -> TiktokMobileCollectionListResponse: ...
    @overload
    def mobile_collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosTextResponseParams]) -> str: ...
    @overload
    def mobile_collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosDefaultParams]) -> TiktokMobileCollectionVideosResponse: ...
    @overload
    def mobile_comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesTextResponseParams]) -> str: ...
    @overload
    def mobile_comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesDefaultParams]) -> TiktokMobileCommentRepliesResponse: ...
    @overload
    def mobile_comments(self, **params: Unpack[TiktokMobileCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_comments(self, **params: Unpack[TiktokMobileCommentsTextResponseParams]) -> str: ...
    @overload
    def mobile_comments(self, **params: Unpack[TiktokMobileCommentsDefaultParams]) -> TiktokMobileCommentsResponse: ...
    @overload
    def mobile_feed(self, **params: Unpack[TiktokMobileFeedStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_feed(self, **params: Unpack[TiktokMobileFeedTextResponseParams]) -> str: ...
    @overload
    def mobile_feed(self, **params: Unpack[TiktokMobileFeedDefaultParams]) -> TiktokMobileFeedResponse: ...
    @overload
    def mobile_feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineTextResponseParams]) -> str: ...
    @overload
    def mobile_feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineDefaultParams]) -> TiktokMobileFeedOfflineResponse: ...
    @overload
    def mobile_feed_post(self, **params: Unpack[TiktokMobileFeedPostStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_feed_post(self, **params: Unpack[TiktokMobileFeedPostTextResponseParams]) -> str: ...
    @overload
    def mobile_feed_post(self, **params: Unpack[TiktokMobileFeedPostDefaultParams]) -> TiktokMobileFeedPostResponse: ...
    @overload
    def mobile_hashtag(self, **params: Unpack[TiktokMobileHashtagStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_hashtag(self, **params: Unpack[TiktokMobileHashtagTextResponseParams]) -> str: ...
    @overload
    def mobile_hashtag(self, **params: Unpack[TiktokMobileHashtagDefaultParams]) -> TiktokMobileHashtagResponse: ...
    @overload
    def mobile_hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsTextResponseParams]) -> str: ...
    @overload
    def mobile_hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsDefaultParams]) -> TiktokMobileHashtagPostsResponse: ...
    @overload
    def mobile_hashtags(self, **params: Unpack[TiktokMobileHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_hashtags(self, **params: Unpack[TiktokMobileHashtagsTextResponseParams]) -> str: ...
    @overload
    def mobile_hashtags(self, **params: Unpack[TiktokMobileHashtagsDefaultParams]) -> TiktokMobileHashtagsResponse: ...
    @overload
    def mobile_live_effects(self, **params: Unpack[TiktokMobileLiveEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_effects(self, **params: Unpack[TiktokMobileLiveEffectsTextResponseParams]) -> str: ...
    @overload
    def mobile_live_effects(self, **params: Unpack[TiktokMobileLiveEffectsDefaultParams]) -> TiktokMobileLiveEffectsResponse: ...
    @overload
    def mobile_live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsTextResponseParams]) -> str: ...
    @overload
    def mobile_live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsDefaultParams]) -> TiktokMobileLiveGiftsResponse: ...
    @overload
    def mobile_live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsTextResponseParams]) -> str: ...
    @overload
    def mobile_live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsDefaultParams]) -> TiktokMobileLiveHashtagsResponse: ...
    @overload
    def mobile_live_room(self, **params: Unpack[TiktokMobileLiveRoomStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_room(self, **params: Unpack[TiktokMobileLiveRoomTextResponseParams]) -> str: ...
    @overload
    def mobile_live_room(self, **params: Unpack[TiktokMobileLiveRoomDefaultParams]) -> TiktokMobileLiveRoomResponse: ...
    @overload
    def mobile_live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserTextResponseParams]) -> str: ...
    @overload
    def mobile_live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserDefaultParams]) -> TiktokMobileLiveRoomByUserResponse: ...
    @overload
    def mobile_live_search(self, **params: Unpack[TiktokMobileLiveSearchStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_search(self, **params: Unpack[TiktokMobileLiveSearchTextResponseParams]) -> str: ...
    @overload
    def mobile_live_search(self, **params: Unpack[TiktokMobileLiveSearchDefaultParams]) -> TiktokMobileLiveSearchResponse: ...
    @overload
    def mobile_live_tabs(self, **params: Unpack[TiktokMobileLiveTabsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_live_tabs(self, **params: Unpack[TiktokMobileLiveTabsTextResponseParams]) -> str: ...
    @overload
    def mobile_live_tabs(self, **params: Unpack[TiktokMobileLiveTabsDefaultParams]) -> TiktokMobileLiveTabsResponse: ...
    @overload
    def mobile_music_beats(self, **params: Unpack[TiktokMobileMusicBeatsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_beats(self, **params: Unpack[TiktokMobileMusicBeatsTextResponseParams]) -> str: ...
    @overload
    def mobile_music_beats(self, **params: Unpack[TiktokMobileMusicBeatsDefaultParams]) -> TiktokMobileMusicBeatsResponse: ...
    @overload
    def mobile_music_chart(self, **params: Unpack[TiktokMobileMusicChartStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_chart(self, **params: Unpack[TiktokMobileMusicChartTextResponseParams]) -> str: ...
    @overload
    def mobile_music_chart(self, **params: Unpack[TiktokMobileMusicChartDefaultParams]) -> TiktokMobileMusicChartResponse: ...
    @overload
    def mobile_music_choices(self, **params: Unpack[TiktokMobileMusicChoicesStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_choices(self, **params: Unpack[TiktokMobileMusicChoicesTextResponseParams]) -> str: ...
    @overload
    def mobile_music_choices(self, **params: Unpack[TiktokMobileMusicChoicesDefaultParams]) -> TiktokMobileMusicChoicesResponse: ...
    @overload
    def mobile_music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListTextResponseParams]) -> str: ...
    @overload
    def mobile_music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListDefaultParams]) -> TiktokMobileMusicCollectionListResponse: ...
    @overload
    def mobile_music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsTextResponseParams]) -> str: ...
    @overload
    def mobile_music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsDefaultParams]) -> TiktokMobileMusicCollectionsResponse: ...
    @overload
    def mobile_music_detail(self, **params: Unpack[TiktokMobileMusicDetailStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_detail(self, **params: Unpack[TiktokMobileMusicDetailTextResponseParams]) -> str: ...
    @overload
    def mobile_music_detail(self, **params: Unpack[TiktokMobileMusicDetailDefaultParams]) -> TiktokMobileMusicDetailResponse: ...
    @overload
    def mobile_music_pick(self, **params: Unpack[TiktokMobileMusicPickStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_pick(self, **params: Unpack[TiktokMobileMusicPickTextResponseParams]) -> str: ...
    @overload
    def mobile_music_pick(self, **params: Unpack[TiktokMobileMusicPickDefaultParams]) -> TiktokMobileMusicPickResponse: ...
    @overload
    def mobile_music_posts(self, **params: Unpack[TiktokMobileMusicPostsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_posts(self, **params: Unpack[TiktokMobileMusicPostsTextResponseParams]) -> str: ...
    @overload
    def mobile_music_posts(self, **params: Unpack[TiktokMobileMusicPostsDefaultParams]) -> TiktokMobileMusicPostsResponse: ...
    @overload
    def mobile_music_related(self, **params: Unpack[TiktokMobileMusicRelatedStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_related(self, **params: Unpack[TiktokMobileMusicRelatedTextResponseParams]) -> str: ...
    @overload
    def mobile_music_related(self, **params: Unpack[TiktokMobileMusicRelatedDefaultParams]) -> TiktokMobileMusicRelatedResponse: ...
    @overload
    def mobile_music_trending(self, **params: Unpack[TiktokMobileMusicTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_music_trending(self, **params: Unpack[TiktokMobileMusicTrendingTextResponseParams]) -> str: ...
    @overload
    def mobile_music_trending(self, **params: Unpack[TiktokMobileMusicTrendingDefaultParams]) -> TiktokMobileMusicTrendingResponse: ...
    @overload
    def mobile_mv_videos(self, **params: Unpack[TiktokMobileMvVideosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_mv_videos(self, **params: Unpack[TiktokMobileMvVideosTextResponseParams]) -> str: ...
    @overload
    def mobile_mv_videos(self, **params: Unpack[TiktokMobileMvVideosDefaultParams]) -> TiktokMobileMvVideosResponse: ...
    @overload
    def mobile_place_detail(self, **params: Unpack[TiktokMobilePlaceDetailStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_place_detail(self, **params: Unpack[TiktokMobilePlaceDetailTextResponseParams]) -> str: ...
    @overload
    def mobile_place_detail(self, **params: Unpack[TiktokMobilePlaceDetailDefaultParams]) -> TiktokMobilePlaceDetailResponse: ...
    @overload
    def mobile_place_info(self, **params: Unpack[TiktokMobilePlaceInfoStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_place_info(self, **params: Unpack[TiktokMobilePlaceInfoTextResponseParams]) -> str: ...
    @overload
    def mobile_place_info(self, **params: Unpack[TiktokMobilePlaceInfoDefaultParams]) -> TiktokMobilePlaceInfoResponse: ...
    @overload
    def mobile_place_media(self, **params: Unpack[TiktokMobilePlaceMediaStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_place_media(self, **params: Unpack[TiktokMobilePlaceMediaTextResponseParams]) -> str: ...
    @overload
    def mobile_place_media(self, **params: Unpack[TiktokMobilePlaceMediaDefaultParams]) -> TiktokMobilePlaceMediaResponse: ...
    @overload
    def mobile_place_photos(self, **params: Unpack[TiktokMobilePlacePhotosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_place_photos(self, **params: Unpack[TiktokMobilePlacePhotosTextResponseParams]) -> str: ...
    @overload
    def mobile_place_photos(self, **params: Unpack[TiktokMobilePlacePhotosDefaultParams]) -> TiktokMobilePlacePhotosResponse: ...
    @overload
    def mobile_place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsTextResponseParams]) -> str: ...
    @overload
    def mobile_place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsDefaultParams]) -> TiktokMobilePlaceReviewsResponse: ...
    @overload
    def mobile_place_videos(self, **params: Unpack[TiktokMobilePlaceVideosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_place_videos(self, **params: Unpack[TiktokMobilePlaceVideosTextResponseParams]) -> str: ...
    @overload
    def mobile_place_videos(self, **params: Unpack[TiktokMobilePlaceVideosDefaultParams]) -> TiktokMobilePlaceVideosResponse: ...
    @overload
    def mobile_playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailTextResponseParams]) -> str: ...
    @overload
    def mobile_playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailDefaultParams]) -> TiktokMobilePlaylistDetailResponse: ...
    @overload
    def mobile_playlist_list(self, **params: Unpack[TiktokMobilePlaylistListStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_playlist_list(self, **params: Unpack[TiktokMobilePlaylistListTextResponseParams]) -> str: ...
    @overload
    def mobile_playlist_list(self, **params: Unpack[TiktokMobilePlaylistListDefaultParams]) -> TiktokMobilePlaylistListResponse: ...
    @overload
    def mobile_playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosTextResponseParams]) -> str: ...
    @overload
    def mobile_playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosDefaultParams]) -> TiktokMobilePlaylistVideosResponse: ...
    @overload
    def mobile_search(self, **params: Unpack[TiktokMobileSearchResponseStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search(self, **params: Unpack[TiktokMobileSearchTextResponseParams]) -> str: ...
    @overload
    def mobile_search(self, **params: Unpack[TiktokMobileSearchDefaultParams]) -> TiktokMobileSearchResponse: ...
    @overload
    def mobile_search_effects(self, **params: Unpack[TiktokMobileSearchEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_effects(self, **params: Unpack[TiktokMobileSearchEffectsTextResponseParams]) -> str: ...
    @overload
    def mobile_search_effects(self, **params: Unpack[TiktokMobileSearchEffectsDefaultParams]) -> TiktokMobileSearchEffectsResponse: ...
    @overload
    def mobile_search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsTextResponseParams]) -> str: ...
    @overload
    def mobile_search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsDefaultParams]) -> TiktokMobileSearchHashtagsResponse: ...
    @overload
    def mobile_search_music(self, **params: Unpack[TiktokMobileSearchMusicStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_music(self, **params: Unpack[TiktokMobileSearchMusicTextResponseParams]) -> str: ...
    @overload
    def mobile_search_music(self, **params: Unpack[TiktokMobileSearchMusicDefaultParams]) -> TiktokMobileSearchMusicResponse: ...
    @overload
    def mobile_search_photos(self, **params: Unpack[TiktokMobileSearchPhotosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_photos(self, **params: Unpack[TiktokMobileSearchPhotosTextResponseParams]) -> str: ...
    @overload
    def mobile_search_photos(self, **params: Unpack[TiktokMobileSearchPhotosDefaultParams]) -> TiktokMobileSearchPhotosResponse: ...
    @overload
    def mobile_search_place(self, **params: Unpack[TiktokMobileSearchPlaceStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_place(self, **params: Unpack[TiktokMobileSearchPlaceTextResponseParams]) -> str: ...
    @overload
    def mobile_search_place(self, **params: Unpack[TiktokMobileSearchPlaceDefaultParams]) -> TiktokMobileSearchPlaceResponse: ...
    @overload
    def mobile_search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoTextResponseParams]) -> str: ...
    @overload
    def mobile_search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoDefaultParams]) -> TiktokMobileSearchPreInfoResponse: ...
    @overload
    def mobile_search_stream(self, **params: Unpack[TiktokMobileSearchStreamStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_stream(self, **params: Unpack[TiktokMobileSearchStreamTextResponseParams]) -> str: ...
    @overload
    def mobile_search_stream(self, **params: Unpack[TiktokMobileSearchStreamDefaultParams]) -> TiktokMobileSearchStreamResponse: ...
    @overload
    def mobile_search_sug(self, **params: Unpack[TiktokMobileSearchSugStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_sug(self, **params: Unpack[TiktokMobileSearchSugTextResponseParams]) -> str: ...
    @overload
    def mobile_search_sug(self, **params: Unpack[TiktokMobileSearchSugDefaultParams]) -> TiktokMobileSearchSugResponse: ...
    @overload
    def mobile_search_tabs(self, **params: Unpack[TiktokMobileSearchTabsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_tabs(self, **params: Unpack[TiktokMobileSearchTabsTextResponseParams]) -> str: ...
    @overload
    def mobile_search_tabs(self, **params: Unpack[TiktokMobileSearchTabsDefaultParams]) -> TiktokMobileSearchTabsResponse: ...
    @overload
    def mobile_search_user(self, **params: Unpack[TiktokMobileSearchUserStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_user(self, **params: Unpack[TiktokMobileSearchUserTextResponseParams]) -> str: ...
    @overload
    def mobile_search_user(self, **params: Unpack[TiktokMobileSearchUserDefaultParams]) -> TiktokMobileSearchUserResponse: ...
    @overload
    def mobile_search_videos(self, **params: Unpack[TiktokMobileSearchVideosStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_search_videos(self, **params: Unpack[TiktokMobileSearchVideosTextResponseParams]) -> str: ...
    @overload
    def mobile_search_videos(self, **params: Unpack[TiktokMobileSearchVideosDefaultParams]) -> TiktokMobileSearchVideosResponse: ...
    @overload
    def mobile_translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionTextResponseParams]) -> str: ...
    @overload
    def mobile_translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionDefaultParams]) -> TiktokMobileTranslationDescriptionResponse: ...
    @overload
    def mobile_trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesTextResponseParams]) -> str: ...
    @overload
    def mobile_trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesDefaultParams]) -> TiktokMobileTrendingCategoriesResponse: ...
    @overload
    def mobile_trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsTextResponseParams]) -> str: ...
    @overload
    def mobile_trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsDefaultParams]) -> TiktokMobileTrendingEffectsResponse: ...
    @overload
    def mobile_user_followers(self, **params: Unpack[TiktokMobileUserFollowersStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_followers(self, **params: Unpack[TiktokMobileUserFollowersTextResponseParams]) -> str: ...
    @overload
    def mobile_user_followers(self, **params: Unpack[TiktokMobileUserFollowersDefaultParams]) -> TiktokMobileUserFollowersResponse: ...
    @overload
    def mobile_user_following(self, **params: Unpack[TiktokMobileUserFollowingStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_following(self, **params: Unpack[TiktokMobileUserFollowingTextResponseParams]) -> str: ...
    @overload
    def mobile_user_following(self, **params: Unpack[TiktokMobileUserFollowingDefaultParams]) -> TiktokMobileUserFollowingResponse: ...
    @overload
    def mobile_user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsTextResponseParams]) -> str: ...
    @overload
    def mobile_user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsDefaultParams]) -> TiktokMobileUserOriginalEffectsResponse: ...
    @overload
    def mobile_user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicTextResponseParams]) -> str: ...
    @overload
    def mobile_user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicDefaultParams]) -> TiktokMobileUserOriginalMusicResponse: ...
    @overload
    def mobile_user_posts(self, **params: Unpack[TiktokMobileUserPostsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_posts(self, **params: Unpack[TiktokMobileUserPostsTextResponseParams]) -> str: ...
    @overload
    def mobile_user_posts(self, **params: Unpack[TiktokMobileUserPostsDefaultParams]) -> TiktokMobileUserPostsResponse: ...
    @overload
    def mobile_user_profile(self, **params: Unpack[TiktokMobileUserProfileStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_profile(self, **params: Unpack[TiktokMobileUserProfileTextResponseParams]) -> str: ...
    @overload
    def mobile_user_profile(self, **params: Unpack[TiktokMobileUserProfileDefaultParams]) -> TiktokMobileUserProfileResponse: ...
    @overload
    def mobile_user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsTextResponseParams]) -> str: ...
    @overload
    def mobile_user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsDefaultParams]) -> TiktokMobileUserRecommendationsResponse: ...
    @overload
    def mobile_video_detail(self, **params: Unpack[TiktokMobileVideoDetailStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_video_detail(self, **params: Unpack[TiktokMobileVideoDetailTextResponseParams]) -> str: ...
    @overload
    def mobile_video_detail(self, **params: Unpack[TiktokMobileVideoDetailDefaultParams]) -> TiktokMobileVideoDetailResponse: ...
    @overload
    def mobile_video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesStreamParams]) -> BinaryIO: ...
    @overload
    def mobile_video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesTextResponseParams]) -> str: ...
    @overload
    def mobile_video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesDefaultParams]) -> TiktokMobileVideoSubtitlesResponse: ...
    @overload
    def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaStreamParams]) -> BinaryIO: ...
    @overload
    def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaTextResponseParams]) -> str: ...
    @overload
    def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaDefaultParams]) -> TiktokPopularTrendCountryIndustryMetaResponse: ...
    @overload
    def post(self, **params: Unpack[TiktokPostStreamParams]) -> BinaryIO: ...
    @overload
    def post(self, **params: Unpack[TiktokPostTextResponseParams]) -> str: ...
    @overload
    def post(self, **params: Unpack[TiktokPostDefaultParams]) -> TiktokPostResponse: ...
    @overload
    def profile_post(self, **params: Unpack[TiktokProfilePostStreamParams]) -> BinaryIO: ...
    @overload
    def profile_post(self, **params: Unpack[TiktokProfilePostTextResponseParams]) -> str: ...
    @overload
    def profile_post(self, **params: Unpack[TiktokProfilePostDefaultParams]) -> TiktokProfilePostResponse: ...
    @overload
    def profile(self, **params: Unpack[TiktokProfileStreamParams]) -> BinaryIO: ...
    @overload
    def profile(self, **params: Unpack[TiktokProfileTextResponseParams]) -> str: ...
    @overload
    def profile(self, **params: Unpack[TiktokProfileDefaultParams]) -> TiktokProfileResponse: ...
    @overload
    def search(self, **params: Unpack[TiktokSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[TiktokSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[TiktokSearchDefaultParams]) -> TiktokSearchResponse: ...
    @overload
    def search_hashtag(self, **params: Unpack[TiktokSearchHashtagStreamParams]) -> BinaryIO: ...
    @overload
    def search_hashtag(self, **params: Unpack[TiktokSearchHashtagTextResponseParams]) -> str: ...
    @overload
    def search_hashtag(self, **params: Unpack[TiktokSearchHashtagDefaultParams]) -> TiktokSearchHashtagResponse: ...
    @overload
    def search_user(self, **params: Unpack[TiktokSearchUserStreamParams]) -> BinaryIO: ...
    @overload
    def search_user(self, **params: Unpack[TiktokSearchUserTextResponseParams]) -> str: ...
    @overload
    def search_user(self, **params: Unpack[TiktokSearchUserDefaultParams]) -> TiktokSearchUserResponse: ...
    @overload
    def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisTextResponseParams]) -> str: ...
    @overload
    def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisDefaultParams]) -> TiktokTopAdsAnalysisResponse: ...
    @overload
    def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailTextResponseParams]) -> str: ...
    @overload
    def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailDefaultParams]) -> TiktokTopAdsDetailResponse: ...
    @overload
    def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersTextResponseParams]) -> str: ...
    @overload
    def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersDefaultParams]) -> TiktokTopAdsFiltersResponse: ...
    @overload
    def top_ads_list(self, **params: Unpack[TiktokTopAdsListStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_list(self, **params: Unpack[TiktokTopAdsListTextResponseParams]) -> str: ...
    @overload
    def top_ads_list(self, **params: Unpack[TiktokTopAdsListDefaultParams]) -> TiktokTopAdsListResponse: ...
    @overload
    def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoTextResponseParams]) -> str: ...
    @overload
    def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoDefaultParams]) -> TiktokTopAdsLocationInfoResponse: ...
    @overload
    def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsTextResponseParams]) -> str: ...
    @overload
    def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsDefaultParams]) -> TiktokTopAdsLocationsResponse: ...
    @overload
    def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendTextResponseParams]) -> str: ...
    @overload
    def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendDefaultParams]) -> TiktokTopAdsRecommendResponse: ...
    @overload
    def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyTextResponseParams]) -> str: ...
    @overload
    def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyDefaultParams]) -> TiktokTopAdsSafetyResponse: ...
    @overload
    def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightTextResponseParams]) -> str: ...
    @overload
    def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightDefaultParams]) -> TiktokTopAdsSpotlightResponse: ...
    @overload
    def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsStreamParams]) -> BinaryIO: ...
    @overload
    def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsTextResponseParams]) -> str: ...
    @overload
    def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsDefaultParams]) -> TiktokTopAdsSuggestionsResponse: ...
    @overload
    def trending(self, **params: Unpack[TiktokTrendingStreamParams]) -> BinaryIO: ...
    @overload
    def trending(self, **params: Unpack[TiktokTrendingTextResponseParams]) -> str: ...
    @overload
    def trending(self, **params: Unpack[TiktokTrendingDefaultParams]) -> TiktokTrendingResponse: ...

class AsyncTikTokClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncTikTokClient: ...
    tiktok: _AsyncTiktokGroup
    @overload
    async def category(self, **params: Unpack[TiktokCategoryStreamParams]) -> BinaryIO: ...
    @overload
    async def category(self, **params: Unpack[TiktokCategoryTextResponseParams]) -> str: ...
    @overload
    async def category(self, **params: Unpack[TiktokCategoryDefaultParams]) -> TiktokCategoryResponse: ...
    @overload
    async def video_comments(self, **params: Unpack[TiktokVideoCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def video_comments(self, **params: Unpack[TiktokVideoCommentsTextResponseParams]) -> str: ...
    @overload
    async def video_comments(self, **params: Unpack[TiktokVideoCommentsDefaultParams]) -> TiktokVideoCommentsResponse: ...
    @overload
    async def creative_center_filters(self, **params: Unpack[TiktokCreativeCenterFiltersStreamParams]) -> BinaryIO: ...
    @overload
    async def creative_center_filters(self, **params: Unpack[TiktokCreativeCenterFiltersTextResponseParams]) -> str: ...
    @overload
    async def creative_center_filters(self, **params: Unpack[TiktokCreativeCenterFiltersDefaultParams]) -> TiktokCreativeCenterFiltersResponse: ...
    @overload
    async def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsTextResponseParams]) -> str: ...
    @overload
    async def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsDefaultParams]) -> TiktokCreativeCenterHashtagsResponse: ...
    @overload
    async def creative_center_top_content(self, **params: Unpack[TiktokCreativeCenterTopContentStreamParams]) -> BinaryIO: ...
    @overload
    async def creative_center_top_content(self, **params: Unpack[TiktokCreativeCenterTopContentTextResponseParams]) -> str: ...
    @overload
    async def creative_center_top_content(self, **params: Unpack[TiktokCreativeCenterTopContentDefaultParams]) -> TiktokCreativeCenterTopContentResponse: ...
    @overload
    async def creative_center_videos(self, **params: Unpack[TiktokCreativeCenterVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def creative_center_videos(self, **params: Unpack[TiktokCreativeCenterVideosTextResponseParams]) -> str: ...
    @overload
    async def creative_center_videos(self, **params: Unpack[TiktokCreativeCenterVideosDefaultParams]) -> TiktokCreativeCenterVideosResponse: ...
    @overload
    async def explore(self, **params: Unpack[TiktokExploreStreamParams]) -> BinaryIO: ...
    @overload
    async def explore(self, **params: Unpack[TiktokExploreTextResponseParams]) -> str: ...
    @overload
    async def explore(self, **params: Unpack[TiktokExploreDefaultParams]) -> TiktokExploreResponse: ...
    @overload
    async def challenge(self, **params: Unpack[TiktokChallengeStreamParams]) -> BinaryIO: ...
    @overload
    async def challenge(self, **params: Unpack[TiktokChallengeTextResponseParams]) -> str: ...
    @overload
    async def challenge(self, **params: Unpack[TiktokChallengeDefaultParams]) -> TiktokChallengeResponse: ...
    @overload
    async def challenge_list(self, **params: Unpack[TiktokChallengeListStreamParams]) -> BinaryIO: ...
    @overload
    async def challenge_list(self, **params: Unpack[TiktokChallengeListTextResponseParams]) -> str: ...
    @overload
    async def challenge_list(self, **params: Unpack[TiktokChallengeListDefaultParams]) -> TiktokChallengeListResponse: ...
    @overload
    async def mobile_anchor_list(self, **params: Unpack[TiktokMobileAnchorListStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_anchor_list(self, **params: Unpack[TiktokMobileAnchorListTextResponseParams]) -> str: ...
    @overload
    async def mobile_anchor_list(self, **params: Unpack[TiktokMobileAnchorListDefaultParams]) -> TiktokMobileAnchorListResponse: ...
    @overload
    async def mobile_collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailTextResponseParams]) -> str: ...
    @overload
    async def mobile_collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailDefaultParams]) -> TiktokMobileCollectionDetailResponse: ...
    @overload
    async def mobile_collection_list(self, **params: Unpack[TiktokMobileCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_collection_list(self, **params: Unpack[TiktokMobileCollectionListTextResponseParams]) -> str: ...
    @overload
    async def mobile_collection_list(self, **params: Unpack[TiktokMobileCollectionListDefaultParams]) -> TiktokMobileCollectionListResponse: ...
    @overload
    async def mobile_collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosTextResponseParams]) -> str: ...
    @overload
    async def mobile_collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosDefaultParams]) -> TiktokMobileCollectionVideosResponse: ...
    @overload
    async def mobile_comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesTextResponseParams]) -> str: ...
    @overload
    async def mobile_comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesDefaultParams]) -> TiktokMobileCommentRepliesResponse: ...
    @overload
    async def mobile_comments(self, **params: Unpack[TiktokMobileCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_comments(self, **params: Unpack[TiktokMobileCommentsTextResponseParams]) -> str: ...
    @overload
    async def mobile_comments(self, **params: Unpack[TiktokMobileCommentsDefaultParams]) -> TiktokMobileCommentsResponse: ...
    @overload
    async def mobile_feed(self, **params: Unpack[TiktokMobileFeedStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_feed(self, **params: Unpack[TiktokMobileFeedTextResponseParams]) -> str: ...
    @overload
    async def mobile_feed(self, **params: Unpack[TiktokMobileFeedDefaultParams]) -> TiktokMobileFeedResponse: ...
    @overload
    async def mobile_feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineTextResponseParams]) -> str: ...
    @overload
    async def mobile_feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineDefaultParams]) -> TiktokMobileFeedOfflineResponse: ...
    @overload
    async def mobile_feed_post(self, **params: Unpack[TiktokMobileFeedPostStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_feed_post(self, **params: Unpack[TiktokMobileFeedPostTextResponseParams]) -> str: ...
    @overload
    async def mobile_feed_post(self, **params: Unpack[TiktokMobileFeedPostDefaultParams]) -> TiktokMobileFeedPostResponse: ...
    @overload
    async def mobile_hashtag(self, **params: Unpack[TiktokMobileHashtagStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_hashtag(self, **params: Unpack[TiktokMobileHashtagTextResponseParams]) -> str: ...
    @overload
    async def mobile_hashtag(self, **params: Unpack[TiktokMobileHashtagDefaultParams]) -> TiktokMobileHashtagResponse: ...
    @overload
    async def mobile_hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsTextResponseParams]) -> str: ...
    @overload
    async def mobile_hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsDefaultParams]) -> TiktokMobileHashtagPostsResponse: ...
    @overload
    async def mobile_hashtags(self, **params: Unpack[TiktokMobileHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_hashtags(self, **params: Unpack[TiktokMobileHashtagsTextResponseParams]) -> str: ...
    @overload
    async def mobile_hashtags(self, **params: Unpack[TiktokMobileHashtagsDefaultParams]) -> TiktokMobileHashtagsResponse: ...
    @overload
    async def mobile_live_effects(self, **params: Unpack[TiktokMobileLiveEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_effects(self, **params: Unpack[TiktokMobileLiveEffectsTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_effects(self, **params: Unpack[TiktokMobileLiveEffectsDefaultParams]) -> TiktokMobileLiveEffectsResponse: ...
    @overload
    async def mobile_live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsDefaultParams]) -> TiktokMobileLiveGiftsResponse: ...
    @overload
    async def mobile_live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsDefaultParams]) -> TiktokMobileLiveHashtagsResponse: ...
    @overload
    async def mobile_live_room(self, **params: Unpack[TiktokMobileLiveRoomStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_room(self, **params: Unpack[TiktokMobileLiveRoomTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_room(self, **params: Unpack[TiktokMobileLiveRoomDefaultParams]) -> TiktokMobileLiveRoomResponse: ...
    @overload
    async def mobile_live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserDefaultParams]) -> TiktokMobileLiveRoomByUserResponse: ...
    @overload
    async def mobile_live_search(self, **params: Unpack[TiktokMobileLiveSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_search(self, **params: Unpack[TiktokMobileLiveSearchTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_search(self, **params: Unpack[TiktokMobileLiveSearchDefaultParams]) -> TiktokMobileLiveSearchResponse: ...
    @overload
    async def mobile_live_tabs(self, **params: Unpack[TiktokMobileLiveTabsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_tabs(self, **params: Unpack[TiktokMobileLiveTabsTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_tabs(self, **params: Unpack[TiktokMobileLiveTabsDefaultParams]) -> TiktokMobileLiveTabsResponse: ...
    @overload
    async def mobile_music_beats(self, **params: Unpack[TiktokMobileMusicBeatsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_beats(self, **params: Unpack[TiktokMobileMusicBeatsTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_beats(self, **params: Unpack[TiktokMobileMusicBeatsDefaultParams]) -> TiktokMobileMusicBeatsResponse: ...
    @overload
    async def mobile_music_chart(self, **params: Unpack[TiktokMobileMusicChartStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_chart(self, **params: Unpack[TiktokMobileMusicChartTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_chart(self, **params: Unpack[TiktokMobileMusicChartDefaultParams]) -> TiktokMobileMusicChartResponse: ...
    @overload
    async def mobile_music_choices(self, **params: Unpack[TiktokMobileMusicChoicesStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_choices(self, **params: Unpack[TiktokMobileMusicChoicesTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_choices(self, **params: Unpack[TiktokMobileMusicChoicesDefaultParams]) -> TiktokMobileMusicChoicesResponse: ...
    @overload
    async def mobile_music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListDefaultParams]) -> TiktokMobileMusicCollectionListResponse: ...
    @overload
    async def mobile_music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsDefaultParams]) -> TiktokMobileMusicCollectionsResponse: ...
    @overload
    async def mobile_music_detail(self, **params: Unpack[TiktokMobileMusicDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_detail(self, **params: Unpack[TiktokMobileMusicDetailTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_detail(self, **params: Unpack[TiktokMobileMusicDetailDefaultParams]) -> TiktokMobileMusicDetailResponse: ...
    @overload
    async def mobile_music_pick(self, **params: Unpack[TiktokMobileMusicPickStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_pick(self, **params: Unpack[TiktokMobileMusicPickTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_pick(self, **params: Unpack[TiktokMobileMusicPickDefaultParams]) -> TiktokMobileMusicPickResponse: ...
    @overload
    async def mobile_music_posts(self, **params: Unpack[TiktokMobileMusicPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_posts(self, **params: Unpack[TiktokMobileMusicPostsTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_posts(self, **params: Unpack[TiktokMobileMusicPostsDefaultParams]) -> TiktokMobileMusicPostsResponse: ...
    @overload
    async def mobile_music_related(self, **params: Unpack[TiktokMobileMusicRelatedStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_related(self, **params: Unpack[TiktokMobileMusicRelatedTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_related(self, **params: Unpack[TiktokMobileMusicRelatedDefaultParams]) -> TiktokMobileMusicRelatedResponse: ...
    @overload
    async def mobile_music_trending(self, **params: Unpack[TiktokMobileMusicTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_trending(self, **params: Unpack[TiktokMobileMusicTrendingTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_trending(self, **params: Unpack[TiktokMobileMusicTrendingDefaultParams]) -> TiktokMobileMusicTrendingResponse: ...
    @overload
    async def mobile_mv_videos(self, **params: Unpack[TiktokMobileMvVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_mv_videos(self, **params: Unpack[TiktokMobileMvVideosTextResponseParams]) -> str: ...
    @overload
    async def mobile_mv_videos(self, **params: Unpack[TiktokMobileMvVideosDefaultParams]) -> TiktokMobileMvVideosResponse: ...
    @overload
    async def mobile_place_detail(self, **params: Unpack[TiktokMobilePlaceDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_place_detail(self, **params: Unpack[TiktokMobilePlaceDetailTextResponseParams]) -> str: ...
    @overload
    async def mobile_place_detail(self, **params: Unpack[TiktokMobilePlaceDetailDefaultParams]) -> TiktokMobilePlaceDetailResponse: ...
    @overload
    async def mobile_place_info(self, **params: Unpack[TiktokMobilePlaceInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_place_info(self, **params: Unpack[TiktokMobilePlaceInfoTextResponseParams]) -> str: ...
    @overload
    async def mobile_place_info(self, **params: Unpack[TiktokMobilePlaceInfoDefaultParams]) -> TiktokMobilePlaceInfoResponse: ...
    @overload
    async def mobile_place_media(self, **params: Unpack[TiktokMobilePlaceMediaStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_place_media(self, **params: Unpack[TiktokMobilePlaceMediaTextResponseParams]) -> str: ...
    @overload
    async def mobile_place_media(self, **params: Unpack[TiktokMobilePlaceMediaDefaultParams]) -> TiktokMobilePlaceMediaResponse: ...
    @overload
    async def mobile_place_photos(self, **params: Unpack[TiktokMobilePlacePhotosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_place_photos(self, **params: Unpack[TiktokMobilePlacePhotosTextResponseParams]) -> str: ...
    @overload
    async def mobile_place_photos(self, **params: Unpack[TiktokMobilePlacePhotosDefaultParams]) -> TiktokMobilePlacePhotosResponse: ...
    @overload
    async def mobile_place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsTextResponseParams]) -> str: ...
    @overload
    async def mobile_place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsDefaultParams]) -> TiktokMobilePlaceReviewsResponse: ...
    @overload
    async def mobile_place_videos(self, **params: Unpack[TiktokMobilePlaceVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_place_videos(self, **params: Unpack[TiktokMobilePlaceVideosTextResponseParams]) -> str: ...
    @overload
    async def mobile_place_videos(self, **params: Unpack[TiktokMobilePlaceVideosDefaultParams]) -> TiktokMobilePlaceVideosResponse: ...
    @overload
    async def mobile_playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailTextResponseParams]) -> str: ...
    @overload
    async def mobile_playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailDefaultParams]) -> TiktokMobilePlaylistDetailResponse: ...
    @overload
    async def mobile_playlist_list(self, **params: Unpack[TiktokMobilePlaylistListStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_playlist_list(self, **params: Unpack[TiktokMobilePlaylistListTextResponseParams]) -> str: ...
    @overload
    async def mobile_playlist_list(self, **params: Unpack[TiktokMobilePlaylistListDefaultParams]) -> TiktokMobilePlaylistListResponse: ...
    @overload
    async def mobile_playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosTextResponseParams]) -> str: ...
    @overload
    async def mobile_playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosDefaultParams]) -> TiktokMobilePlaylistVideosResponse: ...
    @overload
    async def mobile_search(self, **params: Unpack[TiktokMobileSearchResponseStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search(self, **params: Unpack[TiktokMobileSearchTextResponseParams]) -> str: ...
    @overload
    async def mobile_search(self, **params: Unpack[TiktokMobileSearchDefaultParams]) -> TiktokMobileSearchResponse: ...
    @overload
    async def mobile_search_effects(self, **params: Unpack[TiktokMobileSearchEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_effects(self, **params: Unpack[TiktokMobileSearchEffectsTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_effects(self, **params: Unpack[TiktokMobileSearchEffectsDefaultParams]) -> TiktokMobileSearchEffectsResponse: ...
    @overload
    async def mobile_search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsDefaultParams]) -> TiktokMobileSearchHashtagsResponse: ...
    @overload
    async def mobile_search_music(self, **params: Unpack[TiktokMobileSearchMusicStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_music(self, **params: Unpack[TiktokMobileSearchMusicTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_music(self, **params: Unpack[TiktokMobileSearchMusicDefaultParams]) -> TiktokMobileSearchMusicResponse: ...
    @overload
    async def mobile_search_photos(self, **params: Unpack[TiktokMobileSearchPhotosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_photos(self, **params: Unpack[TiktokMobileSearchPhotosTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_photos(self, **params: Unpack[TiktokMobileSearchPhotosDefaultParams]) -> TiktokMobileSearchPhotosResponse: ...
    @overload
    async def mobile_search_place(self, **params: Unpack[TiktokMobileSearchPlaceStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_place(self, **params: Unpack[TiktokMobileSearchPlaceTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_place(self, **params: Unpack[TiktokMobileSearchPlaceDefaultParams]) -> TiktokMobileSearchPlaceResponse: ...
    @overload
    async def mobile_search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoDefaultParams]) -> TiktokMobileSearchPreInfoResponse: ...
    @overload
    async def mobile_search_stream(self, **params: Unpack[TiktokMobileSearchStreamStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_stream(self, **params: Unpack[TiktokMobileSearchStreamTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_stream(self, **params: Unpack[TiktokMobileSearchStreamDefaultParams]) -> TiktokMobileSearchStreamResponse: ...
    @overload
    async def mobile_search_sug(self, **params: Unpack[TiktokMobileSearchSugStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_sug(self, **params: Unpack[TiktokMobileSearchSugTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_sug(self, **params: Unpack[TiktokMobileSearchSugDefaultParams]) -> TiktokMobileSearchSugResponse: ...
    @overload
    async def mobile_search_tabs(self, **params: Unpack[TiktokMobileSearchTabsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_tabs(self, **params: Unpack[TiktokMobileSearchTabsTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_tabs(self, **params: Unpack[TiktokMobileSearchTabsDefaultParams]) -> TiktokMobileSearchTabsResponse: ...
    @overload
    async def mobile_search_user(self, **params: Unpack[TiktokMobileSearchUserStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_user(self, **params: Unpack[TiktokMobileSearchUserTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_user(self, **params: Unpack[TiktokMobileSearchUserDefaultParams]) -> TiktokMobileSearchUserResponse: ...
    @overload
    async def mobile_search_videos(self, **params: Unpack[TiktokMobileSearchVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_videos(self, **params: Unpack[TiktokMobileSearchVideosTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_videos(self, **params: Unpack[TiktokMobileSearchVideosDefaultParams]) -> TiktokMobileSearchVideosResponse: ...
    @overload
    async def mobile_translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionTextResponseParams]) -> str: ...
    @overload
    async def mobile_translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionDefaultParams]) -> TiktokMobileTranslationDescriptionResponse: ...
    @overload
    async def mobile_trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesTextResponseParams]) -> str: ...
    @overload
    async def mobile_trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesDefaultParams]) -> TiktokMobileTrendingCategoriesResponse: ...
    @overload
    async def mobile_trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsTextResponseParams]) -> str: ...
    @overload
    async def mobile_trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsDefaultParams]) -> TiktokMobileTrendingEffectsResponse: ...
    @overload
    async def mobile_user_followers(self, **params: Unpack[TiktokMobileUserFollowersStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_followers(self, **params: Unpack[TiktokMobileUserFollowersTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_followers(self, **params: Unpack[TiktokMobileUserFollowersDefaultParams]) -> TiktokMobileUserFollowersResponse: ...
    @overload
    async def mobile_user_following(self, **params: Unpack[TiktokMobileUserFollowingStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_following(self, **params: Unpack[TiktokMobileUserFollowingTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_following(self, **params: Unpack[TiktokMobileUserFollowingDefaultParams]) -> TiktokMobileUserFollowingResponse: ...
    @overload
    async def mobile_user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsDefaultParams]) -> TiktokMobileUserOriginalEffectsResponse: ...
    @overload
    async def mobile_user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicDefaultParams]) -> TiktokMobileUserOriginalMusicResponse: ...
    @overload
    async def mobile_user_posts(self, **params: Unpack[TiktokMobileUserPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_posts(self, **params: Unpack[TiktokMobileUserPostsTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_posts(self, **params: Unpack[TiktokMobileUserPostsDefaultParams]) -> TiktokMobileUserPostsResponse: ...
    @overload
    async def mobile_user_profile(self, **params: Unpack[TiktokMobileUserProfileStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_profile(self, **params: Unpack[TiktokMobileUserProfileTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_profile(self, **params: Unpack[TiktokMobileUserProfileDefaultParams]) -> TiktokMobileUserProfileResponse: ...
    @overload
    async def mobile_user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsDefaultParams]) -> TiktokMobileUserRecommendationsResponse: ...
    @overload
    async def mobile_video_detail(self, **params: Unpack[TiktokMobileVideoDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_video_detail(self, **params: Unpack[TiktokMobileVideoDetailTextResponseParams]) -> str: ...
    @overload
    async def mobile_video_detail(self, **params: Unpack[TiktokMobileVideoDetailDefaultParams]) -> TiktokMobileVideoDetailResponse: ...
    @overload
    async def mobile_video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesTextResponseParams]) -> str: ...
    @overload
    async def mobile_video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesDefaultParams]) -> TiktokMobileVideoSubtitlesResponse: ...
    @overload
    async def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaStreamParams]) -> BinaryIO: ...
    @overload
    async def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaTextResponseParams]) -> str: ...
    @overload
    async def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaDefaultParams]) -> TiktokPopularTrendCountryIndustryMetaResponse: ...
    @overload
    async def post(self, **params: Unpack[TiktokPostStreamParams]) -> BinaryIO: ...
    @overload
    async def post(self, **params: Unpack[TiktokPostTextResponseParams]) -> str: ...
    @overload
    async def post(self, **params: Unpack[TiktokPostDefaultParams]) -> TiktokPostResponse: ...
    @overload
    async def profile_post(self, **params: Unpack[TiktokProfilePostStreamParams]) -> BinaryIO: ...
    @overload
    async def profile_post(self, **params: Unpack[TiktokProfilePostTextResponseParams]) -> str: ...
    @overload
    async def profile_post(self, **params: Unpack[TiktokProfilePostDefaultParams]) -> TiktokProfilePostResponse: ...
    @overload
    async def profile(self, **params: Unpack[TiktokProfileStreamParams]) -> BinaryIO: ...
    @overload
    async def profile(self, **params: Unpack[TiktokProfileTextResponseParams]) -> str: ...
    @overload
    async def profile(self, **params: Unpack[TiktokProfileDefaultParams]) -> TiktokProfileResponse: ...
    @overload
    async def search(self, **params: Unpack[TiktokSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[TiktokSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[TiktokSearchDefaultParams]) -> TiktokSearchResponse: ...
    @overload
    async def search_hashtag(self, **params: Unpack[TiktokSearchHashtagStreamParams]) -> BinaryIO: ...
    @overload
    async def search_hashtag(self, **params: Unpack[TiktokSearchHashtagTextResponseParams]) -> str: ...
    @overload
    async def search_hashtag(self, **params: Unpack[TiktokSearchHashtagDefaultParams]) -> TiktokSearchHashtagResponse: ...
    @overload
    async def search_user(self, **params: Unpack[TiktokSearchUserStreamParams]) -> BinaryIO: ...
    @overload
    async def search_user(self, **params: Unpack[TiktokSearchUserTextResponseParams]) -> str: ...
    @overload
    async def search_user(self, **params: Unpack[TiktokSearchUserDefaultParams]) -> TiktokSearchUserResponse: ...
    @overload
    async def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisTextResponseParams]) -> str: ...
    @overload
    async def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisDefaultParams]) -> TiktokTopAdsAnalysisResponse: ...
    @overload
    async def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailTextResponseParams]) -> str: ...
    @overload
    async def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailDefaultParams]) -> TiktokTopAdsDetailResponse: ...
    @overload
    async def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersTextResponseParams]) -> str: ...
    @overload
    async def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersDefaultParams]) -> TiktokTopAdsFiltersResponse: ...
    @overload
    async def top_ads_list(self, **params: Unpack[TiktokTopAdsListStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_list(self, **params: Unpack[TiktokTopAdsListTextResponseParams]) -> str: ...
    @overload
    async def top_ads_list(self, **params: Unpack[TiktokTopAdsListDefaultParams]) -> TiktokTopAdsListResponse: ...
    @overload
    async def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoTextResponseParams]) -> str: ...
    @overload
    async def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoDefaultParams]) -> TiktokTopAdsLocationInfoResponse: ...
    @overload
    async def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsTextResponseParams]) -> str: ...
    @overload
    async def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsDefaultParams]) -> TiktokTopAdsLocationsResponse: ...
    @overload
    async def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendTextResponseParams]) -> str: ...
    @overload
    async def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendDefaultParams]) -> TiktokTopAdsRecommendResponse: ...
    @overload
    async def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyTextResponseParams]) -> str: ...
    @overload
    async def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyDefaultParams]) -> TiktokTopAdsSafetyResponse: ...
    @overload
    async def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightTextResponseParams]) -> str: ...
    @overload
    async def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightDefaultParams]) -> TiktokTopAdsSpotlightResponse: ...
    @overload
    async def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsTextResponseParams]) -> str: ...
    @overload
    async def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsDefaultParams]) -> TiktokTopAdsSuggestionsResponse: ...
    @overload
    async def trending(self, **params: Unpack[TiktokTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def trending(self, **params: Unpack[TiktokTrendingTextResponseParams]) -> str: ...
    @overload
    async def trending(self, **params: Unpack[TiktokTrendingDefaultParams]) -> TiktokTrendingResponse: ...

class _AsyncTiktokGroup:
    @overload
    async def category(self, **params: Unpack[TiktokCategoryStreamParams]) -> BinaryIO: ...
    @overload
    async def category(self, **params: Unpack[TiktokCategoryTextResponseParams]) -> str: ...
    @overload
    async def category(self, **params: Unpack[TiktokCategoryDefaultParams]) -> TiktokCategoryResponse: ...
    @overload
    async def video_comments(self, **params: Unpack[TiktokVideoCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def video_comments(self, **params: Unpack[TiktokVideoCommentsTextResponseParams]) -> str: ...
    @overload
    async def video_comments(self, **params: Unpack[TiktokVideoCommentsDefaultParams]) -> TiktokVideoCommentsResponse: ...
    @overload
    async def creative_center_filters(self, **params: Unpack[TiktokCreativeCenterFiltersStreamParams]) -> BinaryIO: ...
    @overload
    async def creative_center_filters(self, **params: Unpack[TiktokCreativeCenterFiltersTextResponseParams]) -> str: ...
    @overload
    async def creative_center_filters(self, **params: Unpack[TiktokCreativeCenterFiltersDefaultParams]) -> TiktokCreativeCenterFiltersResponse: ...
    @overload
    async def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsTextResponseParams]) -> str: ...
    @overload
    async def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsDefaultParams]) -> TiktokCreativeCenterHashtagsResponse: ...
    @overload
    async def creative_center_top_content(self, **params: Unpack[TiktokCreativeCenterTopContentStreamParams]) -> BinaryIO: ...
    @overload
    async def creative_center_top_content(self, **params: Unpack[TiktokCreativeCenterTopContentTextResponseParams]) -> str: ...
    @overload
    async def creative_center_top_content(self, **params: Unpack[TiktokCreativeCenterTopContentDefaultParams]) -> TiktokCreativeCenterTopContentResponse: ...
    @overload
    async def creative_center_videos(self, **params: Unpack[TiktokCreativeCenterVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def creative_center_videos(self, **params: Unpack[TiktokCreativeCenterVideosTextResponseParams]) -> str: ...
    @overload
    async def creative_center_videos(self, **params: Unpack[TiktokCreativeCenterVideosDefaultParams]) -> TiktokCreativeCenterVideosResponse: ...
    @overload
    async def explore(self, **params: Unpack[TiktokExploreStreamParams]) -> BinaryIO: ...
    @overload
    async def explore(self, **params: Unpack[TiktokExploreTextResponseParams]) -> str: ...
    @overload
    async def explore(self, **params: Unpack[TiktokExploreDefaultParams]) -> TiktokExploreResponse: ...
    @overload
    async def challenge(self, **params: Unpack[TiktokChallengeStreamParams]) -> BinaryIO: ...
    @overload
    async def challenge(self, **params: Unpack[TiktokChallengeTextResponseParams]) -> str: ...
    @overload
    async def challenge(self, **params: Unpack[TiktokChallengeDefaultParams]) -> TiktokChallengeResponse: ...
    @overload
    async def challenge_list(self, **params: Unpack[TiktokChallengeListStreamParams]) -> BinaryIO: ...
    @overload
    async def challenge_list(self, **params: Unpack[TiktokChallengeListTextResponseParams]) -> str: ...
    @overload
    async def challenge_list(self, **params: Unpack[TiktokChallengeListDefaultParams]) -> TiktokChallengeListResponse: ...
    @overload
    async def mobile_anchor_list(self, **params: Unpack[TiktokMobileAnchorListStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_anchor_list(self, **params: Unpack[TiktokMobileAnchorListTextResponseParams]) -> str: ...
    @overload
    async def mobile_anchor_list(self, **params: Unpack[TiktokMobileAnchorListDefaultParams]) -> TiktokMobileAnchorListResponse: ...
    @overload
    async def mobile_collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailTextResponseParams]) -> str: ...
    @overload
    async def mobile_collection_detail(self, **params: Unpack[TiktokMobileCollectionDetailDefaultParams]) -> TiktokMobileCollectionDetailResponse: ...
    @overload
    async def mobile_collection_list(self, **params: Unpack[TiktokMobileCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_collection_list(self, **params: Unpack[TiktokMobileCollectionListTextResponseParams]) -> str: ...
    @overload
    async def mobile_collection_list(self, **params: Unpack[TiktokMobileCollectionListDefaultParams]) -> TiktokMobileCollectionListResponse: ...
    @overload
    async def mobile_collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosTextResponseParams]) -> str: ...
    @overload
    async def mobile_collection_videos(self, **params: Unpack[TiktokMobileCollectionVideosDefaultParams]) -> TiktokMobileCollectionVideosResponse: ...
    @overload
    async def mobile_comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesTextResponseParams]) -> str: ...
    @overload
    async def mobile_comment_replies(self, **params: Unpack[TiktokMobileCommentRepliesDefaultParams]) -> TiktokMobileCommentRepliesResponse: ...
    @overload
    async def mobile_comments(self, **params: Unpack[TiktokMobileCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_comments(self, **params: Unpack[TiktokMobileCommentsTextResponseParams]) -> str: ...
    @overload
    async def mobile_comments(self, **params: Unpack[TiktokMobileCommentsDefaultParams]) -> TiktokMobileCommentsResponse: ...
    @overload
    async def mobile_feed(self, **params: Unpack[TiktokMobileFeedStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_feed(self, **params: Unpack[TiktokMobileFeedTextResponseParams]) -> str: ...
    @overload
    async def mobile_feed(self, **params: Unpack[TiktokMobileFeedDefaultParams]) -> TiktokMobileFeedResponse: ...
    @overload
    async def mobile_feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineTextResponseParams]) -> str: ...
    @overload
    async def mobile_feed_offline(self, **params: Unpack[TiktokMobileFeedOfflineDefaultParams]) -> TiktokMobileFeedOfflineResponse: ...
    @overload
    async def mobile_feed_post(self, **params: Unpack[TiktokMobileFeedPostStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_feed_post(self, **params: Unpack[TiktokMobileFeedPostTextResponseParams]) -> str: ...
    @overload
    async def mobile_feed_post(self, **params: Unpack[TiktokMobileFeedPostDefaultParams]) -> TiktokMobileFeedPostResponse: ...
    @overload
    async def mobile_hashtag(self, **params: Unpack[TiktokMobileHashtagStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_hashtag(self, **params: Unpack[TiktokMobileHashtagTextResponseParams]) -> str: ...
    @overload
    async def mobile_hashtag(self, **params: Unpack[TiktokMobileHashtagDefaultParams]) -> TiktokMobileHashtagResponse: ...
    @overload
    async def mobile_hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsTextResponseParams]) -> str: ...
    @overload
    async def mobile_hashtag_posts(self, **params: Unpack[TiktokMobileHashtagPostsDefaultParams]) -> TiktokMobileHashtagPostsResponse: ...
    @overload
    async def mobile_hashtags(self, **params: Unpack[TiktokMobileHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_hashtags(self, **params: Unpack[TiktokMobileHashtagsTextResponseParams]) -> str: ...
    @overload
    async def mobile_hashtags(self, **params: Unpack[TiktokMobileHashtagsDefaultParams]) -> TiktokMobileHashtagsResponse: ...
    @overload
    async def mobile_live_effects(self, **params: Unpack[TiktokMobileLiveEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_effects(self, **params: Unpack[TiktokMobileLiveEffectsTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_effects(self, **params: Unpack[TiktokMobileLiveEffectsDefaultParams]) -> TiktokMobileLiveEffectsResponse: ...
    @overload
    async def mobile_live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_gifts(self, **params: Unpack[TiktokMobileLiveGiftsDefaultParams]) -> TiktokMobileLiveGiftsResponse: ...
    @overload
    async def mobile_live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_hashtags(self, **params: Unpack[TiktokMobileLiveHashtagsDefaultParams]) -> TiktokMobileLiveHashtagsResponse: ...
    @overload
    async def mobile_live_room(self, **params: Unpack[TiktokMobileLiveRoomStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_room(self, **params: Unpack[TiktokMobileLiveRoomTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_room(self, **params: Unpack[TiktokMobileLiveRoomDefaultParams]) -> TiktokMobileLiveRoomResponse: ...
    @overload
    async def mobile_live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_room_by_user(self, **params: Unpack[TiktokMobileLiveRoomByUserDefaultParams]) -> TiktokMobileLiveRoomByUserResponse: ...
    @overload
    async def mobile_live_search(self, **params: Unpack[TiktokMobileLiveSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_search(self, **params: Unpack[TiktokMobileLiveSearchTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_search(self, **params: Unpack[TiktokMobileLiveSearchDefaultParams]) -> TiktokMobileLiveSearchResponse: ...
    @overload
    async def mobile_live_tabs(self, **params: Unpack[TiktokMobileLiveTabsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_live_tabs(self, **params: Unpack[TiktokMobileLiveTabsTextResponseParams]) -> str: ...
    @overload
    async def mobile_live_tabs(self, **params: Unpack[TiktokMobileLiveTabsDefaultParams]) -> TiktokMobileLiveTabsResponse: ...
    @overload
    async def mobile_music_beats(self, **params: Unpack[TiktokMobileMusicBeatsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_beats(self, **params: Unpack[TiktokMobileMusicBeatsTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_beats(self, **params: Unpack[TiktokMobileMusicBeatsDefaultParams]) -> TiktokMobileMusicBeatsResponse: ...
    @overload
    async def mobile_music_chart(self, **params: Unpack[TiktokMobileMusicChartStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_chart(self, **params: Unpack[TiktokMobileMusicChartTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_chart(self, **params: Unpack[TiktokMobileMusicChartDefaultParams]) -> TiktokMobileMusicChartResponse: ...
    @overload
    async def mobile_music_choices(self, **params: Unpack[TiktokMobileMusicChoicesStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_choices(self, **params: Unpack[TiktokMobileMusicChoicesTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_choices(self, **params: Unpack[TiktokMobileMusicChoicesDefaultParams]) -> TiktokMobileMusicChoicesResponse: ...
    @overload
    async def mobile_music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_collection_list(self, **params: Unpack[TiktokMobileMusicCollectionListDefaultParams]) -> TiktokMobileMusicCollectionListResponse: ...
    @overload
    async def mobile_music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_collections(self, **params: Unpack[TiktokMobileMusicCollectionsDefaultParams]) -> TiktokMobileMusicCollectionsResponse: ...
    @overload
    async def mobile_music_detail(self, **params: Unpack[TiktokMobileMusicDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_detail(self, **params: Unpack[TiktokMobileMusicDetailTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_detail(self, **params: Unpack[TiktokMobileMusicDetailDefaultParams]) -> TiktokMobileMusicDetailResponse: ...
    @overload
    async def mobile_music_pick(self, **params: Unpack[TiktokMobileMusicPickStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_pick(self, **params: Unpack[TiktokMobileMusicPickTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_pick(self, **params: Unpack[TiktokMobileMusicPickDefaultParams]) -> TiktokMobileMusicPickResponse: ...
    @overload
    async def mobile_music_posts(self, **params: Unpack[TiktokMobileMusicPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_posts(self, **params: Unpack[TiktokMobileMusicPostsTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_posts(self, **params: Unpack[TiktokMobileMusicPostsDefaultParams]) -> TiktokMobileMusicPostsResponse: ...
    @overload
    async def mobile_music_related(self, **params: Unpack[TiktokMobileMusicRelatedStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_related(self, **params: Unpack[TiktokMobileMusicRelatedTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_related(self, **params: Unpack[TiktokMobileMusicRelatedDefaultParams]) -> TiktokMobileMusicRelatedResponse: ...
    @overload
    async def mobile_music_trending(self, **params: Unpack[TiktokMobileMusicTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_music_trending(self, **params: Unpack[TiktokMobileMusicTrendingTextResponseParams]) -> str: ...
    @overload
    async def mobile_music_trending(self, **params: Unpack[TiktokMobileMusicTrendingDefaultParams]) -> TiktokMobileMusicTrendingResponse: ...
    @overload
    async def mobile_mv_videos(self, **params: Unpack[TiktokMobileMvVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_mv_videos(self, **params: Unpack[TiktokMobileMvVideosTextResponseParams]) -> str: ...
    @overload
    async def mobile_mv_videos(self, **params: Unpack[TiktokMobileMvVideosDefaultParams]) -> TiktokMobileMvVideosResponse: ...
    @overload
    async def mobile_place_detail(self, **params: Unpack[TiktokMobilePlaceDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_place_detail(self, **params: Unpack[TiktokMobilePlaceDetailTextResponseParams]) -> str: ...
    @overload
    async def mobile_place_detail(self, **params: Unpack[TiktokMobilePlaceDetailDefaultParams]) -> TiktokMobilePlaceDetailResponse: ...
    @overload
    async def mobile_place_info(self, **params: Unpack[TiktokMobilePlaceInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_place_info(self, **params: Unpack[TiktokMobilePlaceInfoTextResponseParams]) -> str: ...
    @overload
    async def mobile_place_info(self, **params: Unpack[TiktokMobilePlaceInfoDefaultParams]) -> TiktokMobilePlaceInfoResponse: ...
    @overload
    async def mobile_place_media(self, **params: Unpack[TiktokMobilePlaceMediaStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_place_media(self, **params: Unpack[TiktokMobilePlaceMediaTextResponseParams]) -> str: ...
    @overload
    async def mobile_place_media(self, **params: Unpack[TiktokMobilePlaceMediaDefaultParams]) -> TiktokMobilePlaceMediaResponse: ...
    @overload
    async def mobile_place_photos(self, **params: Unpack[TiktokMobilePlacePhotosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_place_photos(self, **params: Unpack[TiktokMobilePlacePhotosTextResponseParams]) -> str: ...
    @overload
    async def mobile_place_photos(self, **params: Unpack[TiktokMobilePlacePhotosDefaultParams]) -> TiktokMobilePlacePhotosResponse: ...
    @overload
    async def mobile_place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsTextResponseParams]) -> str: ...
    @overload
    async def mobile_place_reviews(self, **params: Unpack[TiktokMobilePlaceReviewsDefaultParams]) -> TiktokMobilePlaceReviewsResponse: ...
    @overload
    async def mobile_place_videos(self, **params: Unpack[TiktokMobilePlaceVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_place_videos(self, **params: Unpack[TiktokMobilePlaceVideosTextResponseParams]) -> str: ...
    @overload
    async def mobile_place_videos(self, **params: Unpack[TiktokMobilePlaceVideosDefaultParams]) -> TiktokMobilePlaceVideosResponse: ...
    @overload
    async def mobile_playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailTextResponseParams]) -> str: ...
    @overload
    async def mobile_playlist_detail(self, **params: Unpack[TiktokMobilePlaylistDetailDefaultParams]) -> TiktokMobilePlaylistDetailResponse: ...
    @overload
    async def mobile_playlist_list(self, **params: Unpack[TiktokMobilePlaylistListStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_playlist_list(self, **params: Unpack[TiktokMobilePlaylistListTextResponseParams]) -> str: ...
    @overload
    async def mobile_playlist_list(self, **params: Unpack[TiktokMobilePlaylistListDefaultParams]) -> TiktokMobilePlaylistListResponse: ...
    @overload
    async def mobile_playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosTextResponseParams]) -> str: ...
    @overload
    async def mobile_playlist_videos(self, **params: Unpack[TiktokMobilePlaylistVideosDefaultParams]) -> TiktokMobilePlaylistVideosResponse: ...
    @overload
    async def mobile_search(self, **params: Unpack[TiktokMobileSearchResponseStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search(self, **params: Unpack[TiktokMobileSearchTextResponseParams]) -> str: ...
    @overload
    async def mobile_search(self, **params: Unpack[TiktokMobileSearchDefaultParams]) -> TiktokMobileSearchResponse: ...
    @overload
    async def mobile_search_effects(self, **params: Unpack[TiktokMobileSearchEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_effects(self, **params: Unpack[TiktokMobileSearchEffectsTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_effects(self, **params: Unpack[TiktokMobileSearchEffectsDefaultParams]) -> TiktokMobileSearchEffectsResponse: ...
    @overload
    async def mobile_search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_hashtags(self, **params: Unpack[TiktokMobileSearchHashtagsDefaultParams]) -> TiktokMobileSearchHashtagsResponse: ...
    @overload
    async def mobile_search_music(self, **params: Unpack[TiktokMobileSearchMusicStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_music(self, **params: Unpack[TiktokMobileSearchMusicTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_music(self, **params: Unpack[TiktokMobileSearchMusicDefaultParams]) -> TiktokMobileSearchMusicResponse: ...
    @overload
    async def mobile_search_photos(self, **params: Unpack[TiktokMobileSearchPhotosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_photos(self, **params: Unpack[TiktokMobileSearchPhotosTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_photos(self, **params: Unpack[TiktokMobileSearchPhotosDefaultParams]) -> TiktokMobileSearchPhotosResponse: ...
    @overload
    async def mobile_search_place(self, **params: Unpack[TiktokMobileSearchPlaceStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_place(self, **params: Unpack[TiktokMobileSearchPlaceTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_place(self, **params: Unpack[TiktokMobileSearchPlaceDefaultParams]) -> TiktokMobileSearchPlaceResponse: ...
    @overload
    async def mobile_search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_pre_info(self, **params: Unpack[TiktokMobileSearchPreInfoDefaultParams]) -> TiktokMobileSearchPreInfoResponse: ...
    @overload
    async def mobile_search_stream(self, **params: Unpack[TiktokMobileSearchStreamStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_stream(self, **params: Unpack[TiktokMobileSearchStreamTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_stream(self, **params: Unpack[TiktokMobileSearchStreamDefaultParams]) -> TiktokMobileSearchStreamResponse: ...
    @overload
    async def mobile_search_sug(self, **params: Unpack[TiktokMobileSearchSugStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_sug(self, **params: Unpack[TiktokMobileSearchSugTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_sug(self, **params: Unpack[TiktokMobileSearchSugDefaultParams]) -> TiktokMobileSearchSugResponse: ...
    @overload
    async def mobile_search_tabs(self, **params: Unpack[TiktokMobileSearchTabsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_tabs(self, **params: Unpack[TiktokMobileSearchTabsTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_tabs(self, **params: Unpack[TiktokMobileSearchTabsDefaultParams]) -> TiktokMobileSearchTabsResponse: ...
    @overload
    async def mobile_search_user(self, **params: Unpack[TiktokMobileSearchUserStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_user(self, **params: Unpack[TiktokMobileSearchUserTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_user(self, **params: Unpack[TiktokMobileSearchUserDefaultParams]) -> TiktokMobileSearchUserResponse: ...
    @overload
    async def mobile_search_videos(self, **params: Unpack[TiktokMobileSearchVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_search_videos(self, **params: Unpack[TiktokMobileSearchVideosTextResponseParams]) -> str: ...
    @overload
    async def mobile_search_videos(self, **params: Unpack[TiktokMobileSearchVideosDefaultParams]) -> TiktokMobileSearchVideosResponse: ...
    @overload
    async def mobile_translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionTextResponseParams]) -> str: ...
    @overload
    async def mobile_translation_description(self, **params: Unpack[TiktokMobileTranslationDescriptionDefaultParams]) -> TiktokMobileTranslationDescriptionResponse: ...
    @overload
    async def mobile_trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesTextResponseParams]) -> str: ...
    @overload
    async def mobile_trending_categories(self, **params: Unpack[TiktokMobileTrendingCategoriesDefaultParams]) -> TiktokMobileTrendingCategoriesResponse: ...
    @overload
    async def mobile_trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsTextResponseParams]) -> str: ...
    @overload
    async def mobile_trending_effects(self, **params: Unpack[TiktokMobileTrendingEffectsDefaultParams]) -> TiktokMobileTrendingEffectsResponse: ...
    @overload
    async def mobile_user_followers(self, **params: Unpack[TiktokMobileUserFollowersStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_followers(self, **params: Unpack[TiktokMobileUserFollowersTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_followers(self, **params: Unpack[TiktokMobileUserFollowersDefaultParams]) -> TiktokMobileUserFollowersResponse: ...
    @overload
    async def mobile_user_following(self, **params: Unpack[TiktokMobileUserFollowingStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_following(self, **params: Unpack[TiktokMobileUserFollowingTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_following(self, **params: Unpack[TiktokMobileUserFollowingDefaultParams]) -> TiktokMobileUserFollowingResponse: ...
    @overload
    async def mobile_user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_original_effects(self, **params: Unpack[TiktokMobileUserOriginalEffectsDefaultParams]) -> TiktokMobileUserOriginalEffectsResponse: ...
    @overload
    async def mobile_user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_original_music(self, **params: Unpack[TiktokMobileUserOriginalMusicDefaultParams]) -> TiktokMobileUserOriginalMusicResponse: ...
    @overload
    async def mobile_user_posts(self, **params: Unpack[TiktokMobileUserPostsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_posts(self, **params: Unpack[TiktokMobileUserPostsTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_posts(self, **params: Unpack[TiktokMobileUserPostsDefaultParams]) -> TiktokMobileUserPostsResponse: ...
    @overload
    async def mobile_user_profile(self, **params: Unpack[TiktokMobileUserProfileStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_profile(self, **params: Unpack[TiktokMobileUserProfileTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_profile(self, **params: Unpack[TiktokMobileUserProfileDefaultParams]) -> TiktokMobileUserProfileResponse: ...
    @overload
    async def mobile_user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsTextResponseParams]) -> str: ...
    @overload
    async def mobile_user_recommendations(self, **params: Unpack[TiktokMobileUserRecommendationsDefaultParams]) -> TiktokMobileUserRecommendationsResponse: ...
    @overload
    async def mobile_video_detail(self, **params: Unpack[TiktokMobileVideoDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_video_detail(self, **params: Unpack[TiktokMobileVideoDetailTextResponseParams]) -> str: ...
    @overload
    async def mobile_video_detail(self, **params: Unpack[TiktokMobileVideoDetailDefaultParams]) -> TiktokMobileVideoDetailResponse: ...
    @overload
    async def mobile_video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesStreamParams]) -> BinaryIO: ...
    @overload
    async def mobile_video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesTextResponseParams]) -> str: ...
    @overload
    async def mobile_video_subtitles(self, **params: Unpack[TiktokMobileVideoSubtitlesDefaultParams]) -> TiktokMobileVideoSubtitlesResponse: ...
    @overload
    async def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaStreamParams]) -> BinaryIO: ...
    @overload
    async def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaTextResponseParams]) -> str: ...
    @overload
    async def popular_trend_country_industry_meta(self, **params: Unpack[TiktokPopularTrendCountryIndustryMetaDefaultParams]) -> TiktokPopularTrendCountryIndustryMetaResponse: ...
    @overload
    async def post(self, **params: Unpack[TiktokPostStreamParams]) -> BinaryIO: ...
    @overload
    async def post(self, **params: Unpack[TiktokPostTextResponseParams]) -> str: ...
    @overload
    async def post(self, **params: Unpack[TiktokPostDefaultParams]) -> TiktokPostResponse: ...
    @overload
    async def profile_post(self, **params: Unpack[TiktokProfilePostStreamParams]) -> BinaryIO: ...
    @overload
    async def profile_post(self, **params: Unpack[TiktokProfilePostTextResponseParams]) -> str: ...
    @overload
    async def profile_post(self, **params: Unpack[TiktokProfilePostDefaultParams]) -> TiktokProfilePostResponse: ...
    @overload
    async def profile(self, **params: Unpack[TiktokProfileStreamParams]) -> BinaryIO: ...
    @overload
    async def profile(self, **params: Unpack[TiktokProfileTextResponseParams]) -> str: ...
    @overload
    async def profile(self, **params: Unpack[TiktokProfileDefaultParams]) -> TiktokProfileResponse: ...
    @overload
    async def search(self, **params: Unpack[TiktokSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[TiktokSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[TiktokSearchDefaultParams]) -> TiktokSearchResponse: ...
    @overload
    async def search_hashtag(self, **params: Unpack[TiktokSearchHashtagStreamParams]) -> BinaryIO: ...
    @overload
    async def search_hashtag(self, **params: Unpack[TiktokSearchHashtagTextResponseParams]) -> str: ...
    @overload
    async def search_hashtag(self, **params: Unpack[TiktokSearchHashtagDefaultParams]) -> TiktokSearchHashtagResponse: ...
    @overload
    async def search_user(self, **params: Unpack[TiktokSearchUserStreamParams]) -> BinaryIO: ...
    @overload
    async def search_user(self, **params: Unpack[TiktokSearchUserTextResponseParams]) -> str: ...
    @overload
    async def search_user(self, **params: Unpack[TiktokSearchUserDefaultParams]) -> TiktokSearchUserResponse: ...
    @overload
    async def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisTextResponseParams]) -> str: ...
    @overload
    async def top_ads_analysis(self, **params: Unpack[TiktokTopAdsAnalysisDefaultParams]) -> TiktokTopAdsAnalysisResponse: ...
    @overload
    async def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailTextResponseParams]) -> str: ...
    @overload
    async def top_ads_detail(self, **params: Unpack[TiktokTopAdsDetailDefaultParams]) -> TiktokTopAdsDetailResponse: ...
    @overload
    async def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersTextResponseParams]) -> str: ...
    @overload
    async def top_ads_filters(self, **params: Unpack[TiktokTopAdsFiltersDefaultParams]) -> TiktokTopAdsFiltersResponse: ...
    @overload
    async def top_ads_list(self, **params: Unpack[TiktokTopAdsListStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_list(self, **params: Unpack[TiktokTopAdsListTextResponseParams]) -> str: ...
    @overload
    async def top_ads_list(self, **params: Unpack[TiktokTopAdsListDefaultParams]) -> TiktokTopAdsListResponse: ...
    @overload
    async def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoTextResponseParams]) -> str: ...
    @overload
    async def top_ads_location_info(self, **params: Unpack[TiktokTopAdsLocationInfoDefaultParams]) -> TiktokTopAdsLocationInfoResponse: ...
    @overload
    async def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsTextResponseParams]) -> str: ...
    @overload
    async def top_ads_locations(self, **params: Unpack[TiktokTopAdsLocationsDefaultParams]) -> TiktokTopAdsLocationsResponse: ...
    @overload
    async def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendTextResponseParams]) -> str: ...
    @overload
    async def top_ads_recommend(self, **params: Unpack[TiktokTopAdsRecommendDefaultParams]) -> TiktokTopAdsRecommendResponse: ...
    @overload
    async def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyTextResponseParams]) -> str: ...
    @overload
    async def top_ads_safety(self, **params: Unpack[TiktokTopAdsSafetyDefaultParams]) -> TiktokTopAdsSafetyResponse: ...
    @overload
    async def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightTextResponseParams]) -> str: ...
    @overload
    async def top_ads_spotlight(self, **params: Unpack[TiktokTopAdsSpotlightDefaultParams]) -> TiktokTopAdsSpotlightResponse: ...
    @overload
    async def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsStreamParams]) -> BinaryIO: ...
    @overload
    async def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsTextResponseParams]) -> str: ...
    @overload
    async def top_ads_suggestions(self, **params: Unpack[TiktokTopAdsSuggestionsDefaultParams]) -> TiktokTopAdsSuggestionsResponse: ...
    @overload
    async def trending(self, **params: Unpack[TiktokTrendingStreamParams]) -> BinaryIO: ...
    @overload
    async def trending(self, **params: Unpack[TiktokTrendingTextResponseParams]) -> str: ...
    @overload
    async def trending(self, **params: Unpack[TiktokTrendingDefaultParams]) -> TiktokTrendingResponse: ...

TiktokCategoryDefaultParams = TypedDict('TiktokCategoryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokCategoryTextResponseParams = TypedDict('TiktokCategoryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokCategoryStreamParams = TypedDict('TiktokCategoryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokVideoCommentsDefaultParams = TypedDict('TiktokVideoCommentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokVideoCommentsTextResponseParams = TypedDict('TiktokVideoCommentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokVideoCommentsStreamParams = TypedDict('TiktokVideoCommentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokCreativeCenterFiltersDefaultParams = TypedDict('TiktokCreativeCenterFiltersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokCreativeCenterFiltersTextResponseParams = TypedDict('TiktokCreativeCenterFiltersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokCreativeCenterFiltersStreamParams = TypedDict('TiktokCreativeCenterFiltersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokCreativeCenterHashtagsDefaultParams = TypedDict('TiktokCreativeCenterHashtagsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30', '90']],
    'industry_id': NotRequired[Literal['10000000000', '11000000000', '12000000000', '13000000000', '14000000000', '15000000000', '17000000000', '18000000000', '19000000000', '21000000000', '22000000000', '23000000000', '24000000000', '25000000000', '26000000000', '27000000000', '28000000000', '29000000000']],
}, total=False)

TiktokCreativeCenterHashtagsTextResponseParams = TypedDict('TiktokCreativeCenterHashtagsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30', '90']],
    'industry_id': NotRequired[Literal['10000000000', '11000000000', '12000000000', '13000000000', '14000000000', '15000000000', '17000000000', '18000000000', '19000000000', '21000000000', '22000000000', '23000000000', '24000000000', '25000000000', '26000000000', '27000000000', '28000000000', '29000000000']],
}, total=False)

TiktokCreativeCenterHashtagsStreamParams = TypedDict('TiktokCreativeCenterHashtagsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30', '90']],
    'industry_id': NotRequired[Literal['10000000000', '11000000000', '12000000000', '13000000000', '14000000000', '15000000000', '17000000000', '18000000000', '19000000000', '21000000000', '22000000000', '23000000000', '24000000000', '25000000000', '26000000000', '27000000000', '28000000000', '29000000000']],
}, total=False)

TiktokCreativeCenterTopContentDefaultParams = TypedDict('TiktokCreativeCenterTopContentDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'include_comments': NotRequired[bool],
}, total=False)

TiktokCreativeCenterTopContentTextResponseParams = TypedDict('TiktokCreativeCenterTopContentTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'include_comments': NotRequired[bool],
}, total=False)

TiktokCreativeCenterTopContentStreamParams = TypedDict('TiktokCreativeCenterTopContentStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'include_comments': NotRequired[bool],
}, total=False)

TiktokCreativeCenterVideosDefaultParams = TypedDict('TiktokCreativeCenterVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30']],
    'sort_by': NotRequired[Literal['views', 'engagement', 'six_second_views']],
    'content_label_id': NotRequired[str],
    'content_label_ids': NotRequired[list[Literal['11002', '11003', '11010', '11013', '11015']]],
    'organic_only': NotRequired[bool],
}, total=False)

TiktokCreativeCenterVideosTextResponseParams = TypedDict('TiktokCreativeCenterVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30']],
    'sort_by': NotRequired[Literal['views', 'engagement', 'six_second_views']],
    'content_label_id': NotRequired[str],
    'content_label_ids': NotRequired[list[Literal['11002', '11003', '11010', '11013', '11015']]],
    'organic_only': NotRequired[bool],
}, total=False)

TiktokCreativeCenterVideosStreamParams = TypedDict('TiktokCreativeCenterVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30']],
    'sort_by': NotRequired[Literal['views', 'engagement', 'six_second_views']],
    'content_label_id': NotRequired[str],
    'content_label_ids': NotRequired[list[Literal['11002', '11003', '11010', '11013', '11015']]],
    'organic_only': NotRequired[bool],
}, total=False)

TiktokExploreDefaultParams = TypedDict('TiktokExploreDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[int],
}, total=False)

TiktokExploreTextResponseParams = TypedDict('TiktokExploreTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[int],
}, total=False)

TiktokExploreStreamParams = TypedDict('TiktokExploreStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[int],
}, total=False)

TiktokChallengeDefaultParams = TypedDict('TiktokChallengeDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'name': Required[str],
}, total=False)

TiktokChallengeTextResponseParams = TypedDict('TiktokChallengeTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'name': Required[str],
}, total=False)

TiktokChallengeStreamParams = TypedDict('TiktokChallengeStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'name': Required[str],
}, total=False)

TiktokChallengeListDefaultParams = TypedDict('TiktokChallengeListDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokChallengeListTextResponseParams = TypedDict('TiktokChallengeListTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokChallengeListStreamParams = TypedDict('TiktokChallengeListStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileAnchorListDefaultParams = TypedDict('TiktokMobileAnchorListDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileAnchorListTextResponseParams = TypedDict('TiktokMobileAnchorListTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileAnchorListStreamParams = TypedDict('TiktokMobileAnchorListStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileCollectionDetailDefaultParams = TypedDict('TiktokMobileCollectionDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'collection_id': Required[str],
}, total=False)

TiktokMobileCollectionDetailTextResponseParams = TypedDict('TiktokMobileCollectionDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'collection_id': Required[str],
}, total=False)

TiktokMobileCollectionDetailStreamParams = TypedDict('TiktokMobileCollectionDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'collection_id': Required[str],
}, total=False)

TiktokMobileCollectionListDefaultParams = TypedDict('TiktokMobileCollectionListDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCollectionListTextResponseParams = TypedDict('TiktokMobileCollectionListTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCollectionListStreamParams = TypedDict('TiktokMobileCollectionListStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCollectionVideosDefaultParams = TypedDict('TiktokMobileCollectionVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'collection_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCollectionVideosTextResponseParams = TypedDict('TiktokMobileCollectionVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'collection_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCollectionVideosStreamParams = TypedDict('TiktokMobileCollectionVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'collection_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentRepliesDefaultParams = TypedDict('TiktokMobileCommentRepliesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'aweme_id': Required[str],
    'comment_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentRepliesTextResponseParams = TypedDict('TiktokMobileCommentRepliesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'aweme_id': Required[str],
    'comment_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentRepliesStreamParams = TypedDict('TiktokMobileCommentRepliesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'aweme_id': Required[str],
    'comment_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentsDefaultParams = TypedDict('TiktokMobileCommentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentsTextResponseParams = TypedDict('TiktokMobileCommentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileCommentsStreamParams = TypedDict('TiktokMobileCommentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'aweme_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileFeedDefaultParams = TypedDict('TiktokMobileFeedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileFeedTextResponseParams = TypedDict('TiktokMobileFeedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileFeedStreamParams = TypedDict('TiktokMobileFeedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileFeedOfflineDefaultParams = TypedDict('TiktokMobileFeedOfflineDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'pull_type': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileFeedOfflineTextResponseParams = TypedDict('TiktokMobileFeedOfflineTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'pull_type': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileFeedOfflineStreamParams = TypedDict('TiktokMobileFeedOfflineStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'pull_type': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileFeedPostDefaultParams = TypedDict('TiktokMobileFeedPostDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileFeedPostTextResponseParams = TypedDict('TiktokMobileFeedPostTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileFeedPostStreamParams = TypedDict('TiktokMobileFeedPostStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileHashtagDefaultParams = TypedDict('TiktokMobileHashtagDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'name': Required[str],
}, total=False)

TiktokMobileHashtagTextResponseParams = TypedDict('TiktokMobileHashtagTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'name': Required[str],
}, total=False)

TiktokMobileHashtagStreamParams = TypedDict('TiktokMobileHashtagStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'name': Required[str],
}, total=False)

TiktokMobileHashtagPostsDefaultParams = TypedDict('TiktokMobileHashtagPostsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'name': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileHashtagPostsTextResponseParams = TypedDict('TiktokMobileHashtagPostsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'name': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileHashtagPostsStreamParams = TypedDict('TiktokMobileHashtagPostsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'name': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileHashtagsDefaultParams = TypedDict('TiktokMobileHashtagsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileHashtagsTextResponseParams = TypedDict('TiktokMobileHashtagsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileHashtagsStreamParams = TypedDict('TiktokMobileHashtagsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileLiveEffectsDefaultParams = TypedDict('TiktokMobileLiveEffectsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileLiveEffectsTextResponseParams = TypedDict('TiktokMobileLiveEffectsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileLiveEffectsStreamParams = TypedDict('TiktokMobileLiveEffectsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileLiveGiftsDefaultParams = TypedDict('TiktokMobileLiveGiftsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileLiveGiftsTextResponseParams = TypedDict('TiktokMobileLiveGiftsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileLiveGiftsStreamParams = TypedDict('TiktokMobileLiveGiftsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileLiveHashtagsDefaultParams = TypedDict('TiktokMobileLiveHashtagsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileLiveHashtagsTextResponseParams = TypedDict('TiktokMobileLiveHashtagsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileLiveHashtagsStreamParams = TypedDict('TiktokMobileLiveHashtagsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileLiveRoomDefaultParams = TypedDict('TiktokMobileLiveRoomDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'room_id': Required[str],
}, total=False)

TiktokMobileLiveRoomTextResponseParams = TypedDict('TiktokMobileLiveRoomTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'room_id': Required[str],
}, total=False)

TiktokMobileLiveRoomStreamParams = TypedDict('TiktokMobileLiveRoomStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'room_id': Required[str],
}, total=False)

TiktokMobileLiveRoomByUserDefaultParams = TypedDict('TiktokMobileLiveRoomByUserDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
}, total=False)

TiktokMobileLiveRoomByUserTextResponseParams = TypedDict('TiktokMobileLiveRoomByUserTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
}, total=False)

TiktokMobileLiveRoomByUserStreamParams = TypedDict('TiktokMobileLiveRoomByUserStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
}, total=False)

TiktokMobileLiveSearchDefaultParams = TypedDict('TiktokMobileLiveSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileLiveSearchTextResponseParams = TypedDict('TiktokMobileLiveSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileLiveSearchStreamParams = TypedDict('TiktokMobileLiveSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileLiveTabsDefaultParams = TypedDict('TiktokMobileLiveTabsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileLiveTabsTextResponseParams = TypedDict('TiktokMobileLiveTabsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileLiveTabsStreamParams = TypedDict('TiktokMobileLiveTabsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileMusicBeatsDefaultParams = TypedDict('TiktokMobileMusicBeatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicBeatsTextResponseParams = TypedDict('TiktokMobileMusicBeatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicBeatsStreamParams = TypedDict('TiktokMobileMusicBeatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicChartDefaultParams = TypedDict('TiktokMobileMusicChartDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'chart_region': NotRequired[Literal['AE', 'BR', 'CA', 'DE', 'EG', 'FR', 'JP', 'KR', 'LB', 'MX', 'NG', 'SA', 'TR', 'US', 'ZA']],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicChartTextResponseParams = TypedDict('TiktokMobileMusicChartTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'chart_region': NotRequired[Literal['AE', 'BR', 'CA', 'DE', 'EG', 'FR', 'JP', 'KR', 'LB', 'MX', 'NG', 'SA', 'TR', 'US', 'ZA']],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicChartStreamParams = TypedDict('TiktokMobileMusicChartStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'chart_region': NotRequired[Literal['AE', 'BR', 'CA', 'DE', 'EG', 'FR', 'JP', 'KR', 'LB', 'MX', 'NG', 'SA', 'TR', 'US', 'ZA']],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileMusicChoicesDefaultParams = TypedDict('TiktokMobileMusicChoicesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokMobileMusicChoicesTextResponseParams = TypedDict('TiktokMobileMusicChoicesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokMobileMusicChoicesStreamParams = TypedDict('TiktokMobileMusicChoicesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokMobileMusicCollectionListDefaultParams = TypedDict('TiktokMobileMusicCollectionListDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicCollectionListTextResponseParams = TypedDict('TiktokMobileMusicCollectionListTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicCollectionListStreamParams = TypedDict('TiktokMobileMusicCollectionListStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicCollectionsDefaultParams = TypedDict('TiktokMobileMusicCollectionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicCollectionsTextResponseParams = TypedDict('TiktokMobileMusicCollectionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicCollectionsStreamParams = TypedDict('TiktokMobileMusicCollectionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicDetailDefaultParams = TypedDict('TiktokMobileMusicDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'music_id': Required[str],
}, total=False)

TiktokMobileMusicDetailTextResponseParams = TypedDict('TiktokMobileMusicDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'music_id': Required[str],
}, total=False)

TiktokMobileMusicDetailStreamParams = TypedDict('TiktokMobileMusicDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'music_id': Required[str],
}, total=False)

TiktokMobileMusicPickDefaultParams = TypedDict('TiktokMobileMusicPickDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicPickTextResponseParams = TypedDict('TiktokMobileMusicPickTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicPickStreamParams = TypedDict('TiktokMobileMusicPickStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicPostsDefaultParams = TypedDict('TiktokMobileMusicPostsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'music_id': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicPostsTextResponseParams = TypedDict('TiktokMobileMusicPostsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'music_id': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicPostsStreamParams = TypedDict('TiktokMobileMusicPostsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'music_id': Required[str],
    'sort': NotRequired[Literal['fresh', 'popular']],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicRelatedDefaultParams = TypedDict('TiktokMobileMusicRelatedDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'aweme_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicRelatedTextResponseParams = TypedDict('TiktokMobileMusicRelatedTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'aweme_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicRelatedStreamParams = TypedDict('TiktokMobileMusicRelatedStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'aweme_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicTrendingDefaultParams = TypedDict('TiktokMobileMusicTrendingDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicTrendingTextResponseParams = TypedDict('TiktokMobileMusicTrendingTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMusicTrendingStreamParams = TypedDict('TiktokMobileMusicTrendingStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMvVideosDefaultParams = TypedDict('TiktokMobileMvVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'mv_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMvVideosTextResponseParams = TypedDict('TiktokMobileMvVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'mv_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileMvVideosStreamParams = TypedDict('TiktokMobileMvVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'mv_id': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaceDetailDefaultParams = TypedDict('TiktokMobilePlaceDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'poi_id': Required[str],
    'review_count': NotRequired[int],
    'review_cursor': NotRequired[int],
    'merged_count': NotRequired[int],
    'video_cursor': NotRequired[int],
    'enter_from': NotRequired[str],
}, total=False)

TiktokMobilePlaceDetailTextResponseParams = TypedDict('TiktokMobilePlaceDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'poi_id': Required[str],
    'review_count': NotRequired[int],
    'review_cursor': NotRequired[int],
    'merged_count': NotRequired[int],
    'video_cursor': NotRequired[int],
    'enter_from': NotRequired[str],
}, total=False)

TiktokMobilePlaceDetailStreamParams = TypedDict('TiktokMobilePlaceDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'poi_id': Required[str],
    'review_count': NotRequired[int],
    'review_cursor': NotRequired[int],
    'merged_count': NotRequired[int],
    'video_cursor': NotRequired[int],
    'enter_from': NotRequired[str],
}, total=False)

TiktokMobilePlaceInfoDefaultParams = TypedDict('TiktokMobilePlaceInfoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlaceInfoTextResponseParams = TypedDict('TiktokMobilePlaceInfoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlaceInfoStreamParams = TypedDict('TiktokMobilePlaceInfoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlaceMediaDefaultParams = TypedDict('TiktokMobilePlaceMediaDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'poi_id': Required[str],
    'cursor': NotRequired[str],
    'size': NotRequired[int],
    'data_version': NotRequired[str],
}, total=False)

TiktokMobilePlaceMediaTextResponseParams = TypedDict('TiktokMobilePlaceMediaTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'poi_id': Required[str],
    'cursor': NotRequired[str],
    'size': NotRequired[int],
    'data_version': NotRequired[str],
}, total=False)

TiktokMobilePlaceMediaStreamParams = TypedDict('TiktokMobilePlaceMediaStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'poi_id': Required[str],
    'cursor': NotRequired[str],
    'size': NotRequired[int],
    'data_version': NotRequired[str],
}, total=False)

TiktokMobilePlacePhotosDefaultParams = TypedDict('TiktokMobilePlacePhotosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlacePhotosTextResponseParams = TypedDict('TiktokMobilePlacePhotosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlacePhotosStreamParams = TypedDict('TiktokMobilePlacePhotosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'poi_id': Required[str],
}, total=False)

TiktokMobilePlaceReviewsDefaultParams = TypedDict('TiktokMobilePlaceReviewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'poi_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
    'sort_type': NotRequired[Literal['1', '2']],
}, total=False)

TiktokMobilePlaceReviewsTextResponseParams = TypedDict('TiktokMobilePlaceReviewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'poi_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
    'sort_type': NotRequired[Literal['1', '2']],
}, total=False)

TiktokMobilePlaceReviewsStreamParams = TypedDict('TiktokMobilePlaceReviewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'poi_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
    'sort_type': NotRequired[Literal['1', '2']],
}, total=False)

TiktokMobilePlaceVideosDefaultParams = TypedDict('TiktokMobilePlaceVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'poi_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaceVideosTextResponseParams = TypedDict('TiktokMobilePlaceVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'poi_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaceVideosStreamParams = TypedDict('TiktokMobilePlaceVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'poi_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaylistDetailDefaultParams = TypedDict('TiktokMobilePlaylistDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'mix_id': Required[str],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobilePlaylistDetailTextResponseParams = TypedDict('TiktokMobilePlaylistDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'mix_id': Required[str],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobilePlaylistDetailStreamParams = TypedDict('TiktokMobilePlaylistDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'mix_id': Required[str],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobilePlaylistListDefaultParams = TypedDict('TiktokMobilePlaylistListDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaylistListTextResponseParams = TypedDict('TiktokMobilePlaylistListTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaylistListStreamParams = TypedDict('TiktokMobilePlaylistListStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobilePlaylistVideosDefaultParams = TypedDict('TiktokMobilePlaylistVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'mix_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobilePlaylistVideosTextResponseParams = TypedDict('TiktokMobilePlaylistVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'mix_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobilePlaylistVideosStreamParams = TypedDict('TiktokMobilePlaylistVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'mix_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchDefaultParams = TypedDict('TiktokMobileSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchTextResponseParams = TypedDict('TiktokMobileSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchResponseStreamParams = TypedDict('TiktokMobileSearchResponseStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchEffectsDefaultParams = TypedDict('TiktokMobileSearchEffectsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchEffectsTextResponseParams = TypedDict('TiktokMobileSearchEffectsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchEffectsStreamParams = TypedDict('TiktokMobileSearchEffectsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchHashtagsDefaultParams = TypedDict('TiktokMobileSearchHashtagsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchHashtagsTextResponseParams = TypedDict('TiktokMobileSearchHashtagsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchHashtagsStreamParams = TypedDict('TiktokMobileSearchHashtagsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchMusicDefaultParams = TypedDict('TiktokMobileSearchMusicDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

TiktokMobileSearchMusicTextResponseParams = TypedDict('TiktokMobileSearchMusicTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

TiktokMobileSearchMusicStreamParams = TypedDict('TiktokMobileSearchMusicStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

TiktokMobileSearchPhotosDefaultParams = TypedDict('TiktokMobileSearchPhotosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[int],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
}, total=False)

TiktokMobileSearchPhotosTextResponseParams = TypedDict('TiktokMobileSearchPhotosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[int],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
}, total=False)

TiktokMobileSearchPhotosStreamParams = TypedDict('TiktokMobileSearchPhotosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[int],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
}, total=False)

TiktokMobileSearchPlaceDefaultParams = TypedDict('TiktokMobileSearchPlaceDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchPlaceTextResponseParams = TypedDict('TiktokMobileSearchPlaceTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchPlaceStreamParams = TypedDict('TiktokMobileSearchPlaceStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchPreInfoDefaultParams = TypedDict('TiktokMobileSearchPreInfoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': NotRequired[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchPreInfoTextResponseParams = TypedDict('TiktokMobileSearchPreInfoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': NotRequired[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchPreInfoStreamParams = TypedDict('TiktokMobileSearchPreInfoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': NotRequired[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchStreamDefaultParams = TypedDict('TiktokMobileSearchStreamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_source': NotRequired[str],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'filter_selected': NotRequired[str],
}, total=False)

TiktokMobileSearchStreamTextResponseParams = TypedDict('TiktokMobileSearchStreamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_source': NotRequired[str],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'filter_selected': NotRequired[str],
}, total=False)

TiktokMobileSearchStreamStreamParams = TypedDict('TiktokMobileSearchStreamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'search_source': NotRequired[str],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'filter_selected': NotRequired[str],
}, total=False)

TiktokMobileSearchSugDefaultParams = TypedDict('TiktokMobileSearchSugDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchSugTextResponseParams = TypedDict('TiktokMobileSearchSugTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchSugStreamParams = TypedDict('TiktokMobileSearchSugStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
}, total=False)

TiktokMobileSearchTabsDefaultParams = TypedDict('TiktokMobileSearchTabsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
}, total=False)

TiktokMobileSearchTabsTextResponseParams = TypedDict('TiktokMobileSearchTabsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
}, total=False)

TiktokMobileSearchTabsStreamParams = TypedDict('TiktokMobileSearchTabsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
}, total=False)

TiktokMobileSearchUserDefaultParams = TypedDict('TiktokMobileSearchUserDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileSearchUserTextResponseParams = TypedDict('TiktokMobileSearchUserTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileSearchUserStreamParams = TypedDict('TiktokMobileSearchUserStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileSearchVideosDefaultParams = TypedDict('TiktokMobileSearchVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchVideosTextResponseParams = TypedDict('TiktokMobileSearchVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileSearchVideosStreamParams = TypedDict('TiktokMobileSearchVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'count': NotRequired[int],
    'offset': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '3']],
    'publish_time': NotRequired[int],
    'search_source': NotRequired[str],
    'search_id': NotRequired[str],
}, total=False)

TiktokMobileTranslationDescriptionDefaultParams = TypedDict('TiktokMobileTranslationDescriptionDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'item_id': Required[str],
    'target_lang': NotRequired[str],
}, total=False)

TiktokMobileTranslationDescriptionTextResponseParams = TypedDict('TiktokMobileTranslationDescriptionTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'item_id': Required[str],
    'target_lang': NotRequired[str],
}, total=False)

TiktokMobileTranslationDescriptionStreamParams = TypedDict('TiktokMobileTranslationDescriptionStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'item_id': Required[str],
    'target_lang': NotRequired[str],
}, total=False)

TiktokMobileTrendingCategoriesDefaultParams = TypedDict('TiktokMobileTrendingCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileTrendingCategoriesTextResponseParams = TypedDict('TiktokMobileTrendingCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileTrendingCategoriesStreamParams = TypedDict('TiktokMobileTrendingCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileTrendingEffectsDefaultParams = TypedDict('TiktokMobileTrendingEffectsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileTrendingEffectsTextResponseParams = TypedDict('TiktokMobileTrendingEffectsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileTrendingEffectsStreamParams = TypedDict('TiktokMobileTrendingEffectsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowersDefaultParams = TypedDict('TiktokMobileUserFollowersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowersTextResponseParams = TypedDict('TiktokMobileUserFollowersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowersStreamParams = TypedDict('TiktokMobileUserFollowersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowingDefaultParams = TypedDict('TiktokMobileUserFollowingDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowingTextResponseParams = TypedDict('TiktokMobileUserFollowingTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserFollowingStreamParams = TypedDict('TiktokMobileUserFollowingStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalEffectsDefaultParams = TypedDict('TiktokMobileUserOriginalEffectsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalEffectsTextResponseParams = TypedDict('TiktokMobileUserOriginalEffectsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalEffectsStreamParams = TypedDict('TiktokMobileUserOriginalEffectsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalMusicDefaultParams = TypedDict('TiktokMobileUserOriginalMusicDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalMusicTextResponseParams = TypedDict('TiktokMobileUserOriginalMusicTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserOriginalMusicStreamParams = TypedDict('TiktokMobileUserOriginalMusicStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserPostsDefaultParams = TypedDict('TiktokMobileUserPostsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[int],
}, total=False)

TiktokMobileUserPostsTextResponseParams = TypedDict('TiktokMobileUserPostsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[int],
}, total=False)

TiktokMobileUserPostsStreamParams = TypedDict('TiktokMobileUserPostsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
    'count': NotRequired[int],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[int],
}, total=False)

TiktokMobileUserProfileDefaultParams = TypedDict('TiktokMobileUserProfileDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobileUserProfileTextResponseParams = TypedDict('TiktokMobileUserProfileTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobileUserProfileStreamParams = TypedDict('TiktokMobileUserProfileStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'user_id': NotRequired[str],
    'sec_user_id': NotRequired[str],
}, total=False)

TiktokMobileUserRecommendationsDefaultParams = TypedDict('TiktokMobileUserRecommendationsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserRecommendationsTextResponseParams = TypedDict('TiktokMobileUserRecommendationsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileUserRecommendationsStreamParams = TypedDict('TiktokMobileUserRecommendationsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
}, total=False)

TiktokMobileVideoDetailDefaultParams = TypedDict('TiktokMobileVideoDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'aweme_id': Required[str],
}, total=False)

TiktokMobileVideoDetailTextResponseParams = TypedDict('TiktokMobileVideoDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'aweme_id': Required[str],
}, total=False)

TiktokMobileVideoDetailStreamParams = TypedDict('TiktokMobileVideoDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'aweme_id': Required[str],
}, total=False)

TiktokMobileVideoSubtitlesDefaultParams = TypedDict('TiktokMobileVideoSubtitlesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'video_id': Required[str],
    'language': Required[str],
}, total=False)

TiktokMobileVideoSubtitlesTextResponseParams = TypedDict('TiktokMobileVideoSubtitlesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'video_id': Required[str],
    'language': Required[str],
}, total=False)

TiktokMobileVideoSubtitlesStreamParams = TypedDict('TiktokMobileVideoSubtitlesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'video_id': Required[str],
    'language': Required[str],
}, total=False)

TiktokPopularTrendCountryIndustryMetaDefaultParams = TypedDict('TiktokPopularTrendCountryIndustryMetaDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokPopularTrendCountryIndustryMetaTextResponseParams = TypedDict('TiktokPopularTrendCountryIndustryMetaTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokPopularTrendCountryIndustryMetaStreamParams = TypedDict('TiktokPopularTrendCountryIndustryMetaStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokPostDefaultParams = TypedDict('TiktokPostDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

TiktokPostTextResponseParams = TypedDict('TiktokPostTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

TiktokPostStreamParams = TypedDict('TiktokPostStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

TiktokProfilePostDefaultParams = TypedDict('TiktokProfilePostDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'secUid': Required[str],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '2']],
}, total=False)

TiktokProfilePostTextResponseParams = TypedDict('TiktokProfilePostTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'secUid': Required[str],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '2']],
}, total=False)

TiktokProfilePostStreamParams = TypedDict('TiktokProfilePostStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'secUid': Required[str],
    'cursor': NotRequired[int],
    'sort_type': NotRequired[Literal['0', '1', '2']],
}, total=False)

TiktokProfileDefaultParams = TypedDict('TiktokProfileDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'handler': Required[str],
}, total=False)

TiktokProfileTextResponseParams = TypedDict('TiktokProfileTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'handler': Required[str],
}, total=False)

TiktokProfileStreamParams = TypedDict('TiktokProfileStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'handler': Required[str],
}, total=False)

TiktokSearchDefaultParams = TypedDict('TiktokSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokSearchTextResponseParams = TypedDict('TiktokSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokSearchStreamParams = TypedDict('TiktokSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokSearchHashtagDefaultParams = TypedDict('TiktokSearchHashtagDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokSearchHashtagTextResponseParams = TypedDict('TiktokSearchHashtagTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokSearchHashtagStreamParams = TypedDict('TiktokSearchHashtagStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
    'count': NotRequired[int],
}, total=False)

TiktokSearchUserDefaultParams = TypedDict('TiktokSearchUserDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokSearchUserTextResponseParams = TypedDict('TiktokSearchUserTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokSearchUserStreamParams = TypedDict('TiktokSearchUserStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'keyword': Required[str],
    'cursor': NotRequired[int],
}, total=False)

TiktokTopAdsAnalysisDefaultParams = TypedDict('TiktokTopAdsAnalysisDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'material_id': Required[str],
    'metric': NotRequired[Literal['retain_ctr', 'retain_cvr', 'click_cnt', 'convert_cnt', 'play_retain_cnt']],
    'period_type': NotRequired[Literal['7', '30', '180']],
}, total=False)

TiktokTopAdsAnalysisTextResponseParams = TypedDict('TiktokTopAdsAnalysisTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'material_id': Required[str],
    'metric': NotRequired[Literal['retain_ctr', 'retain_cvr', 'click_cnt', 'convert_cnt', 'play_retain_cnt']],
    'period_type': NotRequired[Literal['7', '30', '180']],
}, total=False)

TiktokTopAdsAnalysisStreamParams = TypedDict('TiktokTopAdsAnalysisStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'material_id': Required[str],
    'metric': NotRequired[Literal['retain_ctr', 'retain_cvr', 'click_cnt', 'convert_cnt', 'play_retain_cnt']],
    'period_type': NotRequired[Literal['7', '30', '180']],
}, total=False)

TiktokTopAdsDetailDefaultParams = TypedDict('TiktokTopAdsDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'material_id': Required[str],
}, total=False)

TiktokTopAdsDetailTextResponseParams = TypedDict('TiktokTopAdsDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'material_id': Required[str],
}, total=False)

TiktokTopAdsDetailStreamParams = TypedDict('TiktokTopAdsDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'material_id': Required[str],
}, total=False)

TiktokTopAdsFiltersDefaultParams = TypedDict('TiktokTopAdsFiltersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokTopAdsFiltersTextResponseParams = TypedDict('TiktokTopAdsFiltersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokTopAdsFiltersStreamParams = TypedDict('TiktokTopAdsFiltersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokTopAdsListDefaultParams = TypedDict('TiktokTopAdsListDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'period': NotRequired[Literal['7', '30', '180']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'order_by': NotRequired[Literal['for_you', 'impression', 'ctr', 'play_2s_rate', 'play_6s_rate', 'cvr', 'like']],
    'country_code': NotRequired[str],
    'keyword': NotRequired[str],
    'industry': NotRequired[str],
    'objective': NotRequired[str],
    'ad_language': NotRequired[str],
    'pattern_label': NotRequired[str],
    'duration': NotRequired[Literal['time-2', 'time-3', 'time-4', 'time-5', 'time-6', 'time-7']],
    'like': NotRequired[Literal['1', '2', '3', '4', '5']],
    'ad_format': NotRequired[Literal['1', '2']],
}, total=False)

TiktokTopAdsListTextResponseParams = TypedDict('TiktokTopAdsListTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'period': NotRequired[Literal['7', '30', '180']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'order_by': NotRequired[Literal['for_you', 'impression', 'ctr', 'play_2s_rate', 'play_6s_rate', 'cvr', 'like']],
    'country_code': NotRequired[str],
    'keyword': NotRequired[str],
    'industry': NotRequired[str],
    'objective': NotRequired[str],
    'ad_language': NotRequired[str],
    'pattern_label': NotRequired[str],
    'duration': NotRequired[Literal['time-2', 'time-3', 'time-4', 'time-5', 'time-6', 'time-7']],
    'like': NotRequired[Literal['1', '2', '3', '4', '5']],
    'ad_format': NotRequired[Literal['1', '2']],
}, total=False)

TiktokTopAdsListStreamParams = TypedDict('TiktokTopAdsListStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'period': NotRequired[Literal['7', '30', '180']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
    'order_by': NotRequired[Literal['for_you', 'impression', 'ctr', 'play_2s_rate', 'play_6s_rate', 'cvr', 'like']],
    'country_code': NotRequired[str],
    'keyword': NotRequired[str],
    'industry': NotRequired[str],
    'objective': NotRequired[str],
    'ad_language': NotRequired[str],
    'pattern_label': NotRequired[str],
    'duration': NotRequired[Literal['time-2', 'time-3', 'time-4', 'time-5', 'time-6', 'time-7']],
    'like': NotRequired[Literal['1', '2', '3', '4', '5']],
    'ad_format': NotRequired[Literal['1', '2']],
}, total=False)

TiktokTopAdsLocationInfoDefaultParams = TypedDict('TiktokTopAdsLocationInfoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'module': NotRequired[int],
}, total=False)

TiktokTopAdsLocationInfoTextResponseParams = TypedDict('TiktokTopAdsLocationInfoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'module': NotRequired[int],
}, total=False)

TiktokTopAdsLocationInfoStreamParams = TypedDict('TiktokTopAdsLocationInfoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'module': NotRequired[int],
}, total=False)

TiktokTopAdsLocationsDefaultParams = TypedDict('TiktokTopAdsLocationsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokTopAdsLocationsTextResponseParams = TypedDict('TiktokTopAdsLocationsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokTopAdsLocationsStreamParams = TypedDict('TiktokTopAdsLocationsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokTopAdsRecommendDefaultParams = TypedDict('TiktokTopAdsRecommendDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'material_id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

TiktokTopAdsRecommendTextResponseParams = TypedDict('TiktokTopAdsRecommendTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'material_id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

TiktokTopAdsRecommendStreamParams = TypedDict('TiktokTopAdsRecommendStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'material_id': Required[str],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

TiktokTopAdsSafetyDefaultParams = TypedDict('TiktokTopAdsSafetyDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokTopAdsSafetyTextResponseParams = TypedDict('TiktokTopAdsSafetyTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokTopAdsSafetyStreamParams = TypedDict('TiktokTopAdsSafetyStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

TiktokTopAdsSpotlightDefaultParams = TypedDict('TiktokTopAdsSpotlightDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

TiktokTopAdsSpotlightTextResponseParams = TypedDict('TiktokTopAdsSpotlightTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

TiktokTopAdsSpotlightStreamParams = TypedDict('TiktokTopAdsSpotlightStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

TiktokTopAdsSuggestionsDefaultParams = TypedDict('TiktokTopAdsSuggestionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'count': NotRequired[int],
    'scenario': NotRequired[int],
}, total=False)

TiktokTopAdsSuggestionsTextResponseParams = TypedDict('TiktokTopAdsSuggestionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'count': NotRequired[int],
    'scenario': NotRequired[int],
}, total=False)

TiktokTopAdsSuggestionsStreamParams = TypedDict('TiktokTopAdsSuggestionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'count': NotRequired[int],
    'scenario': NotRequired[int],
}, total=False)

TiktokTrendingDefaultParams = TypedDict('TiktokTrendingDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

TiktokTrendingTextResponseParams = TypedDict('TiktokTrendingTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

TiktokTrendingStreamParams = TypedDict('TiktokTrendingStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)
