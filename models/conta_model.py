from sqlalchemy import (
    BigInteger, 
    CheckConstraint,
    Column,
    Date, 
    PrimaryKeyConstraint, 
    String, 
    UniqueConstraint
    )
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Conta(Base):
    __tablename__ = 'conta'
    __table_args__ = (
        CheckConstraint("(telefone IS NULL) OR (telefone <= '99999999999'::bigint)", name='conta_telefone_check'),
        CheckConstraint("cpf_proprietario <= '99999999999'::bigint", name='conta_cpf_proprietario_check'),
        PrimaryKeyConstraint('cpf_proprietario', name='conta_pk'),
        UniqueConstraint('email', name='conta_email_uk')
    )

    cpf_proprietario = Column(BigInteger, primary_key=True)
    nome_proprietario = Column(String(120), nullable=False)
    dt_nasc_proprietario = Column(Date, nullable=False)
    email = Column(String(90), nullable=False)
    senha = Column(String(256), nullable=False)
    telefone = Column(BigInteger)