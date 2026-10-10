"""Typed TikTok client for the Crawlora hosted API."""

from .platform import TikTokClient, AsyncTikTokClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = TikTokClient
AsyncClient = AsyncTikTokClient
__version__ = '0.1.2'
DISPLAY_NAME = 'TikTok'
PLATFORM = 'tiktok'
CONTRACT_REVISION = 'sha256:39c2041e66692f715a6e15609116f20f91cd62c2c391c81213d2832db7377148'

__all__ = [
    "TikTokClient", "AsyncTikTokClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
