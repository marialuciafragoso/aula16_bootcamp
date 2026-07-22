from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func #! Usa uma funçao do banco
from db import Base


class Cep(Base): # -> Representa a tabela inteira
    __tablename__ = 'ceps' # Nome da tabela
    cep = Column(String, primary_key=True, index=True)
    bairro = Column(String)
    cidade = Column(String)
    estado = Column(String)
    logradouro = Column(String)