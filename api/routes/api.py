from fastapi import APIRouter
from src.endpoints import utils, sqlgpt

router = APIRouter()
router.include_router(utils.router)
router.include_router(sqlgpt.router)