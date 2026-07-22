# Representa os dados que chegam da internet.
# Verifica se recebeu tudo certo

from pydantic import BaseModel, ConfigDict

# Pydantic V2 
class PokemonSchema(BaseModel): #-> Modelo de validaçao
    name: str
    type: str
model_config = ConfigDict(
    from_attributes=True
)



#? PYDANTIC VC
#? class PokemonSchema(BaseModel): -> Modelo de validaçao
    #?name: str
    #?type: str

    #?class Config: -> Serve para explicar o comportamento do Pydantic
        #?orm_mode = True # "Pode aceitar objetos do ORM também."

