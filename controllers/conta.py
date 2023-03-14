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
    print(result)
    return result

# Alterar uma conta específica
@router.put("/{cpf}")
def alterar_dados_conta(cpf: int,conta_atualizada: ContaSchemaOptional , db=Depends(get_session)):

    # Implementar a mesma lógica utilizada pelo Samy 
    # Fazer um "for" para deixar o código mais apresentável
    conta_a_alterar = db.query(Conta).filter(Conta.cpf_proprietario == cpf).first()
    if conta_atualizada.senha != None:
        conta_a_alterar.senha = conta_atualizada.senha
    if conta_atualizada.nome_proprietario != None:
        print("Executado")
        conta_a_alterar.nome_proprietario = conta_atualizada.nome_proprietario
    if conta_atualizada.email != None:
        conta_a_alterar.email = conta_atualizada.email
    if conta_atualizada.telefone != None:
        conta_a_alterar.telefone = conta_atualizada.telefone

    db.commit()
    return f'A conta de cpf {cpf} foi alterar com sucesso!  '


# Criar uma conta
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

# Pegar uma conta específica
@router.get("/{cpf}", response_model=ContaSchema)
def pegar_conta(cpf: int , db=Depends(get_session)):
    conta = db.query(Conta).filter(Conta.cpf_proprietario == cpf).first()

    if not conta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Em nosso sistema, não há uma conta cadastrada para o cpf {cpf}'
        )
    return conta



# Remover uma conta
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


