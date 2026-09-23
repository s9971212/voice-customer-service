import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.api import router
from .config import settings

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # =========================
    # Startup
    # =========================

    logger.info("Application 啟動")

    yield

    # =========================
    # Shutdown
    # =========================

    logger.info("Application 已停止")


app = FastAPI(
    title=settings.project_name,
    description=settings.description,
    version=settings.version,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# =========================
# CORS
# =========================

if settings.backend_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.backend_cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# =========================
# Routers
# =========================

app.include_router(router, prefix=settings.api_v1_str)


# =========================
# Api
# =========================

@app.get("/", tags=["Health Check"])
def root():
    """
    根目錄健康檢查
    """

    return {
        "status": "healthy",
        "project_name": settings.project_name,
        "version": settings.version
    }
