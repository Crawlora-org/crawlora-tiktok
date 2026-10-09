require_relative "lib/crawlora/tiktok/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-tiktok"
  spec.version = Crawlora::Tiktok::VERSION
  spec.summary = "TikTok client for the Crawlora hosted API"
  spec.description = "Credential-free TikTok API access through Crawlora's hosted service."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=tiktok-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-tiktok", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-tiktok/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
