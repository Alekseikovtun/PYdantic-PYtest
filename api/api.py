from fastapi import APIRouter
from api.endpoints import station


api_router = APIRouter()


api_router.include_router(station.router, prefix='/station')
