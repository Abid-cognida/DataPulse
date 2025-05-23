"""API router module."""

from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, flower, items

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(flower.router, prefix="/flower", tags=["monitoring"])
