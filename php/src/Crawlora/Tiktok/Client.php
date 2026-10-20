<?php

declare(strict_types=1);

namespace Crawlora\Tiktok;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'tiktok';
    public const VERSION = '0.4.0';
    public const OPERATION_COUNT = 53;
    public const OPERATION_IDS = ["tiktok-category", "tiktok-challenge", "tiktok-challenge-list", "tiktok-creative-center-filters", "tiktok-creative-center-hashtags", "tiktok-creative-center-top-content", "tiktok-creative-center-videos", "tiktok-explore", "tiktok-mobile-anchor-list", "tiktok-mobile-comment-replies", "tiktok-mobile-comments", "tiktok-mobile-feed", "tiktok-mobile-feed-post", "tiktok-mobile-hashtag", "tiktok-mobile-hashtag-posts", "tiktok-mobile-hashtags", "tiktok-mobile-live-effects", "tiktok-mobile-live-gifts", "tiktok-mobile-live-search", "tiktok-mobile-music-beats", "tiktok-mobile-music-collections", "tiktok-mobile-music-pick", "tiktok-mobile-music-posts", "tiktok-mobile-music-related", "tiktok-mobile-music-trending", "tiktok-mobile-search", "tiktok-mobile-search-music", "tiktok-mobile-search-place", "tiktok-mobile-search-pre-info", "tiktok-mobile-search-sug", "tiktok-mobile-search-tabs", "tiktok-mobile-search-user", "tiktok-mobile-trending-categories", "tiktok-mobile-trending-effects", "tiktok-popular-trend-country-industry-meta", "tiktok-post", "tiktok-profile", "tiktok-profile-post", "tiktok-search", "tiktok-search-hashtag", "tiktok-search-user", "tiktok-top-ads-analysis", "tiktok-top-ads-detail", "tiktok-top-ads-filters", "tiktok-top-ads-list", "tiktok-top-ads-location-info", "tiktok-top-ads-locations", "tiktok-top-ads-recommend", "tiktok-top-ads-safety", "tiktok-top-ads-spotlight", "tiktok-top-ads-suggestions", "tiktok-trending", "tiktok-video-comments"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"tiktok-category": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-category", "method": "GET", "params": [], "path": "/tiktok/category", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-challenge": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-challenge", "method": "GET", "params": [{"description": "Hashtag name (e.g., 'christmas')", "in": "path", "name": "name", "required": true, "type": "string", "x-example": "christmas"}], "path": "/tiktok/hashtag/{name}", "pathParams": ["name"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-challenge-list": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-challenge-list", "method": "GET", "params": [{"description": "Hashtag id returned by the hashtag detail endpoint", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "3242"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/hashtags", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-creative-center-filters": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-creative-center-filters", "method": "GET", "params": [], "path": "/tiktok/creative-center/filters", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-creative-center-hashtags": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-creative-center-hashtags", "method": "GET", "params": [{"description": "ISO-2 country code", "in": "query", "name": "country_code", "required": true, "type": "string", "x-example": "US"}, {"default": 7, "description": "Lookback window in days", "enum": [7, 30, 90], "in": "query", "name": "period", "type": "integer"}, {"description": "Creative Center industry id to restrict the ranking to", "enum": ["10000000000", "11000000000", "12000000000", "13000000000", "14000000000", "15000000000", "17000000000", "18000000000", "19000000000", "21000000000", "22000000000", "23000000000", "24000000000", "25000000000", "26000000000", "27000000000", "28000000000", "29000000000"], "in": "query", "name": "industry_id", "type": "string", "x-example": "22000000000"}], "path": "/tiktok/creative-center/hashtags", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country_code", "required": true, "type": "string"}, {"enum": ["7", "30", "90"], "in": "query", "name": "period", "type": "integer"}, {"enum": ["10000000000", "11000000000", "12000000000", "13000000000", "14000000000", "15000000000", "17000000000", "18000000000", "19000000000", "21000000000", "22000000000", "23000000000", "24000000000", "25000000000", "26000000000", "27000000000", "28000000000", "29000000000"], "in": "query", "name": "industry_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-creative-center-top-content": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-creative-center-top-content", "method": "GET", "params": [{"default": true, "description": "Include each object's top comments and comment-keyword counts", "in": "query", "name": "include_comments", "type": "boolean"}], "path": "/tiktok/creative-center/top-content", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "include_comments", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "tiktok-creative-center-videos": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-creative-center-videos", "method": "GET", "params": [{"description": "ISO-2 country code", "in": "query", "name": "country_code", "required": true, "type": "string", "x-example": "US"}, {"default": 7, "description": "Lookback window in days", "enum": [7, 30], "in": "query", "name": "period", "type": "integer"}, {"default": "views", "description": "Sort order", "enum": ["views", "engagement", "six_second_views"], "in": "query", "name": "sort_by", "type": "string"}, {"description": "Deprecated: single content tag id; use content_label_ids instead", "in": "query", "name": "content_label_id", "type": "string", "x-example": "11015"}, {"collectionFormat": "multi", "description": "Content tag ids to filter by, repeatable; matches videos carrying any selected tag", "in": "query", "items": {"enum": ["11002", "11003", "11010", "11013", "11015"], "type": "string"}, "name": "content_label_ids", "type": "array", "x-example": "11003,11015"}, {"default": false, "description": "Restrict to organic (non-paid) videos only", "in": "query", "name": "organic_only", "type": "boolean"}], "path": "/tiktok/creative-center/videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country_code", "required": true, "type": "string"}, {"enum": ["7", "30"], "in": "query", "name": "period", "type": "integer"}, {"enum": ["views", "engagement", "six_second_views"], "in": "query", "name": "sort_by", "type": "string"}, {"in": "query", "name": "content_label_id", "type": "string"}, {"collectionFormat": "multi", "enum": ["11002", "11003", "11010", "11013", "11015"], "in": "query", "name": "content_label_ids", "type": "array"}, {"in": "query", "name": "organic_only", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "tiktok-explore": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-explore", "method": "GET", "params": [{"description": "Category type id returned by the category endpoint", "in": "path", "name": "id", "required": true, "type": "integer", "x-example": 120}], "path": "/tiktok/explore/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-mobile-anchor-list": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-anchor-list", "method": "GET", "params": [], "path": "/tiktok/mobile/anchor/list", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-mobile-comment-replies": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-comment-replies", "method": "GET", "params": [{"description": "Video id the comment belongs to", "in": "query", "name": "aweme_id", "required": true, "type": "string", "x-example": "7680168962218511636"}, {"description": "Comment id to list replies for", "in": "query", "name": "comment_id", "required": true, "type": "string", "x-example": "7680523330713240340"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}, {"default": 20, "description": "Replies per page (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/comment/replies", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "aweme_id", "required": true, "type": "string"}, {"in": "query", "name": "comment_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-comments": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-comments", "method": "GET", "params": [{"description": "Video id to list comments for", "in": "query", "name": "aweme_id", "required": true, "type": "string", "x-example": "7681236055831416084"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}, {"default": 20, "description": "Comments per page (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/comments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "aweme_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-feed": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-feed", "method": "GET", "params": [{"default": 0, "description": "Videos to request (0 = app default, max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/feed", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-feed-post": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-feed-post", "method": "GET", "params": [], "path": "/tiktok/mobile/feed/post", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-mobile-hashtag": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-hashtag", "method": "GET", "params": [{"description": "Hashtag name without the leading #", "in": "query", "name": "name", "required": true, "type": "string", "x-example": "readingvlog"}], "path": "/tiktok/mobile/hashtag", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "name", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-hashtag-posts": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-hashtag-posts", "method": "GET", "params": [{"description": "Hashtag name without the leading #", "in": "query", "name": "name", "required": true, "type": "string", "x-example": "readingvlog"}, {"default": "fresh", "description": "Listing: fresh (newest) or popular (hot)", "enum": ["fresh", "popular"], "in": "query", "name": "sort", "type": "string"}, {"default": 20, "description": "Videos per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/hashtag/posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "name", "required": true, "type": "string"}, {"enum": ["fresh", "popular"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-hashtags": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-hashtags", "method": "GET", "params": [{"description": "Keyword to search hashtags for", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "reading"}, {"default": 20, "description": "Results per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/hashtags", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-live-effects": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-live-effects", "method": "GET", "params": [], "path": "/tiktok/mobile/live/effects", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-mobile-live-gifts": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-live-gifts", "method": "GET", "params": [], "path": "/tiktok/mobile/live/gifts", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-mobile-live-search": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-live-search", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}, {"default": 0, "description": "Results to request (0 = app default, max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/live/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-beats": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-beats", "method": "GET", "params": [{"default": 0, "description": "Accepted for compatibility; not measured to change the page (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/music/beats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-collections": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-collections", "method": "GET", "params": [{"default": 0, "description": "Collections to request (0 = app default, max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Accepted for shape compatibility only; not a verified page token", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/music/collections", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-pick": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-pick", "method": "GET", "params": [{"default": 20, "description": "Sounds per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/music/pick", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-posts": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-posts", "method": "GET", "params": [{"description": "Sound (music) id", "in": "query", "name": "music_id", "required": true, "type": "string", "x-example": "6799585653702019073"}, {"default": 0, "description": "Accepted for compatibility; the server ignores it (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/music/posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "music_id", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-related": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-related", "method": "GET", "params": [{"description": "Video id to find related sounds for", "in": "query", "name": "aweme_id", "required": true, "type": "string", "x-example": "7681236055831416084"}, {"default": 20, "description": "Sounds per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/music/related", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "aweme_id", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-music-trending": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-music-trending", "method": "GET", "params": [{"default": 20, "description": "Sounds per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/music/trending", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}, {"default": 5, "description": "Results per page (max 20)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Result offset", "in": "query", "name": "offset", "type": "integer"}], "path": "/tiktok/mobile/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-music": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-music", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}, {"default": 20, "description": "Sounds per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Result offset", "in": "query", "name": "offset", "type": "integer"}], "path": "/tiktok/mobile/search/music", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-place": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-place", "method": "GET", "params": [{"description": "Place name or category to search for", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "pizza"}, {"default": 10, "description": "Rows to return; the upstream caps the page at 10 regardless", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/search/place", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-pre-info": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-pre-info", "method": "GET", "params": [{"description": "Seed keyword (optional; the app also requests this with an empty keyword)", "in": "query", "name": "keyword", "type": "string", "x-example": "lofi"}, {"default": 20, "description": "Suggestion count (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/search/pre-info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "type": "string"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-sug": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-sug", "method": "GET", "params": [{"description": "Seed keyword to expand", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}, {"default": 10, "description": "Suggestions to return (max 50)", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/mobile/search/sug", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-tabs": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-tabs", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "lofi"}], "path": "/tiktok/mobile/search/tabs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-search-user": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-search-user", "method": "GET", "params": [{"description": "Search keyword (a username or display name)", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "mrbeast"}, {"default": 20, "description": "Users per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/search/user", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-trending-categories": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-trending-categories", "method": "GET", "params": [{"default": 20, "description": "Categories per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/trending/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-mobile-trending-effects": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-mobile-trending-effects", "method": "GET", "params": [{"default": 20, "description": "Videos per page (max 50)", "in": "query", "name": "count", "type": "integer"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/mobile/trending/effects", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-popular-trend-country-industry-meta": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-popular-trend-country-industry-meta", "method": "GET", "params": [], "path": "/tiktok/popular-trend/country-industry-meta", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-post": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-post", "method": "GET", "params": [{"description": "TikTok video id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "7444278905264983342"}], "path": "/tiktok/post/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-profile": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-profile", "method": "GET", "params": [{"description": "TikTok handle without the leading @", "in": "path", "name": "handler", "required": true, "type": "string", "x-example": "chatgpt"}], "path": "/tiktok/profile/{handler}", "pathParams": ["handler"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-profile-post": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-profile-post", "method": "GET", "params": [{"description": "TikTok secUid for the profile", "in": "query", "name": "secUid", "required": true, "type": "string", "x-example": "MS4wLjABAAAAT4vq3vsh9X-Vb_WtV6tz4QWTbKjliTKCiK5DqnJNtQEA2RUveHb7UdnL7xgPK2HB"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}, {"default": 0, "description": "Sort mode: 0 latest, 1 popular, 2 oldest", "enum": [0, 1, 2], "in": "query", "name": "sort_type", "type": "integer"}], "path": "/tiktok/posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "secUid", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"enum": ["0", "1", "2"], "in": "query", "name": "sort_type", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-search": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-search", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "dance"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}, {"default": 20, "description": "Result count, clamped to 50", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-search-hashtag": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-search-hashtag", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "chatgpt"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}, {"default": 20, "description": "Result count, clamped to 50", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/search/hashtag", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-search-user": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-search-user", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "chatgpt"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/search/user", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-analysis": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-top-ads-analysis", "method": "GET", "params": [{"description": "Top Ads material id", "in": "query", "name": "material_id", "required": true, "type": "string", "x-example": "7130614705291427842"}, {"default": "retain_ctr", "description": "Interactive time analysis metric", "enum": ["retain_ctr", "retain_cvr", "click_cnt", "convert_cnt", "play_retain_cnt"], "in": "query", "name": "metric", "type": "string"}, {"default": 7, "description": "Percentile lookback period in days", "enum": [7, 30, 180], "in": "query", "name": "period_type", "type": "integer"}], "path": "/tiktok/top-ads/analysis", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "material_id", "required": true, "type": "string"}, {"enum": ["retain_ctr", "retain_cvr", "click_cnt", "convert_cnt", "play_retain_cnt"], "in": "query", "name": "metric", "type": "string"}, {"enum": ["7", "30", "180"], "in": "query", "name": "period_type", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-detail": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-top-ads-detail", "method": "GET", "params": [{"description": "Top Ads material id", "in": "query", "name": "material_id", "required": true, "type": "string", "x-example": "7631130810943897607"}], "path": "/tiktok/top-ads/detail", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "material_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-filters": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-top-ads-filters", "method": "GET", "params": [], "path": "/tiktok/top-ads/filters", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-list": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-top-ads-list", "method": "GET", "params": [{"default": 30, "description": "Lookback period in days", "enum": [7, 30, 180], "in": "query", "name": "period", "type": "integer"}, {"default": 1, "description": "Page number", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"default": 20, "description": "Maximum number of ads to return", "in": "query", "maximum": 100, "name": "limit", "type": "integer"}, {"default": "for_you", "description": "Sort order", "enum": ["for_you", "impression", "ctr", "play_2s_rate", "play_6s_rate", "cvr", "like"], "in": "query", "name": "order_by", "type": "string"}, {"description": "Country code or comma-separated country codes from /tiktok/top-ads/filters", "in": "query", "name": "country_code", "type": "string", "x-example": "US"}, {"description": "Brand or product keyword search", "in": "query", "name": "keyword", "type": "string", "x-example": "coffee"}, {"description": "Industry filter id or comma-separated ids from /tiktok/top-ads/filters", "in": "query", "name": "industry", "type": "string", "x-example": "23118000000"}, {"description": "Objective filter id or comma-separated ids from /tiktok/top-ads/filters", "in": "query", "name": "objective", "type": "string", "x-example": "3"}, {"description": "Ad language id or comma-separated ids from /tiktok/top-ads/filters", "in": "query", "name": "ad_language", "type": "string", "x-example": "en"}, {"description": "Pattern label id or comma-separated ids from /tiktok/top-ads/filters", "in": "query", "name": "pattern_label", "type": "string", "x-example": "10100100000"}, {"description": "Video duration bucket", "enum": ["time-2", "time-3", "time-4", "time-5", "time-6", "time-7"], "in": "query", "name": "duration", "type": "string"}, {"description": "Like percentile bucket id or comma-separated ids", "enum": ["1", "2", "3", "4", "5"], "in": "query", "name": "like", "type": "string"}, {"description": "Ad format id", "enum": ["1", "2"], "in": "query", "name": "ad_format", "type": "string"}], "path": "/tiktok/top-ads/list", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["7", "30", "180"], "in": "query", "name": "period", "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"enum": ["for_you", "impression", "ctr", "play_2s_rate", "play_6s_rate", "cvr", "like"], "in": "query", "name": "order_by", "type": "string"}, {"in": "query", "name": "country_code", "type": "string"}, {"in": "query", "name": "keyword", "type": "string"}, {"in": "query", "name": "industry", "type": "string"}, {"in": "query", "name": "objective", "type": "string"}, {"in": "query", "name": "ad_language", "type": "string"}, {"in": "query", "name": "pattern_label", "type": "string"}, {"enum": ["time-2", "time-3", "time-4", "time-5", "time-6", "time-7"], "in": "query", "name": "duration", "type": "string"}, {"enum": ["1", "2", "3", "4", "5"], "in": "query", "name": "like", "type": "string"}, {"enum": ["1", "2"], "in": "query", "name": "ad_format", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-location-info": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-top-ads-location-info", "method": "GET", "params": [{"default": 1, "description": "Optional upstream Creative Center module identifier; omitted or 0 defaults to 1, other nonzero IDs are passed through without local range validation", "in": "query", "name": "module", "type": "integer"}], "path": "/tiktok/top-ads/location-info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "module", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-locations": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-top-ads-locations", "method": "GET", "params": [], "path": "/tiktok/top-ads/locations", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-recommend": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-top-ads-recommend", "method": "GET", "params": [{"description": "Top Ads material id", "in": "query", "name": "material_id", "required": true, "type": "string", "x-example": "7631130810943897607"}, {"default": 1, "description": "Page number", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"default": 20, "description": "Maximum number of ads to return", "in": "query", "maximum": 100, "name": "limit", "type": "integer"}], "path": "/tiktok/top-ads/recommend", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "material_id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-safety": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-top-ads-safety", "method": "GET", "params": [], "path": "/tiktok/top-ads/safety", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-spotlight": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-top-ads-spotlight", "method": "GET", "params": [{"default": 1, "description": "Page number", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"default": 20, "description": "Maximum number of ads to return", "in": "query", "maximum": 100, "name": "limit", "type": "integer"}], "path": "/tiktok/top-ads/spotlight", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-suggestions": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-top-ads-suggestions", "method": "GET", "params": [{"default": 50, "description": "Maximum number of suggestions to return", "in": "query", "name": "count", "type": "integer"}, {"default": 1, "description": "Suggestion scenario id", "in": "query", "name": "scenario", "type": "integer"}], "path": "/tiktok/top-ads/suggestions", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "scenario", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-trending": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-trending", "method": "GET", "params": [], "path": "/tiktok/trending", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-video-comments": {"bodyParam": null, "bodyRequired": false, "id": "tiktok-video-comments", "method": "GET", "params": [{"description": "TikTok video id from the video URL", "in": "query", "name": "aweme_id", "required": true, "type": "string", "x-example": "7304809083817774382"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/comments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "aweme_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-tiktok-php/0.4.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function category(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-category", $params, $responseType);
    }
    public function video_comments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-video-comments", $params, $responseType);
    }
    public function creative_center_filters(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-creative-center-filters", $params, $responseType);
    }
    public function creative_center_hashtags(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-creative-center-hashtags", $params, $responseType);
    }
    public function creative_center_top_content(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-creative-center-top-content", $params, $responseType);
    }
    public function creative_center_videos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-creative-center-videos", $params, $responseType);
    }
    public function explore(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-explore", $params, $responseType);
    }
    public function challenge(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-challenge", $params, $responseType);
    }
    public function challenge_list(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-challenge-list", $params, $responseType);
    }
    public function mobile_anchor_list(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-anchor-list", $params, $responseType);
    }
    public function mobile_comment_replies(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-comment-replies", $params, $responseType);
    }
    public function mobile_comments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-comments", $params, $responseType);
    }
    public function mobile_feed(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-feed", $params, $responseType);
    }
    public function mobile_feed_post(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-feed-post", $params, $responseType);
    }
    public function mobile_hashtag(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-hashtag", $params, $responseType);
    }
    public function mobile_hashtag_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-hashtag-posts", $params, $responseType);
    }
    public function mobile_hashtags(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-hashtags", $params, $responseType);
    }
    public function mobile_live_effects(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-live-effects", $params, $responseType);
    }
    public function mobile_live_gifts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-live-gifts", $params, $responseType);
    }
    public function mobile_live_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-live-search", $params, $responseType);
    }
    public function mobile_music_beats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-beats", $params, $responseType);
    }
    public function mobile_music_collections(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-collections", $params, $responseType);
    }
    public function mobile_music_pick(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-pick", $params, $responseType);
    }
    public function mobile_music_posts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-posts", $params, $responseType);
    }
    public function mobile_music_related(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-related", $params, $responseType);
    }
    public function mobile_music_trending(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-music-trending", $params, $responseType);
    }
    public function mobile_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search", $params, $responseType);
    }
    public function mobile_search_music(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-music", $params, $responseType);
    }
    public function mobile_search_place(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-place", $params, $responseType);
    }
    public function mobile_search_pre_info(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-pre-info", $params, $responseType);
    }
    public function mobile_search_sug(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-sug", $params, $responseType);
    }
    public function mobile_search_tabs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-tabs", $params, $responseType);
    }
    public function mobile_search_user(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-search-user", $params, $responseType);
    }
    public function mobile_trending_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-trending-categories", $params, $responseType);
    }
    public function mobile_trending_effects(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-mobile-trending-effects", $params, $responseType);
    }
    public function popular_trend_country_industry_meta(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-popular-trend-country-industry-meta", $params, $responseType);
    }
    public function post(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-post", $params, $responseType);
    }
    public function profile_post(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-profile-post", $params, $responseType);
    }
    public function profile(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-profile", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-search", $params, $responseType);
    }
    public function search_hashtag(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-search-hashtag", $params, $responseType);
    }
    public function search_user(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-search-user", $params, $responseType);
    }
    public function top_ads_analysis(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-top-ads-analysis", $params, $responseType);
    }
    public function top_ads_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-top-ads-detail", $params, $responseType);
    }
    public function top_ads_filters(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-top-ads-filters", $params, $responseType);
    }
    public function top_ads_list(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-top-ads-list", $params, $responseType);
    }
    public function top_ads_location_info(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-top-ads-location-info", $params, $responseType);
    }
    public function top_ads_locations(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-top-ads-locations", $params, $responseType);
    }
    public function top_ads_recommend(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-top-ads-recommend", $params, $responseType);
    }
    public function top_ads_safety(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-top-ads-safety", $params, $responseType);
    }
    public function top_ads_spotlight(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-top-ads-spotlight", $params, $responseType);
    }
    public function top_ads_suggestions(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-top-ads-suggestions", $params, $responseType);
    }
    public function trending(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("tiktok-trending", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
