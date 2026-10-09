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
  creativeCenterHashtags(params: OperationParamsMap["tiktok-creative-center-hashtags"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  creativeCenterVideos(params: OperationParamsMap["tiktok-creative-center-videos"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  explore(params: OperationParamsMap["tiktok-explore"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  challenge(params: OperationParamsMap["tiktok-challenge"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  challengeList(params: OperationParamsMap["tiktok-challenge-list"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
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
  creativeCenterHashtags(params: OperationParamsMap["tiktok-creative-center-hashtags"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  creativeCenterVideos(params: OperationParamsMap["tiktok-creative-center-videos"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  explore(params: OperationParamsMap["tiktok-explore"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  challenge(params: OperationParamsMap["tiktok-challenge"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  challengeList(params: OperationParamsMap["tiktok-challenge-list"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
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
  creativeCenterHashtags(...args: OperationRequestArgs<"tiktok-creative-center-hashtags">): Promise<OperationResponseMap["tiktok-creative-center-hashtags"]>;
  creativeCenterVideos(...args: OperationRequestArgs<"tiktok-creative-center-videos">): Promise<OperationResponseMap["tiktok-creative-center-videos"]>;
  explore(...args: OperationRequestArgs<"tiktok-explore">): Promise<OperationResponseMap["tiktok-explore"]>;
  challenge(...args: OperationRequestArgs<"tiktok-challenge">): Promise<OperationResponseMap["tiktok-challenge"]>;
  challengeList(...args: OperationRequestArgs<"tiktok-challenge-list">): Promise<OperationResponseMap["tiktok-challenge-list"]>;
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
