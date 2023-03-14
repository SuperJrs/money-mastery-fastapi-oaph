from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.conta_model import Conta
from schemas.conta_schema import ContaSchema, ContaSchemaOptional

class ContaRepository:

    # Implementar a mesma lógica utilizada pelo Samy 
    # Fazer um "for" para deixar o código mais apresentável

    @staticmethod
    def update_account(cpf:int, updated_account:ContaSchemaOptional, db:Session):
        conta_a_alterar = db.query(Conta).filter(Conta.cpf_proprietario == cpf).first()
        if updated_account.senha != None:
            conta_a_alterar.senha = updated_account.senha
        if updated_account.nome_proprietario != None:
            print("Executado")
            conta_a_alterar.nome_proprietario = updated_account.nome_proprietario
        if updated_account.email != None:
            conta_a_alterar.email = updated_account.email
        if updated_account.telefone != None:
            conta_a_alterar.telefone = updated_account.telefone

        db.commit()
        return f'A conta de cpf {cpf} foi alterar com sucesso!'


    @staticmethod
    def delete_account(cpf:int, db:Session):
        conta_a_remover = ContaRepository.get_conta(cpf, db)

        if not conta_a_remover:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Conta não existe!"
            )
        db.delete(conta_a_remover)
        db.commit()
        return f"A conta de cpf {cpf} foi removida com sucesso!"
    
    @staticmethod
    def get_conta(cpf: int, db:Session):
        conta = db.query(Conta).filter(Conta.cpf_proprietario == cpf).first()

        if not conta:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Em nosso sistema, não há uma conta cadastrada para o cpf {cpf}'
        )
        return conta

    @staticmethod
    def create_conta(nova_conta:ContaSchema, db:Session):
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

    @staticmethod
    def get_all(db:Session):
        try:
            contas = db.query(Conta).all()
        except Exception as error:
            raise HTTPException(
                detail=str(error),
                status_code=500
            )
        if not contas:
            raise HTTPException(
                detail="Não há contas para retornar!",
                status_code=status.HTTP_404_NOT_FOUND
            )
        return contas
        

