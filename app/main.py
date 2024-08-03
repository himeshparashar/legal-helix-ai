import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from app.routers.api import backend_router

load_dotenv()
app = FastAPI()




app.include_router(backend_router)