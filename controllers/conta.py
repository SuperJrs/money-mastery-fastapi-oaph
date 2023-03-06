from fastapi import APIRouter, Depends
from models.conta_model import Conta
from core.deps import get_session
from schemas.conta_schema import ContaSchema
from repository.conta_repository import ContaRepository

router = APIRouter(prefix="/conta")
repo = ContaRepository()

@router.get("/")
def obter_contas(db = Depends(get_session)):
    result = repo.get_all(db)
    print(result)
    return result

