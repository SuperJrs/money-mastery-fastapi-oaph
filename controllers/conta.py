from fastapi import APIRouter, Depends, HTTPException, status
from models.conta_model import Conta
from core.deps import get_session
from schemas.conta_schema import ContaSchema, ContaSchemaOptional
from repository.conta_repository import ContaRepository

router = APIRouter(prefix="/conta")
repo = ContaRepository()

# Pegar todas as contas
@router.get("/")
def obter_contas(db = Depends(get_session)):
    result = repo.get_all(db)
    return result

# Alterar uma conta específica
@router.put("/{cpf}")
def update_account(cpf: int,conta_atualizada: ContaSchemaOptional , db=Depends(get_session)):
    result = repo.update_account(cpf, conta_atualizada, db)
    return result


# Criar uma conta
@router.post("/")
def criar_conta(nova_conta:ContaSchema, db=Depends(get_session)):
    new_conta = repo.create_conta(nova_conta, db)
    return new_conta


# Pegar uma conta específica
@router.get("/{cpf}", response_model=ContaSchema)
def pegar_conta(cpf: int , db=Depends(get_session)):
    result = repo.get_conta(cpf, db)
    return result

# Remover uma conta
@router.delete("/{cpf}")
def remover_conta(cpf: int, db=Depends(get_session)):
    result = repo.delete_account(cpf, db)
    return result


