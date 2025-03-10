from fastapi import APIRouter
from .employee import employee_router

api_router = APIRouter()
api_router.include_router(employee_router)
