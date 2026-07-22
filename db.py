from sqlalchemy import create_engine #? Cria conexao com o banco
from sqlalchemy.ext.declarative import declarative_base #? Essa classe representa uma tabela do banco.
from sqlalchemy.orm import sessionmaker #? Faz a ponte real com o banco de dados (engine)


SQLALCHEMY_DATABASE_URL = "sqlite:///./cep.db" # <- O banco fica nesse arquivo 
engine = create_engine(SQLALCHEMY_DATABASE_URL) # Cria a conexao 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# | bind: "Toda session deve usar esse banco", autocommit: Nao salva diretamente, autoflush: Nao faz nada automatico
Base = declarative_base() # Cria uma classe base 
