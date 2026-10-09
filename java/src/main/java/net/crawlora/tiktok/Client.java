package net.crawlora.tiktok;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the TikTok endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 25;
    public static final List<String> OPERATION_IDS = List.of(
            "tiktok-category",
            "tiktok-challenge",
            "tiktok-challenge-list",
            "tiktok-creative-center-hashtags",
            "tiktok-creative-center-videos",
            "tiktok-explore",
            "tiktok-popular-trend-country-industry-meta",
            "tiktok-post",
            "tiktok-profile",
            "tiktok-profile-post",
            "tiktok-search",
            "tiktok-search-hashtag",
            "tiktok-search-user",
            "tiktok-top-ads-analysis",
            "tiktok-top-ads-detail",
            "tiktok-top-ads-filters",
            "tiktok-top-ads-list",
            "tiktok-top-ads-location-info",
            "tiktok-top-ads-locations",
            "tiktok-top-ads-recommend",
            "tiktok-top-ads-safety",
            "tiktok-top-ads-spotlight",
            "tiktok-top-ads-suggestions",
            "tiktok-trending",
            "tiktok-video-comments"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("tiktok-category", new Operation("tiktok-category", "GET", "/tiktok/category", Map.of(), List.of("application/json")));
        operations.put("tiktok-video-comments", new Operation("tiktok-video-comments", "GET", "/tiktok/comments", Map.ofEntries(Map.entry("aweme_id", new Param("aweme_id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-creative-center-hashtags", new Operation("tiktok-creative-center-hashtags", "GET", "/tiktok/creative-center/hashtags", Map.ofEntries(Map.entry("country_code", new Param("country_code", "query", true, "string", List.of(), "csv")), Map.entry("period", new Param("period", "query", false, "integer", List.of("7", "30"), "csv"))), List.of("application/json")));
        operations.put("tiktok-creative-center-videos", new Operation("tiktok-creative-center-videos", "GET", "/tiktok/creative-center/videos", Map.ofEntries(Map.entry("country_code", new Param("country_code", "query", true, "string", List.of(), "csv")), Map.entry("period", new Param("period", "query", false, "integer", List.of("7", "30"), "csv")), Map.entry("sort_by", new Param("sort_by", "query", false, "string", List.of("views", "engagement", "six_second_views"), "csv")), Map.entry("content_label_id", new Param("content_label_id", "query", false, "string", List.of(), "csv")), Map.entry("organic_only", new Param("organic_only", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-explore", new Operation("tiktok-explore", "GET", "/tiktok/explore/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-challenge", new Operation("tiktok-challenge", "GET", "/tiktok/hashtag/{name}", Map.ofEntries(Map.entry("name", new Param("name", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-challenge-list", new Operation("tiktok-challenge-list", "GET", "/tiktok/hashtags", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-popular-trend-country-industry-meta", new Operation("tiktok-popular-trend-country-industry-meta", "GET", "/tiktok/popular-trend/country-industry-meta", Map.of(), List.of("application/json")));
        operations.put("tiktok-post", new Operation("tiktok-post", "GET", "/tiktok/post/{id}", Map.ofEntries(Map.entry("id", new Param("id", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-profile-post", new Operation("tiktok-profile-post", "GET", "/tiktok/posts", Map.ofEntries(Map.entry("secUid", new Param("secUid", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("sort_type", new Param("sort_type", "query", false, "integer", List.of("0", "1", "2"), "csv"))), List.of("application/json")));
        operations.put("tiktok-profile", new Operation("tiktok-profile", "GET", "/tiktok/profile/{handler}", Map.ofEntries(Map.entry("handler", new Param("handler", "path", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-search", new Operation("tiktok-search", "GET", "/tiktok/search", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-search-hashtag", new Operation("tiktok-search-hashtag", "GET", "/tiktok/search/hashtag", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv")), Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-search-user", new Operation("tiktok-search-user", "GET", "/tiktok/search/user", Map.ofEntries(Map.entry("keyword", new Param("keyword", "query", true, "string", List.of(), "csv")), Map.entry("cursor", new Param("cursor", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-top-ads-analysis", new Operation("tiktok-top-ads-analysis", "GET", "/tiktok/top-ads/analysis", Map.ofEntries(Map.entry("material_id", new Param("material_id", "query", true, "string", List.of(), "csv")), Map.entry("metric", new Param("metric", "query", false, "string", List.of("retain_ctr", "retain_cvr", "click_cnt", "convert_cnt", "play_retain_cnt"), "csv")), Map.entry("period_type", new Param("period_type", "query", false, "integer", List.of("7", "30", "180"), "csv"))), List.of("application/json")));
        operations.put("tiktok-top-ads-detail", new Operation("tiktok-top-ads-detail", "GET", "/tiktok/top-ads/detail", Map.ofEntries(Map.entry("material_id", new Param("material_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-top-ads-filters", new Operation("tiktok-top-ads-filters", "GET", "/tiktok/top-ads/filters", Map.of(), List.of("application/json")));
        operations.put("tiktok-top-ads-list", new Operation("tiktok-top-ads-list", "GET", "/tiktok/top-ads/list", Map.ofEntries(Map.entry("period", new Param("period", "query", false, "integer", List.of("7", "30", "180"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("order_by", new Param("order_by", "query", false, "string", List.of("for_you", "impression", "ctr", "play_2s_rate", "play_6s_rate", "cvr", "like"), "csv")), Map.entry("country_code", new Param("country_code", "query", false, "string", List.of(), "csv")), Map.entry("keyword", new Param("keyword", "query", false, "string", List.of(), "csv")), Map.entry("industry", new Param("industry", "query", false, "string", List.of(), "csv")), Map.entry("objective", new Param("objective", "query", false, "string", List.of(), "csv")), Map.entry("ad_language", new Param("ad_language", "query", false, "string", List.of(), "csv")), Map.entry("pattern_label", new Param("pattern_label", "query", false, "string", List.of(), "csv")), Map.entry("duration", new Param("duration", "query", false, "string", List.of("time-2", "time-3", "time-4", "time-5", "time-6", "time-7"), "csv")), Map.entry("like", new Param("like", "query", false, "string", List.of("1", "2", "3", "4", "5"), "csv")), Map.entry("ad_format", new Param("ad_format", "query", false, "string", List.of("1", "2"), "csv"))), List.of("application/json")));
        operations.put("tiktok-top-ads-location-info", new Operation("tiktok-top-ads-location-info", "GET", "/tiktok/top-ads/location-info", Map.ofEntries(Map.entry("module", new Param("module", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-top-ads-locations", new Operation("tiktok-top-ads-locations", "GET", "/tiktok/top-ads/locations", Map.of(), List.of("application/json")));
        operations.put("tiktok-top-ads-recommend", new Operation("tiktok-top-ads-recommend", "GET", "/tiktok/top-ads/recommend", Map.ofEntries(Map.entry("material_id", new Param("material_id", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-top-ads-safety", new Operation("tiktok-top-ads-safety", "GET", "/tiktok/top-ads/safety", Map.of(), List.of("application/json")));
        operations.put("tiktok-top-ads-spotlight", new Operation("tiktok-top-ads-spotlight", "GET", "/tiktok/top-ads/spotlight", Map.ofEntries(Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-top-ads-suggestions", new Operation("tiktok-top-ads-suggestions", "GET", "/tiktok/top-ads/suggestions", Map.ofEntries(Map.entry("count", new Param("count", "query", false, "integer", List.of(), "csv")), Map.entry("scenario", new Param("scenario", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("tiktok-trending", new Operation("tiktok-trending", "GET", "/tiktok/trending", Map.of(), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown TikTok operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest request = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation))
                .GET().build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object category(Map<String, ?> params) { return request("tiktok-category", params); }
    public Object videoComments(Map<String, ?> params) { return request("tiktok-video-comments", params); }
    public Object creativeCenterHashtags(Map<String, ?> params) { return request("tiktok-creative-center-hashtags", params); }
    public Object creativeCenterVideos(Map<String, ?> params) { return request("tiktok-creative-center-videos", params); }
    public Object explore(Map<String, ?> params) { return request("tiktok-explore", params); }
    public Object challenge(Map<String, ?> params) { return request("tiktok-challenge", params); }
    public Object challengeList(Map<String, ?> params) { return request("tiktok-challenge-list", params); }
    public Object popularTrendCountryIndustryMeta(Map<String, ?> params) { return request("tiktok-popular-trend-country-industry-meta", params); }
    public Object post(Map<String, ?> params) { return request("tiktok-post", params); }
    public Object profilePost(Map<String, ?> params) { return request("tiktok-profile-post", params); }
    public Object profile(Map<String, ?> params) { return request("tiktok-profile", params); }
    public Object search(Map<String, ?> params) { return request("tiktok-search", params); }
    public Object searchHashtag(Map<String, ?> params) { return request("tiktok-search-hashtag", params); }
    public Object searchUser(Map<String, ?> params) { return request("tiktok-search-user", params); }
    public Object topAdsAnalysis(Map<String, ?> params) { return request("tiktok-top-ads-analysis", params); }
    public Object topAdsDetail(Map<String, ?> params) { return request("tiktok-top-ads-detail", params); }
    public Object topAdsFilters(Map<String, ?> params) { return request("tiktok-top-ads-filters", params); }
    public Object topAdsList(Map<String, ?> params) { return request("tiktok-top-ads-list", params); }
    public Object topAdsLocationInfo(Map<String, ?> params) { return request("tiktok-top-ads-location-info", params); }
    public Object topAdsLocations(Map<String, ?> params) { return request("tiktok-top-ads-locations", params); }
    public Object topAdsRecommend(Map<String, ?> params) { return request("tiktok-top-ads-recommend", params); }
    public Object topAdsSafety(Map<String, ?> params) { return request("tiktok-top-ads-safety", params); }
    public Object topAdsSpotlight(Map<String, ?> params) { return request("tiktok-top-ads-spotlight", params); }
    public Object topAdsSuggestions(Map<String, ?> params) { return request("tiktok-top-ads-suggestions", params); }
    public Object trending(Map<String, ?> params) { return request("tiktok-trending", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
