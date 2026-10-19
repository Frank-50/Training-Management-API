from fastapi import APIRouter

router = APIRouter()


lista_dinamica = []
lista_isometrica = []


@router.get('/')
def listar_treinos():
    return lista_dinamica + lista_isometrica

