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
    'create_time': NotRequired[int],
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

ModelCreativecenterTrendingVideoContentTag = TypedDict('ModelCreativecenterTrendingVideoContentTag', {
    'id': NotRequired[str],
    'name': NotRequired[str],
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

TiktokCreativeCenterHashtagsResponse = ModelCreativecenterTrendingHashtagsResponseDoc
TiktokCreativeCenterHashtagsParams = TypedDict('TiktokCreativeCenterHashtagsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30']],
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
    def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsTextResponseParams]) -> str: ...
    @overload
    def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsDefaultParams]) -> TiktokCreativeCenterHashtagsResponse: ...
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
    'tiktok-creative-center-hashtags',
    'tiktok-creative-center-videos',
    'tiktok-explore',
    'tiktok-challenge',
    'tiktok-challenge-list',
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
    def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsTextResponseParams]) -> str: ...
    @overload
    def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsDefaultParams]) -> TiktokCreativeCenterHashtagsResponse: ...
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
    async def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsTextResponseParams]) -> str: ...
    @overload
    async def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsDefaultParams]) -> TiktokCreativeCenterHashtagsResponse: ...
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
    async def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsStreamParams]) -> BinaryIO: ...
    @overload
    async def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsTextResponseParams]) -> str: ...
    @overload
    async def creative_center_hashtags(self, **params: Unpack[TiktokCreativeCenterHashtagsDefaultParams]) -> TiktokCreativeCenterHashtagsResponse: ...
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

TiktokCreativeCenterHashtagsDefaultParams = TypedDict('TiktokCreativeCenterHashtagsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30']],
}, total=False)

TiktokCreativeCenterHashtagsTextResponseParams = TypedDict('TiktokCreativeCenterHashtagsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30']],
}, total=False)

TiktokCreativeCenterHashtagsStreamParams = TypedDict('TiktokCreativeCenterHashtagsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30']],
}, total=False)

TiktokCreativeCenterVideosDefaultParams = TypedDict('TiktokCreativeCenterVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'country_code': Required[str],
    'period': NotRequired[Literal['7', '30']],
    'sort_by': NotRequired[Literal['views', 'engagement', 'six_second_views']],
    'content_label_id': NotRequired[str],
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
