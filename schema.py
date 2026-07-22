from pydantic import BaseModel, ConfigDict

# Pydantic V2 
class CepSchema(BaseModel): #-> Modelo de validaçao
    cep: str
    bairro: str
    cidade: str
    estado: str
    logradouro: str
    model_config = ConfigDict(
    from_attributes=True
    )
