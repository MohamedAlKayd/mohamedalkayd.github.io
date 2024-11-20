source 'https://rubygems.org'

# GitHub Pages gem for managing Jekyll dependencies
gem 'github-pages', '~> 227', group: :jekyll_plugins

# Additional plugins you need
group :jekyll_plugins do
    gem 'jekyll-archives'
    gem 'jekyll-diagrams'
    gem 'jekyll-email-protect'
    gem 'jekyll-feed'
    # Remove jekyll-imagemagick if not necessary to avoid potential issues
    # gem 'jekyll-imagemagick'
    gem 'jekyll-minifier'
    gem 'jekyll-paginate-v2'
    gem 'jekyll-sitemap'
    gem 'jekyll-link-attributes'
    gem 'jekyll-twitter-plugin'
    gem 'jemoji'
    gem 'unicode_utils'
    gem 'webrick', '~> 1.7' # Required for Ruby 3.x to run `jekyll serve`
end

# Other plugins
group :other_plugins do
    gem 'httparty'
    gem 'feedjira'
end
gem 'faraday-retry'

# Jekyll Scholar plugin for academic citations (Downgraded for Jekyll 3.x compatibility)
gem "jekyll-scholar", "~> 5.15"
