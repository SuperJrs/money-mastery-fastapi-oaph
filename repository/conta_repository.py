from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.conta_model import Conta
from schemas.conta_schema import ContaSchema

class ContaRepository:
    

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
        

