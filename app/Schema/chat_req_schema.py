from pydantic import BaseModel

class ChatReqSchema(BaseModel):
    user_id: int
    message: str