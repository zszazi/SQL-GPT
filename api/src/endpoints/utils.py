from fastapi import APIRouter

router = APIRouter(
    prefix="/utils",
    tags=["Utils"]
)

@router.get("/status")
async def get_status():
    return {"status" : "SQLGPT is up and alive"}


@router.post("/update_key")
async def update_openai_key():
    pass