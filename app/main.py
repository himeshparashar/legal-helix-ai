import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from app.routers.api import backend_router
from fastapi.middleware.cors import CORSMiddleware



load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(backend_router)