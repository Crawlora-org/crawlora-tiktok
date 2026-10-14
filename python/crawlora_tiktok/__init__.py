"""Typed TikTok client for the Crawlora hosted API."""

from .platform import TikTokClient, AsyncTikTokClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = TikTokClient
AsyncClient = AsyncTikTokClient
__version__ = '0.2.0'
DISPLAY_NAME = 'TikTok'
PLATFORM = 'tiktok'
CONTRACT_REVISION = 'sha256:4c68b3ffb1086f7e35a137a7a0cf5ac6849821f94323e8004e5f05f62fb6f95a'

__all__ = [
    "TikTokClient", "AsyncTikTokClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
