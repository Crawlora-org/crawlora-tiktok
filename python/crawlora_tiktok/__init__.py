"""Typed TikTok client for the Crawlora hosted API."""

from .platform import TikTokClient, AsyncTikTokClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = TikTokClient
AsyncClient = AsyncTikTokClient
__version__ = '0.1.1'
DISPLAY_NAME = 'TikTok'
PLATFORM = 'tiktok'
CONTRACT_REVISION = 'sha256:54cbbf627ce0c1a21749439fd3c7fe474e0c855da0977c70674aa93de7e1e8be'

__all__ = [
    "TikTokClient", "AsyncTikTokClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
