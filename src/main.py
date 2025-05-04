from fastapi import FastAPI
from src.routers import user as user_router
from src.db.session import engine
from src.models import * 
from src.db.base import Base

app = FastAPI()

app.include_router(user_router.router, prefix="/api")

@app.get("/")
async def read_root():
    return {"Hello": "World PUTA"}
