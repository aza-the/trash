from fastapi import APIRouter, Request

from app.api.routes import sample_route


api_router = APIRouter()

api_router.include_router(
    sample_route.router, prefix='/sample', tags=['flats'])
