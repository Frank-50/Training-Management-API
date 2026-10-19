
from fastapi import FastAPI
from app.api import routers_treinos

app = FastAPI()

app.include_router(
    routers_treinos.router,
    prefix="/treinos",
    tags=["Treinos"]
    )

