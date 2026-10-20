"""Typed TikTok client for the Crawlora hosted API."""

from .platform import TikTokClient, AsyncTikTokClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = TikTokClient
AsyncClient = AsyncTikTokClient
__version__ = '0.4.0'
DISPLAY_NAME = 'TikTok'
PLATFORM = 'tiktok'
CONTRACT_REVISION = 'sha256:a027d217d59233b22a7523eb4b5063fa5ec396297a0cfdae9f87f7deaad2402f'

__all__ = [
    "TikTokClient", "AsyncTikTokClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
