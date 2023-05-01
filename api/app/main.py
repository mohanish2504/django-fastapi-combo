
import secrets
from datetime import datetime
from fastapi import FastAPI,status, Request, HTTPException, Depends
from starlette.middleware.cors import CORSMiddleware

import asyncio
from fastapi.responses import StreamingResponse
from app.api.api_v1.api import api_router
from app.core.config import settings


from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    openapi_url=f'/docs{settings.API_V1_STR}.json'
)


app.include_router(api_router, prefix=settings.API_V1_STR)
security = HTTPBasic()






