import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class TikTokClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-tiktok-js/0.5.0" });
    this["category"] = (...args) => this.request("tiktok-category", ...args);
    this["videoComments"] = (...args) => this.request("tiktok-video-comments", ...args);
    this["creativeCenterFilters"] = (...args) => this.request("tiktok-creative-center-filters", ...args);
    this["creativeCenterHashtags"] = (...args) => this.request("tiktok-creative-center-hashtags", ...args);
    this["creativeCenterTopContent"] = (...args) => this.request("tiktok-creative-center-top-content", ...args);
    this["creativeCenterVideos"] = (...args) => this.request("tiktok-creative-center-videos", ...args);
    this["explore"] = (...args) => this.request("tiktok-explore", ...args);
    this["challenge"] = (...args) => this.request("tiktok-challenge", ...args);
    this["challengeList"] = (...args) => this.request("tiktok-challenge-list", ...args);
    this["mobileAnchorList"] = (...args) => this.request("tiktok-mobile-anchor-list", ...args);
    this["mobileCollectionDetail"] = (...args) => this.request("tiktok-mobile-collection-detail", ...args);
    this["mobileCollectionList"] = (...args) => this.request("tiktok-mobile-collection-list", ...args);
    this["mobileCollectionVideos"] = (...args) => this.request("tiktok-mobile-collection-videos", ...args);
    this["mobileCommentReplies"] = (...args) => this.request("tiktok-mobile-comment-replies", ...args);
    this["mobileComments"] = (...args) => this.request("tiktok-mobile-comments", ...args);
    this["mobileFeed"] = (...args) => this.request("tiktok-mobile-feed", ...args);
    this["mobileFeedOffline"] = (...args) => this.request("tiktok-mobile-feed-offline", ...args);
    this["mobileFeedPost"] = (...args) => this.request("tiktok-mobile-feed-post", ...args);
    this["mobileHashtag"] = (...args) => this.request("tiktok-mobile-hashtag", ...args);
    this["mobileHashtagPosts"] = (...args) => this.request("tiktok-mobile-hashtag-posts", ...args);
    this["mobileHashtags"] = (...args) => this.request("tiktok-mobile-hashtags", ...args);
    this["mobileLiveEffects"] = (...args) => this.request("tiktok-mobile-live-effects", ...args);
    this["mobileLiveGifts"] = (...args) => this.request("tiktok-mobile-live-gifts", ...args);
    this["mobileLiveHashtags"] = (...args) => this.request("tiktok-mobile-live-hashtags", ...args);
    this["mobileLiveRoom"] = (...args) => this.request("tiktok-mobile-live-room", ...args);
    this["mobileLiveRoomByUser"] = (...args) => this.request("tiktok-mobile-live-room-by-user", ...args);
    this["mobileLiveSearch"] = (...args) => this.request("tiktok-mobile-live-search", ...args);
    this["mobileLiveTabs"] = (...args) => this.request("tiktok-mobile-live-tabs", ...args);
    this["mobileMusicBeats"] = (...args) => this.request("tiktok-mobile-music-beats", ...args);
    this["mobileMusicChart"] = (...args) => this.request("tiktok-mobile-music-chart", ...args);
    this["mobileMusicChoices"] = (...args) => this.request("tiktok-mobile-music-choices", ...args);
    this["mobileMusicCollectionList"] = (...args) => this.request("tiktok-mobile-music-collection-list", ...args);
    this["mobileMusicCollections"] = (...args) => this.request("tiktok-mobile-music-collections", ...args);
    this["mobileMusicDetail"] = (...args) => this.request("tiktok-mobile-music-detail", ...args);
    this["mobileMusicPick"] = (...args) => this.request("tiktok-mobile-music-pick", ...args);
    this["mobileMusicPosts"] = (...args) => this.request("tiktok-mobile-music-posts", ...args);
    this["mobileMusicRelated"] = (...args) => this.request("tiktok-mobile-music-related", ...args);
    this["mobileMusicTrending"] = (...args) => this.request("tiktok-mobile-music-trending", ...args);
    this["mobileMvVideos"] = (...args) => this.request("tiktok-mobile-mv-videos", ...args);
    this["mobilePlaceDetail"] = (...args) => this.request("tiktok-mobile-place-detail", ...args);
    this["mobilePlaceInfo"] = (...args) => this.request("tiktok-mobile-place-info", ...args);
    this["mobilePlaceMedia"] = (...args) => this.request("tiktok-mobile-place-media", ...args);
    this["mobilePlacePhotos"] = (...args) => this.request("tiktok-mobile-place-photos", ...args);
    this["mobilePlaceReviews"] = (...args) => this.request("tiktok-mobile-place-reviews", ...args);
    this["mobilePlaceVideos"] = (...args) => this.request("tiktok-mobile-place-videos", ...args);
    this["mobilePlaylistDetail"] = (...args) => this.request("tiktok-mobile-playlist-detail", ...args);
    this["mobilePlaylistList"] = (...args) => this.request("tiktok-mobile-playlist-list", ...args);
    this["mobilePlaylistVideos"] = (...args) => this.request("tiktok-mobile-playlist-videos", ...args);
    this["mobileSearch"] = (...args) => this.request("tiktok-mobile-search", ...args);
    this["mobileSearchEffects"] = (...args) => this.request("tiktok-mobile-search-effects", ...args);
    this["mobileSearchHashtags"] = (...args) => this.request("tiktok-mobile-search-hashtags", ...args);
    this["mobileSearchMusic"] = (...args) => this.request("tiktok-mobile-search-music", ...args);
    this["mobileSearchPhotos"] = (...args) => this.request("tiktok-mobile-search-photos", ...args);
    this["mobileSearchPlace"] = (...args) => this.request("tiktok-mobile-search-place", ...args);
    this["mobileSearchPreInfo"] = (...args) => this.request("tiktok-mobile-search-pre-info", ...args);
    this["mobileSearchStream"] = (...args) => this.request("tiktok-mobile-search-stream", ...args);
    this["mobileSearchSug"] = (...args) => this.request("tiktok-mobile-search-sug", ...args);
    this["mobileSearchTabs"] = (...args) => this.request("tiktok-mobile-search-tabs", ...args);
    this["mobileSearchUser"] = (...args) => this.request("tiktok-mobile-search-user", ...args);
    this["mobileSearchVideos"] = (...args) => this.request("tiktok-mobile-search-videos", ...args);
    this["mobileTranslationDescription"] = (...args) => this.request("tiktok-mobile-translation-description", ...args);
    this["mobileTrendingCategories"] = (...args) => this.request("tiktok-mobile-trending-categories", ...args);
    this["mobileTrendingEffects"] = (...args) => this.request("tiktok-mobile-trending-effects", ...args);
    this["mobileUserFollowers"] = (...args) => this.request("tiktok-mobile-user-followers", ...args);
    this["mobileUserFollowing"] = (...args) => this.request("tiktok-mobile-user-following", ...args);
    this["mobileUserOriginalEffects"] = (...args) => this.request("tiktok-mobile-user-original-effects", ...args);
    this["mobileUserOriginalMusic"] = (...args) => this.request("tiktok-mobile-user-original-music", ...args);
    this["mobileUserPosts"] = (...args) => this.request("tiktok-mobile-user-posts", ...args);
    this["mobileUserProfile"] = (...args) => this.request("tiktok-mobile-user-profile", ...args);
    this["mobileUserRecommendations"] = (...args) => this.request("tiktok-mobile-user-recommendations", ...args);
    this["mobileVideoDetail"] = (...args) => this.request("tiktok-mobile-video-detail", ...args);
    this["mobileVideoSubtitles"] = (...args) => this.request("tiktok-mobile-video-subtitles", ...args);
    this["popularTrendCountryIndustryMeta"] = (...args) => this.request("tiktok-popular-trend-country-industry-meta", ...args);
    this["post"] = (...args) => this.request("tiktok-post", ...args);
    this["profilePost"] = (...args) => this.request("tiktok-profile-post", ...args);
    this["profile"] = (...args) => this.request("tiktok-profile", ...args);
    this["search"] = (...args) => this.request("tiktok-search", ...args);
    this["searchHashtag"] = (...args) => this.request("tiktok-search-hashtag", ...args);
    this["searchUser"] = (...args) => this.request("tiktok-search-user", ...args);
    this["topAdsAnalysis"] = (...args) => this.request("tiktok-top-ads-analysis", ...args);
    this["topAdsDetail"] = (...args) => this.request("tiktok-top-ads-detail", ...args);
    this["topAdsFilters"] = (...args) => this.request("tiktok-top-ads-filters", ...args);
    this["topAdsList"] = (...args) => this.request("tiktok-top-ads-list", ...args);
    this["topAdsLocationInfo"] = (...args) => this.request("tiktok-top-ads-location-info", ...args);
    this["topAdsLocations"] = (...args) => this.request("tiktok-top-ads-locations", ...args);
    this["topAdsRecommend"] = (...args) => this.request("tiktok-top-ads-recommend", ...args);
    this["topAdsSafety"] = (...args) => this.request("tiktok-top-ads-safety", ...args);
    this["topAdsSpotlight"] = (...args) => this.request("tiktok-top-ads-spotlight", ...args);
    this["topAdsSuggestions"] = (...args) => this.request("tiktok-top-ads-suggestions", ...args);
    this["trending"] = (...args) => this.request("tiktok-trending", ...args);
  }
}

export { TikTokClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.5.0";
export default TikTokClient;
