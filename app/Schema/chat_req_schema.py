from pydantic import BaseModel

class chat_req_model(BaseModel):
    query: str
    user_id: int