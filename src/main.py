from fastapi import FastAPI
from src.routers import auth, user as user_router
from src.routers import insurance_module as insurance_module_router
from src.routers import user_insurance_module as uim_router
from fastapi.middleware.cors import CORSMiddleware
from src.db.session import engine
from src.models import * 
from src.db.base import Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(insurance_module_router.router, prefix="/api")
app.include_router(uim_router.router, prefix="/api")
