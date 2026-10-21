from fastapi import APIRouter, HTTPException
from http import HTTPStatus
from app.schemas.schema_class import Criar_treinos

router = APIRouter()



treinos = []
proximo_id = 1

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
    global proximo_id
    novo_treino = treino.model_dump() # model_dump transforma o json em Um dicionario (dict)
    novo_treino["id"] = proximo_id # O servidor acresenta a chave id: {"id": 1}
    proximo_id += 1 # Sobe o contador pra 2, e o proximo treino vai receber o id 2
    treinos.append(novo_treino)
    return novo_treino


#Rota GET: recebe uma requisição http no parametro `treino_id` onde ela vai filtra o treino específico que que seja igual ao id da requisição, 
# se o `treino[id]` for igual a lista `treinos`, e o FastAPI
#converte ela para JSON e retorna 200 (OK). se o id não for encontrado, ele devolve 404 (NOT FOUND)
@router.get('/{treino_id}', status_code=HTTPStatus.OK)
def filtra_treinos(treino_id: int):
    # `treino` e uma variavel temporaria que recebe um item da lista `treinos` acada vez que o loop roda
    for treino in treinos:
        if treino["id"] == treino_id:
            return treino
    raise HTTPException(status_code=404, detail="Treino não encontrado")