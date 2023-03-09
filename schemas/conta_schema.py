from pydantic import BaseModel
from typing import Optional
from datetime import date

class ContaSchema(BaseModel):
    cpf_proprietario: int
    nome_proprietario: str
    dt_nasc_proprietario: date
    email: str
    senha: str
    telefone: Optional[int]

    class Config:
        orm_mode = True

class ContaSchemaOptional(BaseModel):
    nome_proprietario: Optional[str]
    dt_nasc_proprietario: Optional[date]
    email: Optional[str]
    senha: Optional[str]
    telefone: Optional[int]

    class Config:
        orm_mode = True
