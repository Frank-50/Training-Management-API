
from pydantic import BaseModel

#Molde usado para criar os objetos dos treinos que são enviados na requisição da rota POST
class Criar_treinos(BaseModel):
    nome: str
    tipo: str
    series: int
#Model usado na rota PATCH. todos os campos são opcionais: `| None = None` permite que o campo não venha, `= None` e o valor padrão quando ele não é enviado.
#Assim o usuário manda só o dado que deseja alterar, sem recerver erro 422.
#Quem evita que os campos não enviados apagem os valores antigos é o `exclude_unset=True`, usado na rota.
class Atualizar_treinos(BaseModel):
    nome: str | None = None
    tipo: str | None = None
    series: int | None  = None