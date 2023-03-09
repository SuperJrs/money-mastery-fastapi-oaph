from sqlalchemy import BigInteger, CheckConstraint, Column, Date, DateTime, Enum, ForeignKeyConstraint, Numeric, PrimaryKeyConstraint, String, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Reserva(Base):
    __tablename__ = 'reserva'
    __table_args__ = (
        ForeignKeyConstraint(['cpf_proprietario'], ['conta.cpf_proprietario'], ondelete='CASCADE', onupdate='RESTRICT', name='reserva_conta_fk'),
        PrimaryKeyConstraint('id_reserva', name='reserva_pk')
    )

    id_reserva = Column(BigInteger)
    dt_criacao = Column(Date, nullable=False)
    titulo_reserva = Column(String(30), nullable=False)
    cpf_proprietario = Column(BigInteger, nullable=False)
    descricao_reserva = Column(String(100))

    conta = relationship('Conta', back_populates='reserva')
    saida = relationship('Saida', back_populates='reserva')
    entrada = relationship('Entrada', back_populates='reserva')
