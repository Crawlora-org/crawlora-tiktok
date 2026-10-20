"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class TikTokClient(CrawloraClient):
    """Synchronous TikTok API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-tiktok-python/0.4.0')
        super().__init__(*args, **kwargs)

    def category(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-category', params, response_type=response_type, timeout=timeout, headers=headers)

    def video_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-video-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    def creative_center_filters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-creative-center-filters', params, response_type=response_type, timeout=timeout, headers=headers)

    def creative_center_hashtags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-creative-center-hashtags', params, response_type=response_type, timeout=timeout, headers=headers)

    def creative_center_top_content(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-creative-center-top-content', params, response_type=response_type, timeout=timeout, headers=headers)

    def creative_center_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-creative-center-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    def explore(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-explore', params, response_type=response_type, timeout=timeout, headers=headers)

    def challenge(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-challenge', params, response_type=response_type, timeout=timeout, headers=headers)

    def challenge_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-challenge-list', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_anchor_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-anchor-list', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_comment_replies(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-comment-replies', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_feed(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-feed', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_feed_post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-feed-post', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_hashtag(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-hashtag', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_hashtag_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-hashtag-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_hashtags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-hashtags', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_live_effects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-live-effects', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_live_gifts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-live-gifts', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_live_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-live-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_music_beats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-beats', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_music_collections(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-collections', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_music_pick(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-pick', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_music_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_music_related(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-related', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_music_trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-music-trending', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_search_music(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-music', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_search_place(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-place', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_search_pre_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-pre-info', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_search_sug(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-sug', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_search_tabs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-tabs', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_search_user(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-search-user', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_trending_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-trending-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def mobile_trending_effects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-mobile-trending-effects', params, response_type=response_type, timeout=timeout, headers=headers)

    def popular_trend_country_industry_meta(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-popular-trend-country-industry-meta', params, response_type=response_type, timeout=timeout, headers=headers)

    def post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-post', params, response_type=response_type, timeout=timeout, headers=headers)

    def profile_post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-profile-post', params, response_type=response_type, timeout=timeout, headers=headers)

    def profile(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-profile', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_hashtag(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-search-hashtag', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_user(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-search-user', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_ads_analysis(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-top-ads-analysis', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_ads_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-top-ads-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_ads_filters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-top-ads-filters', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_ads_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-top-ads-list', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_ads_location_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-top-ads-location-info', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_ads_locations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-top-ads-locations', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_ads_recommend(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-top-ads-recommend', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_ads_safety(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-top-ads-safety', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_ads_spotlight(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-top-ads-spotlight', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_ads_suggestions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-top-ads-suggestions', params, response_type=response_type, timeout=timeout, headers=headers)

    def trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('tiktok-trending', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncTikTokClient(AsyncCrawloraClient):
    """Asynchronous TikTok API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-tiktok-python/0.4.0')
        super().__init__(*args, **kwargs)

    async def category(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-category', params, response_type=response_type, timeout=timeout, headers=headers)

    async def video_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-video-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def creative_center_filters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-creative-center-filters', params, response_type=response_type, timeout=timeout, headers=headers)

    async def creative_center_hashtags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-creative-center-hashtags', params, response_type=response_type, timeout=timeout, headers=headers)

    async def creative_center_top_content(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-creative-center-top-content', params, response_type=response_type, timeout=timeout, headers=headers)

    async def creative_center_videos(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-creative-center-videos', params, response_type=response_type, timeout=timeout, headers=headers)

    async def explore(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-explore', params, response_type=response_type, timeout=timeout, headers=headers)

    async def challenge(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-challenge', params, response_type=response_type, timeout=timeout, headers=headers)

    async def challenge_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-challenge-list', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_anchor_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-anchor-list', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_comment_replies(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-comment-replies', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_feed(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-feed', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_feed_post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-feed-post', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_hashtag(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-hashtag', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_hashtag_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-hashtag-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_hashtags(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-hashtags', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_live_effects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-live-effects', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_live_gifts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-live-gifts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_live_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-live-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_music_beats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-beats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_music_collections(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-collections', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_music_pick(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-pick', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_music_posts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-posts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_music_related(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-related', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_music_trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-music-trending', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_search_music(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-music', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_search_place(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-place', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_search_pre_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-pre-info', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_search_sug(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-sug', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_search_tabs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-tabs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_search_user(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-search-user', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_trending_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-trending-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def mobile_trending_effects(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-mobile-trending-effects', params, response_type=response_type, timeout=timeout, headers=headers)

    async def popular_trend_country_industry_meta(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-popular-trend-country-industry-meta', params, response_type=response_type, timeout=timeout, headers=headers)

    async def post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-post', params, response_type=response_type, timeout=timeout, headers=headers)

    async def profile_post(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-profile-post', params, response_type=response_type, timeout=timeout, headers=headers)

    async def profile(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-profile', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_hashtag(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-search-hashtag', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_user(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-search-user', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_ads_analysis(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-top-ads-analysis', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_ads_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-top-ads-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_ads_filters(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-top-ads-filters', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_ads_list(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-top-ads-list', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_ads_location_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-top-ads-location-info', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_ads_locations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-top-ads-locations', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_ads_recommend(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-top-ads-recommend', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_ads_safety(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-top-ads-safety', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_ads_spotlight(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-top-ads-spotlight', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_ads_suggestions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-top-ads-suggestions', params, response_type=response_type, timeout=timeout, headers=headers)

    async def trending(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('tiktok-trending', params, response_type=response_type, timeout=timeout, headers=headers)
