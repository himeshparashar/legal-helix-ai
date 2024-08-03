from fastapi import APIRouter

chat_session_router = APIRouter(prefix="/chat_session")

@chat_session_router.post("/")
async def create_chat_session():
    return {"message": "Chat session created successfully"}