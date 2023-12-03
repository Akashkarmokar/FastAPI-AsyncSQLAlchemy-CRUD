from fastapi import FastAPI
from app.API.User.routers import UserRouter


def init_routes(app: FastAPI):
    app.include_router(UserRouter)
