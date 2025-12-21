# FastAPI application with health endpoint
import logging
import time
from fastapi import FastAPI, Request
from fastapi.responses import Response
from config import settings

# Configurar logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Python API",
    description="Simple API with health endpoint",
    version="0.1.0"
)


# Middleware para logging de requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Ignorar logs de favicon y otros recursos estáticos
    ignored_paths = ["/favicon.ico", "/robots.txt"]

    if request.url.path not in ignored_paths:
        start_time = time.time()
        logger.info(f"Request: {request.method} {request.url.path}")

        response = await call_next(request)

        process_time = time.time() - start_time
        logger.info(
            f"Response: {request.method} {request.url.path} "
            f"- Status: {response.status_code} - Time: {process_time:.4f}s"
        )
    else:
        response = await call_next(request)

    return response


@app.on_event("startup")
async def startup_event():
    logger.info(
        f"Application '{settings.APP_NAME}' starting up with LOG_LEVEL={settings.LOG_LEVEL}...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down...")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """
    Favicon endpoint to avoid 404 logs

    Returns 204 No Content instead of 404
    """
    return Response(status_code=204)


@app.get("/health", tags=["health"])
async def health_check() -> dict:
    """
    Health check endpoint

    Returns:
        dict: Health status information
    """
    logger.debug("Health check endpoint called")
    return {
        "status": "healthy",
        "message": f"{settings.APP_NAME} is running successfully 2."
    }


@app.get("/", tags=["root"])
async def root() -> dict:
    """
    Root endpoint

    Returns:
        dict: Welcome message
    """
    logger.info("Root endpoint accessed")
    return {
        "message": f"Welcome to Python {settings.APP_NAME}"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT
    )
