# Busca API -> transforma -> manda para o banco

import requests # Requisições HTTP
from db1 import SessionLocal, engine, Base
from models1 import Pokemon
from schema1 import PokemonSchema

Base.metadata.create_all(bind=engine)

def fetch_pokemon_data(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    # | Buscar informaçoes
    print(response)
    if response.status_code == 200: # Se tudo funcionar normalmente...
        data = response.json() #? Requests converte esse JSON para um dicionário Python.
        types = ', '.join(type_info['type']['name'] for type_info in data['types']) 
        # | Percorre os tipos, pega o nome e junta tudo em texto
        return PokemonSchema(name=data['name'], type=types)
    else:
        return None

def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        # | Transformação dos dados validados em um objeto que pode ser salvo no banco.
        db.add(db_pokemon) # Coloca o objeto na Session 
        db.commit() # Salva definitivamente
        db.refresh(db_pokemon) # Atualiza o objeto com as informações que o banco gerou automaticamente.
    return db_pokemon
