from fastapi import FastAPI
from api.v1.routers import router as router_v1
from core.config import API_V1_PREFIX

app = FastAPI()
app.include_router(router_v1, prefix=API_V1_PREFIX)
