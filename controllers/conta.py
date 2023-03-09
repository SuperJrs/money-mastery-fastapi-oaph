from fastapi import APIRouter, Depends, HTTPException, status
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

@router.put("/{cpf}")
def alterar_dados_conta(cpf: int, conta_atualizada: ContaSchema, db=Depends(get_session)):
    conta_a_alterar = db.query(Conta).filter(Conta.cpf_proprietario == cpf).update({
        # CPF é inalterável
        # Criar ContaSchema onde os dados são opcionais
        # Utilizar o método firt()
        'cpf_proprietario': conta_atualizada.cpf_proprietario,
        'senha' : conta_atualizada.senha,
        'dt_nasc_proprietario' : conta_atualizada.dt_nasc_proprietario,
        'nome_proprietario' : conta_atualizada.nome_proprietario,
        'email' : conta_atualizada.email,
        'telefone' : conta_atualizada.telefone
        }
    
        
    )
    db.commit()
    return f"A conta cujo cpf é {cpf} foi atualizada com sucesso!"


@router.post("/")
def criar_conta(nova_conta:ContaSchema, db=Depends(get_session)):
    db.add(Conta(
        cpf_proprietario = nova_conta.cpf_proprietario,
        nome_proprietario = nova_conta.nome_proprietario,
        dt_nasc_proprietario = nova_conta.dt_nasc_proprietario,
        telefone = nova_conta.telefone,
        email = nova_conta.email,
        senha = nova_conta.senha
    ))
    db.commit()
    return {
        "detail": "Conta criada com sucesso!"
    }

@router.get("/{cpf}", response_model=ContaSchema)
def pegar_conta(cpf: int , db=Depends(get_session)):
    conta = db.query(Conta).filter(Conta.cpf_proprietario == cpf).first()

    if not conta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Em nosso sistema, não há uma conta cadastrada para o cpf {cpf}'
        )
    return conta




@router.delete("/{cpf}")
def remover_conta(cpf: int, db=Depends(get_session)):
    conta_a_remover = db.query(Conta).filter(Conta.cpf_proprietario == cpf).first()

    if not conta_a_remover:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conta não existe!"
        )
    db.delete(conta_a_remover)
    db.commit()
    return f'A conta {cpf} foi removida com sucesso!'


# @router.delete("/")
# def remover_conta(conta: ContaSchema, db=Depends(get_session)):
#     db.delete(conta)
#     return {
#         "detail": "Conta deletada com sucesso!"
#     }
