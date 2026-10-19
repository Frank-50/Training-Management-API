from fastapi import APIRouter
from http import HTTPStatus
from app.schemas.schema_class import Criar_treinos

router = APIRouter()



treinos = []

#Rota GET: recebe uma requisição http, e devolve a lista `treinos`, e o FastAPI
#converte ela para JSON e retorna 200 (OK). se a lista estiver vazia, ele devolve []
@router.get('/', status_code=HTTPStatus.OK)
def listar_treinos():
    return treinos

# Rota POST: recebe um JSON no parâmetro `treino`. O FastAPI valida os dados
# conforme a classe `criar_treinos` e cria um objeto Python a partir dela.
# Depois o objeto é adicionado à lista `treinos` e devolvido na resposta (201).
@router.post('/', status_code=HTTPStatus.CREATED)
def criar_treino(treino: Criar_treinos):
    treinos.append(treino)
    return treino