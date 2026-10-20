import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class TikTokClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  category(params?: OperationParamsMap["tiktok-category"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  videoComments(params: OperationParamsMap["tiktok-video-comments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  creativeCenterFilters(params?: OperationParamsMap["tiktok-creative-center-filters"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  creativeCenterHashtags(params: OperationParamsMap["tiktok-creative-center-hashtags"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  creativeCenterTopContent(params?: OperationParamsMap["tiktok-creative-center-top-content"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  creativeCenterVideos(params: OperationParamsMap["tiktok-creative-center-videos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  explore(params: OperationParamsMap["tiktok-explore"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  challenge(params: OperationParamsMap["tiktok-challenge"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  challengeList(params: OperationParamsMap["tiktok-challenge-list"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileAnchorList(params?: OperationParamsMap["tiktok-mobile-anchor-list"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileCommentReplies(params: OperationParamsMap["tiktok-mobile-comment-replies"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileComments(params: OperationParamsMap["tiktok-mobile-comments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileFeed(params?: OperationParamsMap["tiktok-mobile-feed"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileFeedPost(params?: OperationParamsMap["tiktok-mobile-feed-post"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileHashtag(params: OperationParamsMap["tiktok-mobile-hashtag"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileHashtagPosts(params: OperationParamsMap["tiktok-mobile-hashtag-posts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileHashtags(params: OperationParamsMap["tiktok-mobile-hashtags"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileLiveEffects(params?: OperationParamsMap["tiktok-mobile-live-effects"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileLiveGifts(params?: OperationParamsMap["tiktok-mobile-live-gifts"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileLiveSearch(params: OperationParamsMap["tiktok-mobile-live-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileMusicBeats(params?: OperationParamsMap["tiktok-mobile-music-beats"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileMusicCollections(params?: OperationParamsMap["tiktok-mobile-music-collections"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileMusicPick(params?: OperationParamsMap["tiktok-mobile-music-pick"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileMusicPosts(params: OperationParamsMap["tiktok-mobile-music-posts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileMusicRelated(params: OperationParamsMap["tiktok-mobile-music-related"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileMusicTrending(params?: OperationParamsMap["tiktok-mobile-music-trending"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileSearch(params: OperationParamsMap["tiktok-mobile-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileSearchMusic(params: OperationParamsMap["tiktok-mobile-search-music"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileSearchPlace(params: OperationParamsMap["tiktok-mobile-search-place"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileSearchPreInfo(params?: OperationParamsMap["tiktok-mobile-search-pre-info"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileSearchSug(params: OperationParamsMap["tiktok-mobile-search-sug"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileSearchTabs(params: OperationParamsMap["tiktok-mobile-search-tabs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileSearchUser(params: OperationParamsMap["tiktok-mobile-search-user"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileTrendingCategories(params?: OperationParamsMap["tiktok-mobile-trending-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  mobileTrendingEffects(params?: OperationParamsMap["tiktok-mobile-trending-effects"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  popularTrendCountryIndustryMeta(params?: OperationParamsMap["tiktok-popular-trend-country-industry-meta"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  post(params: OperationParamsMap["tiktok-post"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  profilePost(params: OperationParamsMap["tiktok-profile-post"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  profile(params: OperationParamsMap["tiktok-profile"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["tiktok-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchHashtag(params: OperationParamsMap["tiktok-search-hashtag"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchUser(params: OperationParamsMap["tiktok-search-user"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topAdsAnalysis(params: OperationParamsMap["tiktok-top-ads-analysis"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topAdsDetail(params: OperationParamsMap["tiktok-top-ads-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topAdsFilters(params?: OperationParamsMap["tiktok-top-ads-filters"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topAdsList(params?: OperationParamsMap["tiktok-top-ads-list"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topAdsLocationInfo(params?: OperationParamsMap["tiktok-top-ads-location-info"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topAdsLocations(params?: OperationParamsMap["tiktok-top-ads-locations"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topAdsRecommend(params: OperationParamsMap["tiktok-top-ads-recommend"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topAdsSafety(params?: OperationParamsMap["tiktok-top-ads-safety"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topAdsSpotlight(params?: OperationParamsMap["tiktok-top-ads-spotlight"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topAdsSuggestions(params?: OperationParamsMap["tiktok-top-ads-suggestions"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  trending(params?: OperationParamsMap["tiktok-trending"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  category(params?: OperationParamsMap["tiktok-category"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  videoComments(params: OperationParamsMap["tiktok-video-comments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  creativeCenterFilters(params?: OperationParamsMap["tiktok-creative-center-filters"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  creativeCenterHashtags(params: OperationParamsMap["tiktok-creative-center-hashtags"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  creativeCenterTopContent(params?: OperationParamsMap["tiktok-creative-center-top-content"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  creativeCenterVideos(params: OperationParamsMap["tiktok-creative-center-videos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  explore(params: OperationParamsMap["tiktok-explore"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  challenge(params: OperationParamsMap["tiktok-challenge"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  challengeList(params: OperationParamsMap["tiktok-challenge-list"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileAnchorList(params?: OperationParamsMap["tiktok-mobile-anchor-list"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileCommentReplies(params: OperationParamsMap["tiktok-mobile-comment-replies"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileComments(params: OperationParamsMap["tiktok-mobile-comments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileFeed(params?: OperationParamsMap["tiktok-mobile-feed"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileFeedPost(params?: OperationParamsMap["tiktok-mobile-feed-post"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileHashtag(params: OperationParamsMap["tiktok-mobile-hashtag"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileHashtagPosts(params: OperationParamsMap["tiktok-mobile-hashtag-posts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileHashtags(params: OperationParamsMap["tiktok-mobile-hashtags"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileLiveEffects(params?: OperationParamsMap["tiktok-mobile-live-effects"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileLiveGifts(params?: OperationParamsMap["tiktok-mobile-live-gifts"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileLiveSearch(params: OperationParamsMap["tiktok-mobile-live-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileMusicBeats(params?: OperationParamsMap["tiktok-mobile-music-beats"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileMusicCollections(params?: OperationParamsMap["tiktok-mobile-music-collections"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileMusicPick(params?: OperationParamsMap["tiktok-mobile-music-pick"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileMusicPosts(params: OperationParamsMap["tiktok-mobile-music-posts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileMusicRelated(params: OperationParamsMap["tiktok-mobile-music-related"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileMusicTrending(params?: OperationParamsMap["tiktok-mobile-music-trending"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileSearch(params: OperationParamsMap["tiktok-mobile-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileSearchMusic(params: OperationParamsMap["tiktok-mobile-search-music"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileSearchPlace(params: OperationParamsMap["tiktok-mobile-search-place"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileSearchPreInfo(params?: OperationParamsMap["tiktok-mobile-search-pre-info"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileSearchSug(params: OperationParamsMap["tiktok-mobile-search-sug"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileSearchTabs(params: OperationParamsMap["tiktok-mobile-search-tabs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileSearchUser(params: OperationParamsMap["tiktok-mobile-search-user"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileTrendingCategories(params?: OperationParamsMap["tiktok-mobile-trending-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  mobileTrendingEffects(params?: OperationParamsMap["tiktok-mobile-trending-effects"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  popularTrendCountryIndustryMeta(params?: OperationParamsMap["tiktok-popular-trend-country-industry-meta"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  post(params: OperationParamsMap["tiktok-post"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  profilePost(params: OperationParamsMap["tiktok-profile-post"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  profile(params: OperationParamsMap["tiktok-profile"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["tiktok-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchHashtag(params: OperationParamsMap["tiktok-search-hashtag"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchUser(params: OperationParamsMap["tiktok-search-user"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topAdsAnalysis(params: OperationParamsMap["tiktok-top-ads-analysis"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topAdsDetail(params: OperationParamsMap["tiktok-top-ads-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topAdsFilters(params?: OperationParamsMap["tiktok-top-ads-filters"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topAdsList(params?: OperationParamsMap["tiktok-top-ads-list"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topAdsLocationInfo(params?: OperationParamsMap["tiktok-top-ads-location-info"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topAdsLocations(params?: OperationParamsMap["tiktok-top-ads-locations"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topAdsRecommend(params: OperationParamsMap["tiktok-top-ads-recommend"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topAdsSafety(params?: OperationParamsMap["tiktok-top-ads-safety"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topAdsSpotlight(params?: OperationParamsMap["tiktok-top-ads-spotlight"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topAdsSuggestions(params?: OperationParamsMap["tiktok-top-ads-suggestions"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  trending(params?: OperationParamsMap["tiktok-trending"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  category(...args: OperationRequestArgs<"tiktok-category">): Promise<OperationResponseMap["tiktok-category"]>;
  videoComments(...args: OperationRequestArgs<"tiktok-video-comments">): Promise<OperationResponseMap["tiktok-video-comments"]>;
  creativeCenterFilters(...args: OperationRequestArgs<"tiktok-creative-center-filters">): Promise<OperationResponseMap["tiktok-creative-center-filters"]>;
  creativeCenterHashtags(...args: OperationRequestArgs<"tiktok-creative-center-hashtags">): Promise<OperationResponseMap["tiktok-creative-center-hashtags"]>;
  creativeCenterTopContent(...args: OperationRequestArgs<"tiktok-creative-center-top-content">): Promise<OperationResponseMap["tiktok-creative-center-top-content"]>;
  creativeCenterVideos(...args: OperationRequestArgs<"tiktok-creative-center-videos">): Promise<OperationResponseMap["tiktok-creative-center-videos"]>;
  explore(...args: OperationRequestArgs<"tiktok-explore">): Promise<OperationResponseMap["tiktok-explore"]>;
  challenge(...args: OperationRequestArgs<"tiktok-challenge">): Promise<OperationResponseMap["tiktok-challenge"]>;
  challengeList(...args: OperationRequestArgs<"tiktok-challenge-list">): Promise<OperationResponseMap["tiktok-challenge-list"]>;
  mobileAnchorList(...args: OperationRequestArgs<"tiktok-mobile-anchor-list">): Promise<OperationResponseMap["tiktok-mobile-anchor-list"]>;
  mobileCommentReplies(...args: OperationRequestArgs<"tiktok-mobile-comment-replies">): Promise<OperationResponseMap["tiktok-mobile-comment-replies"]>;
  mobileComments(...args: OperationRequestArgs<"tiktok-mobile-comments">): Promise<OperationResponseMap["tiktok-mobile-comments"]>;
  mobileFeed(...args: OperationRequestArgs<"tiktok-mobile-feed">): Promise<OperationResponseMap["tiktok-mobile-feed"]>;
  mobileFeedPost(...args: OperationRequestArgs<"tiktok-mobile-feed-post">): Promise<OperationResponseMap["tiktok-mobile-feed-post"]>;
  mobileHashtag(...args: OperationRequestArgs<"tiktok-mobile-hashtag">): Promise<OperationResponseMap["tiktok-mobile-hashtag"]>;
  mobileHashtagPosts(...args: OperationRequestArgs<"tiktok-mobile-hashtag-posts">): Promise<OperationResponseMap["tiktok-mobile-hashtag-posts"]>;
  mobileHashtags(...args: OperationRequestArgs<"tiktok-mobile-hashtags">): Promise<OperationResponseMap["tiktok-mobile-hashtags"]>;
  mobileLiveEffects(...args: OperationRequestArgs<"tiktok-mobile-live-effects">): Promise<OperationResponseMap["tiktok-mobile-live-effects"]>;
  mobileLiveGifts(...args: OperationRequestArgs<"tiktok-mobile-live-gifts">): Promise<OperationResponseMap["tiktok-mobile-live-gifts"]>;
  mobileLiveSearch(...args: OperationRequestArgs<"tiktok-mobile-live-search">): Promise<OperationResponseMap["tiktok-mobile-live-search"]>;
  mobileMusicBeats(...args: OperationRequestArgs<"tiktok-mobile-music-beats">): Promise<OperationResponseMap["tiktok-mobile-music-beats"]>;
  mobileMusicCollections(...args: OperationRequestArgs<"tiktok-mobile-music-collections">): Promise<OperationResponseMap["tiktok-mobile-music-collections"]>;
  mobileMusicPick(...args: OperationRequestArgs<"tiktok-mobile-music-pick">): Promise<OperationResponseMap["tiktok-mobile-music-pick"]>;
  mobileMusicPosts(...args: OperationRequestArgs<"tiktok-mobile-music-posts">): Promise<OperationResponseMap["tiktok-mobile-music-posts"]>;
  mobileMusicRelated(...args: OperationRequestArgs<"tiktok-mobile-music-related">): Promise<OperationResponseMap["tiktok-mobile-music-related"]>;
  mobileMusicTrending(...args: OperationRequestArgs<"tiktok-mobile-music-trending">): Promise<OperationResponseMap["tiktok-mobile-music-trending"]>;
  mobileSearch(...args: OperationRequestArgs<"tiktok-mobile-search">): Promise<OperationResponseMap["tiktok-mobile-search"]>;
  mobileSearchMusic(...args: OperationRequestArgs<"tiktok-mobile-search-music">): Promise<OperationResponseMap["tiktok-mobile-search-music"]>;
  mobileSearchPlace(...args: OperationRequestArgs<"tiktok-mobile-search-place">): Promise<OperationResponseMap["tiktok-mobile-search-place"]>;
  mobileSearchPreInfo(...args: OperationRequestArgs<"tiktok-mobile-search-pre-info">): Promise<OperationResponseMap["tiktok-mobile-search-pre-info"]>;
  mobileSearchSug(...args: OperationRequestArgs<"tiktok-mobile-search-sug">): Promise<OperationResponseMap["tiktok-mobile-search-sug"]>;
  mobileSearchTabs(...args: OperationRequestArgs<"tiktok-mobile-search-tabs">): Promise<OperationResponseMap["tiktok-mobile-search-tabs"]>;
  mobileSearchUser(...args: OperationRequestArgs<"tiktok-mobile-search-user">): Promise<OperationResponseMap["tiktok-mobile-search-user"]>;
  mobileTrendingCategories(...args: OperationRequestArgs<"tiktok-mobile-trending-categories">): Promise<OperationResponseMap["tiktok-mobile-trending-categories"]>;
  mobileTrendingEffects(...args: OperationRequestArgs<"tiktok-mobile-trending-effects">): Promise<OperationResponseMap["tiktok-mobile-trending-effects"]>;
  popularTrendCountryIndustryMeta(...args: OperationRequestArgs<"tiktok-popular-trend-country-industry-meta">): Promise<OperationResponseMap["tiktok-popular-trend-country-industry-meta"]>;
  post(...args: OperationRequestArgs<"tiktok-post">): Promise<OperationResponseMap["tiktok-post"]>;
  profilePost(...args: OperationRequestArgs<"tiktok-profile-post">): Promise<OperationResponseMap["tiktok-profile-post"]>;
  profile(...args: OperationRequestArgs<"tiktok-profile">): Promise<OperationResponseMap["tiktok-profile"]>;
  search(...args: OperationRequestArgs<"tiktok-search">): Promise<OperationResponseMap["tiktok-search"]>;
  searchHashtag(...args: OperationRequestArgs<"tiktok-search-hashtag">): Promise<OperationResponseMap["tiktok-search-hashtag"]>;
  searchUser(...args: OperationRequestArgs<"tiktok-search-user">): Promise<OperationResponseMap["tiktok-search-user"]>;
  topAdsAnalysis(...args: OperationRequestArgs<"tiktok-top-ads-analysis">): Promise<OperationResponseMap["tiktok-top-ads-analysis"]>;
  topAdsDetail(...args: OperationRequestArgs<"tiktok-top-ads-detail">): Promise<OperationResponseMap["tiktok-top-ads-detail"]>;
  topAdsFilters(...args: OperationRequestArgs<"tiktok-top-ads-filters">): Promise<OperationResponseMap["tiktok-top-ads-filters"]>;
  topAdsList(...args: OperationRequestArgs<"tiktok-top-ads-list">): Promise<OperationResponseMap["tiktok-top-ads-list"]>;
  topAdsLocationInfo(...args: OperationRequestArgs<"tiktok-top-ads-location-info">): Promise<OperationResponseMap["tiktok-top-ads-location-info"]>;
  topAdsLocations(...args: OperationRequestArgs<"tiktok-top-ads-locations">): Promise<OperationResponseMap["tiktok-top-ads-locations"]>;
  topAdsRecommend(...args: OperationRequestArgs<"tiktok-top-ads-recommend">): Promise<OperationResponseMap["tiktok-top-ads-recommend"]>;
  topAdsSafety(...args: OperationRequestArgs<"tiktok-top-ads-safety">): Promise<OperationResponseMap["tiktok-top-ads-safety"]>;
  topAdsSpotlight(...args: OperationRequestArgs<"tiktok-top-ads-spotlight">): Promise<OperationResponseMap["tiktok-top-ads-spotlight"]>;
  topAdsSuggestions(...args: OperationRequestArgs<"tiktok-top-ads-suggestions">): Promise<OperationResponseMap["tiktok-top-ads-suggestions"]>;
  trending(...args: OperationRequestArgs<"tiktok-trending">): Promise<OperationResponseMap["tiktok-trending"]>;
}
export { TikTokClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default TikTokClient;
