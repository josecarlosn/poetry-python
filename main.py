from fastapi import FastAPI

app = FastAPI()

from routes.auth import auth_router
from routes.home import home_router

app.include_router(auth_router)
app.include_router(home_router)