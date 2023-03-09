from sqlalchemy import BigInteger, CheckConstraint, Column, Date, DateTime, Enum, ForeignKeyConstraint, Numeric, PrimaryKeyConstraint, String, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Lembrete(Base):
    __tablename__ = 'lembrete'
    __table_args__ = (
        ForeignKeyConstraint(['cpf_proprietario'], ['conta.cpf_proprietario'], ondelete='CASCADE', onupdate='RESTRICT', name='lembrete_conta_fk'),
        PrimaryKeyConstraint('id_lembrete', name='lembrete_pk')
    )

    id_lembrete = Column(BigInteger)
    dt_lembrete = Column(Date, nullable=False)
    titulo_lembrete = Column(String(30), nullable=False)
    cpf_proprietario = Column(BigInteger, nullable=False)

    conta = relationship('Conta', back_populates='lembrete')

