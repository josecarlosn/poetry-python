from fastapi import APIRouter

home_router = APIRouter(prefix="/home", tags=["home"])

@home_router.get("/")
async def read_home():
    return {"message": "Welcome to the home page!"}