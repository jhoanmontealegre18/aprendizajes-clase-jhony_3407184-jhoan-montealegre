from pydantic import BaseModel


# Modelo base con los datos principales del cliente
class ClienteBase(BaseModel):
    nombre: str
    edad: int
    descripcion: str | None=None


# Modelo para crear un cliente
class ClienteCrear(ClienteBase):
    pass


# Modelo completo del cliente (incluye ID)
class Cliente(ClienteBase):
    id: int | None = None   
