"""Typed TikTok client for the Crawlora hosted API."""

from .platform import TikTokClient, AsyncTikTokClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = TikTokClient
AsyncClient = AsyncTikTokClient
__version__ = '0.5.0'
DISPLAY_NAME = 'TikTok'
PLATFORM = 'tiktok'
CONTRACT_REVISION = 'sha256:5823222daa31ec6f43dbc20c0ebf31a2e341cdbf1e93509f340d2126c102421f'

__all__ = [
    "TikTokClient", "AsyncTikTokClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
