from sqlalchemy import BigInteger, CheckConstraint, Column, Date, DateTime, Enum, ForeignKeyConstraint, Numeric, PrimaryKeyConstraint, String, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class GastoBase(Base):
    __tablename__ = 'gasto_base'
    __table_args__ = (
        ForeignKeyConstraint(['cpf_proprietario'], ['conta.cpf_proprietario'], ondelete='CASCADE', onupdate='RESTRICT', name='gasto_base_conta_fk'),
        PrimaryKeyConstraint('id_gasto_base', name='gasto_base_pk')
    )

    id_gasto_base = Column(BigInteger)
    titulo_gasto = Column(String(30), nullable=False)
    valor_gasto = Column(Numeric(9, 2), nullable=False)
    cpf_proprietario = Column(BigInteger, nullable=False)
    
    conta = relationship('Conta', back_populates='gasto_base')