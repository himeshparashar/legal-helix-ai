from fastapi import APIRouter
from app.routers.chat_session_router import chat_session_router
from app.routers.user_save import save_user_router

backend_router = APIRouter(prefix="/api")
backend_router.include_router(save_user_router)
backend_router.include_router(chat_session_router)