# Scrapy settings for stealth_crawler project

BOT_NAME = "stealth_crawler"

SPIDER_MODULES = ["stealth_crawler.spiders"]
NEWSPIDER_MODULE = "stealth_crawler.spiders"

# User-Agent configuration
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# Uncomment and update the user-agent as needed
# USER_AGENT = "stealth_crawler (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True

# Enable AutoThrottle to automatically slow down based on site load
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1  # Initial download delay
AUTOTHROTTLE_MAX_DELAY = 5  # Max download delay
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # Average number of requests per second per remote server

# Disable cookies to reduce tracking
COOKIES_ENABLED = False

# Configure downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,  # Disable default UserAgentMiddleware
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,  # Use Random User-Agent middleware
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,  # Enable HTTP Proxy middleware
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,  # Enable rotating proxies
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,  # Enable ban detection
}

# Proxy configuration
HTTP_PROXY = 'http://127.0.0.1:8118'  # Tor default HTTP proxy

# Uncomment if you have a custom ProxyMiddleware implemented
# 'stealth_crawler.middlewares.ProxyMiddleware': 100,

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Enable HTTP caching (disabled by default)
# Uncomment to enable and configure HTTP caching
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
