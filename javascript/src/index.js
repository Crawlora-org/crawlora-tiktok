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
    super({ ...options, userAgent: options.userAgent ?? "crawlora-tiktok-js/0.4.0" });
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
    this["mobileCommentReplies"] = (...args) => this.request("tiktok-mobile-comment-replies", ...args);
    this["mobileComments"] = (...args) => this.request("tiktok-mobile-comments", ...args);
    this["mobileFeed"] = (...args) => this.request("tiktok-mobile-feed", ...args);
    this["mobileFeedPost"] = (...args) => this.request("tiktok-mobile-feed-post", ...args);
    this["mobileHashtag"] = (...args) => this.request("tiktok-mobile-hashtag", ...args);
    this["mobileHashtagPosts"] = (...args) => this.request("tiktok-mobile-hashtag-posts", ...args);
    this["mobileHashtags"] = (...args) => this.request("tiktok-mobile-hashtags", ...args);
    this["mobileLiveEffects"] = (...args) => this.request("tiktok-mobile-live-effects", ...args);
    this["mobileLiveGifts"] = (...args) => this.request("tiktok-mobile-live-gifts", ...args);
    this["mobileLiveSearch"] = (...args) => this.request("tiktok-mobile-live-search", ...args);
    this["mobileMusicBeats"] = (...args) => this.request("tiktok-mobile-music-beats", ...args);
    this["mobileMusicCollections"] = (...args) => this.request("tiktok-mobile-music-collections", ...args);
    this["mobileMusicPick"] = (...args) => this.request("tiktok-mobile-music-pick", ...args);
    this["mobileMusicPosts"] = (...args) => this.request("tiktok-mobile-music-posts", ...args);
    this["mobileMusicRelated"] = (...args) => this.request("tiktok-mobile-music-related", ...args);
    this["mobileMusicTrending"] = (...args) => this.request("tiktok-mobile-music-trending", ...args);
    this["mobileSearch"] = (...args) => this.request("tiktok-mobile-search", ...args);
    this["mobileSearchMusic"] = (...args) => this.request("tiktok-mobile-search-music", ...args);
    this["mobileSearchPlace"] = (...args) => this.request("tiktok-mobile-search-place", ...args);
    this["mobileSearchPreInfo"] = (...args) => this.request("tiktok-mobile-search-pre-info", ...args);
    this["mobileSearchSug"] = (...args) => this.request("tiktok-mobile-search-sug", ...args);
    this["mobileSearchTabs"] = (...args) => this.request("tiktok-mobile-search-tabs", ...args);
    this["mobileSearchUser"] = (...args) => this.request("tiktok-mobile-search-user", ...args);
    this["mobileTrendingCategories"] = (...args) => this.request("tiktok-mobile-trending-categories", ...args);
    this["mobileTrendingEffects"] = (...args) => this.request("tiktok-mobile-trending-effects", ...args);
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
export const VERSION = "0.4.0";
export default TikTokClient;
