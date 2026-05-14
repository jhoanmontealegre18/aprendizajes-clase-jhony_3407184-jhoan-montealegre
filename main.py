
from fastapi import FastAPI
from modelos.Clientes import Cliente, ClienteCrear
from modelos.factura import Factura, FacturaCrear
from modelos.transacciones import Transaccion, TransaccionCrear

app = FastAPI()

lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []


@app.get("/clientes")
async def listar_clientes():
    return {"clientes": lista_clientes}


@app.post("/clientes", response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    cliente_val.id = len(lista_clientes) + 1
    lista_clientes.append(cliente_val)
    return cliente_val


@app.get("/clientes/{id}", response_model=Cliente)
async def obtener_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return cliente
    return {"mensaje": "Cliente no encontrado"}


@app.delete("/clientes/{id}", response_model=Cliente)
async def eliminar_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            cliente_eliminado = Cliente.model_validate(cliente.model_dump())
            lista_clientes.remove(cliente)
            return cliente_eliminado
    return {"mensaje": "Cliente no encontrado"}


@app.put("/clientes/{id}", response_model=Cliente)
async def actualizar_cliente(id: int, datos_cliente: ClienteCrear):
    for cliente in lista_clientes:
        if cliente.id == id:
            cliente_actualizado = Cliente(
                id=cliente.id,
                nombre=datos_cliente.nombre,
                edad=datos_cliente.edad,
                descripcion=datos_cliente.descripcion
            )

            index = lista_clientes.index(cliente)
            lista_clientes[index] = cliente_actualizado
            return cliente_actualizado

    return {"mensaje": "Cliente no encontrado"}


@app.get("/facturas")
async def listar_facturas():
    return {"facturas": lista_facturas}


@app.post("/facturas", response_model=Factura)
async def crear_factura(datos_factura: FacturaCrear):
    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.id = len(lista_facturas) + 1
    lista_facturas.append(factura_val)
    return factura_val


@app.get("/facturas/{id}", response_model=Factura)
async def obtener_factura(id: int):
    for factura in lista_facturas:
        if factura.id == id:
            return factura
    return {"mensaje": "Factura no encontrada"}


@app.delete("/facturas/{id}", response_model=Factura)
async def eliminar_factura(id: int):
    for factura in lista_facturas:
        if factura.id == id:
            factura_eliminada = Factura.model_validate(factura.model_dump())
            lista_facturas.remove(factura)
            return factura_eliminada
    return {"mensaje": "Factura no encontrada"}


@app.put("/facturas/{id}", response_model=Factura)
async def actualizar_factura(id: int, datos_factura: FacturaCrear):
    for factura in lista_facturas:
        if factura.id == id:
            factura_actualizada = Factura(
                id=factura.id,
                cliente_id=datos_factura.cliente_id,
                monto=datos_factura.monto,
                descripcion=datos_factura.descripcion
            )

            index = lista_facturas.index(factura)
            lista_facturas[index] = factura_actualizada
            return factura_actualizada

    return {"mensaje": "Factura no encontrada"}


@app.get("/transacciones")
async def listar_transacciones():
    return {"transacciones": lista_transacciones}


@app.post("/transacciones", response_model=Transaccion)
async def crear_transaccion(datos_transaccion: TransaccionCrear):
    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
    transaccion_val.id = len(lista_transacciones) + 1
    lista_transacciones.append(transaccion_val)
    return transaccion_val


@app.get("/transacciones/{id}", response_model=Transaccion)
async def obtener_transaccion(id: int):
    for transaccion in lista_transacciones:
        if transaccion.id == id:
            return transaccion
    return {"mensaje": "Transacción no encontrada"}


@app.delete("/transacciones/{id}", response_model=Transaccion)
async def eliminar_transaccion(id: int):
    for transaccion in lista_transacciones:
        if transaccion.id == id:
            transaccion_eliminada = Transaccion.model_validate(transaccion.model_dump())
            lista_transacciones.remove(transaccion)
            return transaccion_eliminada
    return {"mensaje": "Transacción no encontrada"}


@app.put("/transacciones/{id}", response_model=Transaccion)
async def actualizar_transaccion(id: int, datos_transaccion: TransaccionCrear):
    for transaccion in lista_transacciones:
        if transaccion.id == id:
            transaccion_actualizada = Transaccion(
                id=transaccion.id,
                cliente_id=datos_transaccion.cliente_id,
                monto=datos_transaccion.monto,
                descripcion=datos_transaccion.descripcion
            )

            index = lista_transacciones.index(transaccion)
            lista_transacciones[index] = transaccion_actualizada
            return transaccion_actualizada

    return {"mensaje": "Transacción no encontrada"}

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
