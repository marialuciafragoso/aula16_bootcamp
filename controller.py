import requests # Requisições HTTP
from db import SessionLocal, engine, Base
from models import Cep
from schema import CepSchema

Base.metadata.create_all(bind=engine)

def get_cep(cep: str): 
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    # | Buscar informaçoes
    print(response)
    if response.status_code == 200: # Se tudo funcionar normalmente...
        data = response.json() #? Requests converte esse JSON para um dicionário Python.
        if data.get("erro"):
            return None

        return CepSchema(
            cep=data["cep"],
            logradouro=data["logradouro"],
            bairro=data["bairro"],
            cidade=data["localidade"],
            estado=data["uf"])

    return None

def add_cep_to_db(cep_schema: CepSchema): 
    with SessionLocal() as db:
        db_cep = Cep(cep=cep_schema.cep, logradouro=cep_schema.logradouro, 
        bairro=cep_schema.bairro, cidade=cep_schema.cidade, estado=cep_schema.estado)
        # | Transformação dos dados validados em um objeto que pode ser salvo no banco.
        db.add(db_cep) # Coloca o objeto na Session 
        db.commit() # Salva definitivamente
        db.refresh(db_cep) # Atualiza o objeto com as informações que o banco gerou automaticamente.
    return db_cep
