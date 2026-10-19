
from pydantic import BaseModel

class Criar_treinos(BaseModel):
    nome: str
    tipo: str
    series: int
