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
    super({ ...options, userAgent: options.userAgent ?? "crawlora-tiktok-js/0.1.1" });
    this["category"] = (...args) => this.request("tiktok-category", ...args);
    this["videoComments"] = (...args) => this.request("tiktok-video-comments", ...args);
    this["creativeCenterHashtags"] = (...args) => this.request("tiktok-creative-center-hashtags", ...args);
    this["creativeCenterVideos"] = (...args) => this.request("tiktok-creative-center-videos", ...args);
    this["explore"] = (...args) => this.request("tiktok-explore", ...args);
    this["challenge"] = (...args) => this.request("tiktok-challenge", ...args);
    this["challengeList"] = (...args) => this.request("tiktok-challenge-list", ...args);
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
export const VERSION = "0.1.1";
export default TikTokClient;
