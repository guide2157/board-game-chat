import json
import logging
import time
from typing import Any, Callable, Coroutine

from fastapi import Request
from starlette.responses import Response

logger = logging.getLogger(__name__)


class LoggingMiddleware:
    """Middleware to log request payloads, headers, and responses."""

    async def __call__(
        self,
        request: Request,
        call_next: Callable[[Request], Coroutine[Any, Any, Response]],
    ) -> Response:
        # Log request start time
        start_time = time.time()

        # Read request body
        body = await request.body()

        # Log request details
        logger.info("=" * 80)
        logger.info(f"Request: {request.method} {request.url.path}")
        logger.info(f"Query params: {dict(request.query_params)}")
        logger.info(f"Headers: {dict(request.headers)}")

        # Log request body if present
        if body:
            try:
                body_json = json.loads(body.decode("utf-8"))
                logger.info(f"Request body: {json.dumps(body_json, indent=2)}")
            except (json.JSONDecodeError, UnicodeDecodeError):
                logger.info(
                    f"Request body (raw): {body.decode('utf-8', errors='replace')}"
                )

        # Recreate request with body (since it was consumed)
        async def receive():
            return {"type": "http.request", "body": body}

        request._receive = receive

        # Process request
        response = await call_next(request)

        # Calculate processing time
        process_time = time.time() - start_time

        # Log response details
        logger.info(f"Response status: {response.status_code}")
        logger.info(f"Response headers: {dict(response.headers)}")

        # Read response body
        response_body = b""
        async for chunk in response.body_iterator:  # type: ignore[attr-defined]
            response_body += chunk

        # Log response body if present
        if response_body:
            try:
                response_json = json.loads(response_body.decode("utf-8"))
                logger.info(f"Response body: {json.dumps(response_json, indent=2)}")
            except (json.JSONDecodeError, UnicodeDecodeError):
                logger.info(
                    f"Response body (raw): {response_body.decode('utf-8', errors='replace')[:500]}"
                )

        logger.info(f"Process time: {process_time:.3f}s")
        logger.info("=" * 80)

        # Recreate response with body
        return Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type,
        )
