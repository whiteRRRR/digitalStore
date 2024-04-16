from fastapi import FastAPI
from api.v1.routers import router as v1_router
from core.config import API_V1_PREFIX

app = FastAPI()
app.include_router(v1_router, prefix=API_V1_PREFIX)
