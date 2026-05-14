from pydantic import BaseModel

# Modelo base de factura
class FacturaBase(BaseModel):
    cliente_id: int
    monto: float
    descripcion: str | None = None


# Modelo para crear una factura
class FacturaCrear(FacturaBase):
    pass


# Modelo final de factura con ID
class Factura(FacturaBase):
    id: int | None = None