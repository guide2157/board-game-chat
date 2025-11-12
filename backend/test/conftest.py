"""Configuration for pytest."""

from typing import AsyncGenerator

import pytest
from app import app
from httpx import ASGITransport, AsyncClient


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Create an asynchronous test client for the FastAPI app."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac
