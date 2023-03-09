from sqlalchemy import BigInteger, CheckConstraint, Column, Date, DateTime, Enum, ForeignKeyConstraint, Numeric, PrimaryKeyConstraint, String, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Emprestimo(Base):
    __tablename__ = 'emprestimo'
    __table_args__ = (
        ForeignKeyConstraint(['cpf_proprietario'], ['conta.cpf_proprietario'], ondelete='CASCADE', onupdate='RESTRICT', name='emprestimo_conta_fk'),
        ForeignKeyConstraint(['id_saida'], ['saida.id_saida'], ondelete='CASCADE', onupdate='CASCADE', name='emprestimo_saida_fk'),
        PrimaryKeyConstraint('id_emprestimo', name='emprestimo_pk')
    )

    id_emprestimo = Column(BigInteger)
    nome_devedor = Column(String(120), nullable=False)
    dt_emprestimo = Column(Date, nullable=False)
    cpf_proprietario = Column(BigInteger, nullable=False)
    id_saida = Column(BigInteger, nullable=False)
    dt_limite_pg = Column(Date)

    conta = relationship('Conta', back_populates='emprestimo')
    saida = relationship('Saida', back_populates='emprestimo')
    entrada = relationship('Entrada', back_populates='emprestimo')

