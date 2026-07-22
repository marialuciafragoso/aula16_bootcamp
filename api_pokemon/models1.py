# Desenha estrutura da tabela 


from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func #! Usa uma funçao do banco
from db1 import Base


class Pokemon(Base): # -> Representa a tabela inteira
    __tablename__ = 'pokemons' # Nome da tabela
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    created_at = Column(DateTime, default=func.now()) # Cria coluna de data