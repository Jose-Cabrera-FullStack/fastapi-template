from fastapi import FastAPI

from app.adapter.example import AppNameAdapter
from app.domain.example import AppNameDomain
from app.domain.example import error_for_test
from app.schemas.request import POSTRequest
from app.schemas.response import POSTResponse
from app.service.example import AppNameService
from app.database.config import database
from app.database.models import Client


app = FastAPI(title="app_name Service", description="API to validate the Client Debts status", version="0.1.0")


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


@app.get("/")
async def read_root():
    return "app_name-service-ms v1"


@app.post("/api/v1/YOUR_ENDPOINT", response_model=POSTResponse, status_code=200)
def post_endpoint(item: POSTRequest):

    return item
