from fastapi import APIRouter, Depends
from models.conta_model import Conta
from core.deps import get_session
from schemas.conta_schema import ContaSchema

router = APIRouter(prefix="/conta")

@router.get("/")
def obter_contas(db = Depends(get_session)):
    result = db.query(Conta).all()
    return result

