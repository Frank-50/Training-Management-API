
from fastapi import FastAPI, HTTPException
from app.api import routers_treinos

app = FastAPI()

app.include_router(
    routers_treinos.router,
    prefix="/treinos",
    tags=["Treinos"]
    )

