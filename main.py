import uvicorn
import jwt
import csv
from fastapi import FastAPI
from app.router import api_router
from app.core import settings


app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(api_router, prefix=settings.API_V1_STR)