from fastapi import APIRouter

save_user_router = APIRouter(prefix="/save_user")

@save_user_router.post("/")
async def save_user():
    return {"message": "User saved successfully"}