from fastapi import APIRouter

ROUTER = APIRouter()

@ROUTER.get("/test/", tags=["test"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
