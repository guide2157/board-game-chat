"""Unit tests for the LoggingMiddleware."""

import logging

import pytest
from httpx import AsyncClient
from pytest import LogCaptureFixture


async def test_middleware_logs_request_details(
    client: AsyncClient, caplog: LogCaptureFixture
) -> None:
    """Test that middleware logs request method and path."""
    with caplog.at_level(logging.INFO):
        response = await client.get("/")

    assert response.status_code == 200

    # Check that request details were logged
    log_messages = caplog.text
    assert "Request: GET /" in log_messages
    assert "Query params:" in log_messages
    assert "Headers:" in log_messages


async def test_middleware_logs_response_details(
    client: AsyncClient, caplog: LogCaptureFixture
) -> None:
    """Test that middleware logs response status and body."""
    with caplog.at_level(logging.INFO):
        response = await client.get("/")

    assert response.status_code == 200

    log_messages = caplog.text
    assert "Response status: 200" in log_messages
    assert "Response body:" in log_messages
    assert "message" in log_messages or "test" in log_messages


async def test_middleware_logs_process_time(
    client: AsyncClient, caplog: LogCaptureFixture
) -> None:
    """Test that middleware logs process time."""
    with caplog.at_level(logging.INFO):
        response = await client.get("/")

    assert response.status_code == 200

    log_messages = caplog.text
    assert "Process time:" in log_messages


async def test_middleware_handles_empty_request_body(
    client: AsyncClient, caplog: LogCaptureFixture
) -> None:
    """Test that middleware handles requests without body."""
    with caplog.at_level(logging.INFO):
        response = await client.get("/")

    assert response.status_code == 200

    log_messages = caplog.text
    assert "Request: GET /" in log_messages


async def test_middleware_handles_query_params(
    client: AsyncClient, caplog: LogCaptureFixture
) -> None:
    """Test that middleware logs query parameters."""
    with caplog.at_level(logging.INFO):
        response = await client.get("/?param1=value1&param2=value2")

    assert response.status_code == 200

    log_messages = caplog.text
    assert "Query params:" in log_messages
    assert "param1" in log_messages or "value1" in log_messages


async def test_middleware_preserves_response_body(client: AsyncClient) -> None:
    """Test that middleware preserves the response body."""
    response = await client.get("/")

    assert response.status_code == 200
    data = response.json()
    assert data == {"message": "Welcome to Board Game Chat API"}


async def test_middleware_preserves_response_headers(client: AsyncClient) -> None:
    """Test that middleware preserves response headers."""
    response = await client.get("/")

    assert response.status_code == 200
    assert "content-type" in response.headers
    assert "application/json" in response.headers["content-type"]
