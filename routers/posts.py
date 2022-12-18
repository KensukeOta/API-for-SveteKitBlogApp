from fastapi import APIRouter

router = APIRouter(
  prefix="/api",
  tags=["posts"],
)

@router.get("/posts")
async def read_posts():
    return {"posts": "posts"}