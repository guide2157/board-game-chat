from fastapi import FastAPI
import logging
from middleware import LoggingMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Board Game Chat API", version="1.0.0")


# Add middleware
app.middleware("http")(LoggingMiddleware())


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "board-game-chat"}


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to Board Game Chat API"}
