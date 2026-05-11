from  fastapi import FastAPI
from pydantic import BaseModel
app =FastAPI()
@app.get("/")
def root():
    return{"mensaje","Hola mundo"}
#aplicacion de clientes
lista_clientes=[]#datos de la base de datos
class cliente(BaseModel):
    id:int
    nombre:str
    edad:int
    descripcion:str| None=None
    #listar
    
@app.get("/clientes")
def listar_clientes():
    return{"clientes":lista_clientes}


@app.post("/clientes",)
def crear_clientes(datos_cliente: cliente):
    lista_clientes.append(datos_cliente)
    return{"mensaje":"Cliente creado"}

#RETO : crear un nuevo endpoint y que me retome un solo cliente
@app.get("/clientes/{id_cliente}")
def obtener_cliente(id_cliente: int):
# verificamos si el id existe en clientes 
    for cliente in lista_clientes:
        if cliente.id == id_cliente:
            return {"cliente": cliente}

    return {"mensaje": "Cliente no ah sido encontrado"}
