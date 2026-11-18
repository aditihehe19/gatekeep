
from fastapi import FastAPI

from app.api.routes import health
from app.core.config import settings
from app.modules.iam.router import router as iam_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="A modular cybersecurity engineering platform",
)

app.include_router(health.router, prefix=settings.api_v1_prefix)
app.include_router(iam_router, prefix=settings.api_v1_prefix)
from fastapi import FastAPI

from app.api.routes import health
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="A modular cybersecurity engineering platform",
)

app.include_router(
    health.router,
    prefix=settings.api_v1_prefix,
)