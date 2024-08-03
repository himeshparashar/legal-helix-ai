from fastapi import APIRouter
from app.routers.user_save import save_user_router

backend_router = APIRouter(prefix="/api")
backend_router.include_router(save_user_router)