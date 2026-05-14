from pydantic import BaseModel

# Modelo base de transacciones
class TransaccionesBase(BaseModel):
    cliente_id: int
    monto: float
    descripcion: str | None = None


# Modelo para crear una transacción
class TransaccionCrear(TransaccionesBase):
    pass


# Modelo final de transacción con ID
class Transaccion(TransaccionesBase):
    id: int | None = None