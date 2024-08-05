from fastapi import APIRouter

from app.Schema.chat_req_schema import chat_req_model
from app.helpers.chater import get_chat_response

chat_session_router = APIRouter(prefix="/chat_session")

@chat_session_router.post("/")
async def create_chat_session(req:chat_req_model):
    try:
        response = await get_chat_response(req.query, req.user_id)
        return {"role":"ai","content":response}
    except Exception as e:
        return {"error":str(e)}