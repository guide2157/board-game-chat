"""Unit tests for the FastAPI application endpoints."""

import pytest
from httpx import AsyncClient


async def test_health_check_endpoint(client: AsyncClient) -> None:
    """Test that the health check endpoint returns the expected response."""
    response = await client.get("/health")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    data = response.json()
    assert data == {"status": "healthy", "service": "board-game-chat"}
    assert data["status"] == "healthy"
    assert data["service"] == "board-game-chat"


async def test_health_check_endpoint_method_not_allowed(client: AsyncClient) -> None:
    """Test that POST method is not allowed on health check endpoint."""
    response = await client.post("/health")

    assert response.status_code == 405  # Method Not Allowed


async def test_health_check_endpoint_with_query_params(client: AsyncClient) -> None:
    """Test that health check endpoint works with query parameters."""
    response = await client.get("/health?foo=bar")

    assert response.status_code == 200
    data = response.json()
    assert data == {"status": "healthy", "service": "board-game-chat"}
