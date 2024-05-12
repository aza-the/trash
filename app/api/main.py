from fastapi import APIRouter, Request

from app.api.routes import flats


api_router = APIRouter()

api_router.include_router(flats.router, prefix='/flats', tags=['flats'])
