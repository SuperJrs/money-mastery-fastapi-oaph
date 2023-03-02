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
