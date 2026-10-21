from fastapi import APIRouter, HTTPException
from http import HTTPStatus
from app.schemas.schema_class import Criar_treinos, Atualizar_treinos

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
#se o `treino[id]` for igual a lista `treinos`, e o FastAPI
#converte ela para JSON e retorna 200 (OK). se o id não for encontrado, ele devolve 404 (NOT FOUND)
@router.get('/{treino_id}', status_code=HTTPStatus.OK)
def filtra_treinos(treino_id: int):
    # `treino` e uma variavel temporaria que recebe um item da lista `treinos` acada vez que o loop roda
    for treino in treinos:
        if treino["id"] == treino_id:
            return treino
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Treino não encontrado")

#Rota PATCH: Recebe o `treino_id` pela URL e um JSON no parametro `novo_treino`, validado pela classe `Atualizar_treinos` (todos os campos são opcionais possuindo None).
#O loop for procura o treino com aquele id. se acha o model_dump(exclude_unset=True), transforma em dicionario so com os campos que o usuário realmente envio em novo_treino.
#e `update()` sobrescreve apenas essas chaves, sem mexer nas outras. devolve o treino atualizado (200). se caso o loop terminar e o id não for encontrado, devolver (404).
@router.patch('/{treino_id}', status_code=HTTPStatus.OK)
def atualizar_treino(treino_id: int, novo_treino: Atualizar_treinos):

    for treino in treinos: # `treino` e uma variavel temporaria que recebe um item da lista `treinos` acada vez que o loop roda
        if treino["id"] == treino_id:
            #model.dump(exclude_unset=True), Transforma os dados em dicionario só com os campos que o usuário realmente enviou
            #exclude_unset=True -> Sem ele os campos enviados viriam como None e apagariam os valores antigos.
            treino.update(novo_treino.model_dump(exclude_unset=True)) 
            return treino
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Treino não encontrado")
