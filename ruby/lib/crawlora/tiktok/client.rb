require "json"
require "net/http"
require "uri"

module Crawlora
  module Tiktok
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"tiktok-category": {"id": "tiktok-category", "method": "GET", "params": [], "path": "/tiktok/category", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-challenge": {"id": "tiktok-challenge", "method": "GET", "params": [{"description": "Hashtag name (e.g., 'christmas')", "in": "path", "name": "name", "required": true, "type": "string", "x-example": "christmas"}], "path": "/tiktok/hashtag/{name}", "pathParams": ["name"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-challenge-list": {"id": "tiktok-challenge-list", "method": "GET", "params": [{"description": "Hashtag id returned by the hashtag detail endpoint", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "3242"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/hashtags", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-creative-center-hashtags": {"id": "tiktok-creative-center-hashtags", "method": "GET", "params": [{"description": "ISO-2 country code", "in": "query", "name": "country_code", "required": true, "type": "string", "x-example": "US"}, {"default": 7, "description": "Lookback window in days", "enum": [7, 30], "in": "query", "name": "period", "type": "integer"}], "path": "/tiktok/creative-center/hashtags", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country_code", "required": true, "type": "string"}, {"enum": ["7", "30"], "in": "query", "name": "period", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-creative-center-videos": {"id": "tiktok-creative-center-videos", "method": "GET", "params": [{"description": "ISO-2 country code", "in": "query", "name": "country_code", "required": true, "type": "string", "x-example": "US"}, {"default": 7, "description": "Lookback window in days", "enum": [7, 30], "in": "query", "name": "period", "type": "integer"}, {"default": "views", "description": "Sort order", "enum": ["views", "engagement", "six_second_views"], "in": "query", "name": "sort_by", "type": "string"}, {"description": "Content tag id to filter by", "in": "query", "name": "content_label_id", "type": "string", "x-example": "11015"}, {"default": false, "description": "Restrict to organic (non-paid) videos only", "in": "query", "name": "organic_only", "type": "boolean"}], "path": "/tiktok/creative-center/videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "country_code", "required": true, "type": "string"}, {"enum": ["7", "30"], "in": "query", "name": "period", "type": "integer"}, {"enum": ["views", "engagement", "six_second_views"], "in": "query", "name": "sort_by", "type": "string"}, {"in": "query", "name": "content_label_id", "type": "string"}, {"in": "query", "name": "organic_only", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "tiktok-explore": {"id": "tiktok-explore", "method": "GET", "params": [{"description": "Category type id returned by the category endpoint", "in": "path", "name": "id", "required": true, "type": "integer", "x-example": 120}], "path": "/tiktok/explore/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-popular-trend-country-industry-meta": {"id": "tiktok-popular-trend-country-industry-meta", "method": "GET", "params": [], "path": "/tiktok/popular-trend/country-industry-meta", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-post": {"id": "tiktok-post", "method": "GET", "params": [{"description": "TikTok video id", "in": "path", "name": "id", "required": true, "type": "string", "x-example": "7444278905264983342"}], "path": "/tiktok/post/{id}", "pathParams": ["id"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-profile": {"id": "tiktok-profile", "method": "GET", "params": [{"description": "TikTok handle without the leading @", "in": "path", "name": "handler", "required": true, "type": "string", "x-example": "chatgpt"}], "path": "/tiktok/profile/{handler}", "pathParams": ["handler"], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-profile-post": {"id": "tiktok-profile-post", "method": "GET", "params": [{"description": "TikTok secUid for the profile", "in": "query", "name": "secUid", "required": true, "type": "string", "x-example": "MS4wLjABAAAAT4vq3vsh9X-Vb_WtV6tz4QWTbKjliTKCiK5DqnJNtQEA2RUveHb7UdnL7xgPK2HB"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}, {"default": 0, "description": "Sort mode: 0 latest, 1 popular, 2 oldest", "enum": [0, 1, 2], "in": "query", "name": "sort_type", "type": "integer"}], "path": "/tiktok/posts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "secUid", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"enum": ["0", "1", "2"], "in": "query", "name": "sort_type", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-search": {"id": "tiktok-search", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "dance"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}, {"default": 20, "description": "Result count, clamped to 50", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-search-hashtag": {"id": "tiktok-search-hashtag", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "chatgpt"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}, {"default": 20, "description": "Result count, clamped to 50", "in": "query", "name": "count", "type": "integer"}], "path": "/tiktok/search/hashtag", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-search-user": {"id": "tiktok-search-user", "method": "GET", "params": [{"description": "Search keyword", "in": "query", "name": "keyword", "required": true, "type": "string", "x-example": "chatgpt"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/search/user", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "keyword", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-analysis": {"id": "tiktok-top-ads-analysis", "method": "GET", "params": [{"description": "Top Ads material id", "in": "query", "name": "material_id", "required": true, "type": "string", "x-example": "7130614705291427842"}, {"default": "retain_ctr", "description": "Interactive time analysis metric", "enum": ["retain_ctr", "retain_cvr", "click_cnt", "convert_cnt", "play_retain_cnt"], "in": "query", "name": "metric", "type": "string"}, {"default": 7, "description": "Percentile lookback period in days", "enum": [7, 30, 180], "in": "query", "name": "period_type", "type": "integer"}], "path": "/tiktok/top-ads/analysis", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "material_id", "required": true, "type": "string"}, {"enum": ["retain_ctr", "retain_cvr", "click_cnt", "convert_cnt", "play_retain_cnt"], "in": "query", "name": "metric", "type": "string"}, {"enum": ["7", "30", "180"], "in": "query", "name": "period_type", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-detail": {"id": "tiktok-top-ads-detail", "method": "GET", "params": [{"description": "Top Ads material id", "in": "query", "name": "material_id", "required": true, "type": "string", "x-example": "7631130810943897607"}], "path": "/tiktok/top-ads/detail", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "material_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-filters": {"id": "tiktok-top-ads-filters", "method": "GET", "params": [], "path": "/tiktok/top-ads/filters", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-list": {"id": "tiktok-top-ads-list", "method": "GET", "params": [{"default": 30, "description": "Lookback period in days", "enum": [7, 30, 180], "in": "query", "name": "period", "type": "integer"}, {"default": 1, "description": "Page number", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"default": 20, "description": "Maximum number of ads to return", "in": "query", "maximum": 100, "name": "limit", "type": "integer"}, {"default": "for_you", "description": "Sort order", "enum": ["for_you", "impression", "ctr", "play_2s_rate", "play_6s_rate", "cvr", "like"], "in": "query", "name": "order_by", "type": "string"}, {"description": "Country code or comma-separated country codes from /tiktok/top-ads/filters", "in": "query", "name": "country_code", "type": "string", "x-example": "US"}, {"description": "Brand or product keyword search", "in": "query", "name": "keyword", "type": "string", "x-example": "coffee"}, {"description": "Industry filter id or comma-separated ids from /tiktok/top-ads/filters", "in": "query", "name": "industry", "type": "string", "x-example": "23118000000"}, {"description": "Objective filter id or comma-separated ids from /tiktok/top-ads/filters", "in": "query", "name": "objective", "type": "string", "x-example": "3"}, {"description": "Ad language id or comma-separated ids from /tiktok/top-ads/filters", "in": "query", "name": "ad_language", "type": "string", "x-example": "en"}, {"description": "Pattern label id or comma-separated ids from /tiktok/top-ads/filters", "in": "query", "name": "pattern_label", "type": "string", "x-example": "10100100000"}, {"description": "Video duration bucket", "enum": ["time-2", "time-3", "time-4", "time-5", "time-6", "time-7"], "in": "query", "name": "duration", "type": "string"}, {"description": "Like percentile bucket id or comma-separated ids", "enum": ["1", "2", "3", "4", "5"], "in": "query", "name": "like", "type": "string"}, {"description": "Ad format id", "enum": ["1", "2"], "in": "query", "name": "ad_format", "type": "string"}], "path": "/tiktok/top-ads/list", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["7", "30", "180"], "in": "query", "name": "period", "type": "integer"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"enum": ["for_you", "impression", "ctr", "play_2s_rate", "play_6s_rate", "cvr", "like"], "in": "query", "name": "order_by", "type": "string"}, {"in": "query", "name": "country_code", "type": "string"}, {"in": "query", "name": "keyword", "type": "string"}, {"in": "query", "name": "industry", "type": "string"}, {"in": "query", "name": "objective", "type": "string"}, {"in": "query", "name": "ad_language", "type": "string"}, {"in": "query", "name": "pattern_label", "type": "string"}, {"enum": ["time-2", "time-3", "time-4", "time-5", "time-6", "time-7"], "in": "query", "name": "duration", "type": "string"}, {"enum": ["1", "2", "3", "4", "5"], "in": "query", "name": "like", "type": "string"}, {"enum": ["1", "2"], "in": "query", "name": "ad_format", "type": "string"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-location-info": {"id": "tiktok-top-ads-location-info", "method": "GET", "params": [{"default": 1, "description": "Creative Center module id", "in": "query", "name": "module", "type": "integer"}], "path": "/tiktok/top-ads/location-info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "module", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-locations": {"id": "tiktok-top-ads-locations", "method": "GET", "params": [], "path": "/tiktok/top-ads/locations", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-recommend": {"id": "tiktok-top-ads-recommend", "method": "GET", "params": [{"description": "Top Ads material id", "in": "query", "name": "material_id", "required": true, "type": "string", "x-example": "7631130810943897607"}, {"default": 1, "description": "Page number", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"default": 20, "description": "Maximum number of ads to return", "in": "query", "maximum": 100, "name": "limit", "type": "integer"}], "path": "/tiktok/top-ads/recommend", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "material_id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-safety": {"id": "tiktok-top-ads-safety", "method": "GET", "params": [], "path": "/tiktok/top-ads/safety", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-spotlight": {"id": "tiktok-top-ads-spotlight", "method": "GET", "params": [{"default": 1, "description": "Page number", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"default": 20, "description": "Maximum number of ads to return", "in": "query", "maximum": 100, "name": "limit", "type": "integer"}], "path": "/tiktok/top-ads/spotlight", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-top-ads-suggestions": {"id": "tiktok-top-ads-suggestions", "method": "GET", "params": [{"default": 50, "description": "Maximum number of suggestions to return", "in": "query", "name": "count", "type": "integer"}, {"default": 1, "description": "Suggestion scenario id", "in": "query", "name": "scenario", "type": "integer"}], "path": "/tiktok/top-ads/suggestions", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "count", "type": "integer"}, {"in": "query", "name": "scenario", "type": "integer"}], "security": ["ApiKeyAuth"]}, "tiktok-trending": {"id": "tiktok-trending", "method": "GET", "params": [], "path": "/tiktok/trending", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "tiktok-video-comments": {"id": "tiktok-video-comments", "method": "GET", "params": [{"description": "TikTok video id from the video URL", "in": "query", "name": "aweme_id", "required": true, "type": "string", "x-example": "7304809083817774382"}, {"default": 0, "description": "Pagination cursor", "in": "query", "name": "cursor", "type": "integer"}], "path": "/tiktok/comments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "aweme_id", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "integer"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["tiktok-category", "tiktok-challenge", "tiktok-challenge-list", "tiktok-creative-center-hashtags", "tiktok-creative-center-videos", "tiktok-explore", "tiktok-popular-trend-country-industry-meta", "tiktok-post", "tiktok-profile", "tiktok-profile-post", "tiktok-search", "tiktok-search-hashtag", "tiktok-search-user", "tiktok-top-ads-analysis", "tiktok-top-ads-detail", "tiktok-top-ads-filters", "tiktok-top-ads-list", "tiktok-top-ads-location-info", "tiktok-top-ads-locations", "tiktok-top-ads-recommend", "tiktok-top-ads-safety", "tiktok-top-ads-spotlight", "tiktok-top-ads-suggestions", "tiktok-trending", "tiktok-video-comments"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-tiktok-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = Net::HTTP::Get.new(uri)
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = @transport.call(url, request.to_hash, @timeout)
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('category') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-category', params, response_type: response_type)
      end
      define_method('video_comments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-video-comments', params, response_type: response_type)
      end
      define_method('creative_center_hashtags') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-creative-center-hashtags', params, response_type: response_type)
      end
      define_method('creative_center_videos') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-creative-center-videos', params, response_type: response_type)
      end
      define_method('explore') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-explore', params, response_type: response_type)
      end
      define_method('challenge') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-challenge', params, response_type: response_type)
      end
      define_method('challenge_list') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-challenge-list', params, response_type: response_type)
      end
      define_method('popular_trend_country_industry_meta') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-popular-trend-country-industry-meta', params, response_type: response_type)
      end
      define_method('post') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-post', params, response_type: response_type)
      end
      define_method('profile_post') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-profile-post', params, response_type: response_type)
      end
      define_method('profile') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-profile', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-search', params, response_type: response_type)
      end
      define_method('search_hashtag') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-search-hashtag', params, response_type: response_type)
      end
      define_method('search_user') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-search-user', params, response_type: response_type)
      end
      define_method('top_ads_analysis') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-top-ads-analysis', params, response_type: response_type)
      end
      define_method('top_ads_detail') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-top-ads-detail', params, response_type: response_type)
      end
      define_method('top_ads_filters') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-top-ads-filters', params, response_type: response_type)
      end
      define_method('top_ads_list') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-top-ads-list', params, response_type: response_type)
      end
      define_method('top_ads_location_info') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-top-ads-location-info', params, response_type: response_type)
      end
      define_method('top_ads_locations') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-top-ads-locations', params, response_type: response_type)
      end
      define_method('top_ads_recommend') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-top-ads-recommend', params, response_type: response_type)
      end
      define_method('top_ads_safety') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-top-ads-safety', params, response_type: response_type)
      end
      define_method('top_ads_spotlight') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-top-ads-spotlight', params, response_type: response_type)
      end
      define_method('top_ads_suggestions') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-top-ads-suggestions', params, response_type: response_type)
      end
      define_method('trending') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('tiktok-trending', params, response_type: response_type)
      end

      private

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
