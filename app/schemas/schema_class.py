
from pydantic import BaseModel

class treino_dinamico(BaseModel):
    nome: str
    type: str
    series: int
    repetiçoes: int

class treino_isomatria(BaseModel):
    nome: str
    type: str
    series: int
    tempo: float