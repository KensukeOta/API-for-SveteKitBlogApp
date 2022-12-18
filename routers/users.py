from fastapi import APIRouter

router = APIRouter(
  prefix="/api",
  tags=["users"],
)

@router.get("/user")
async def read_user():
    return {"name": "kensuke"}