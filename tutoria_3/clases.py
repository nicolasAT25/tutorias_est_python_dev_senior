class Categoria:
    def __init__(self, nombre: str, subcategoria: str):
        self.nombre = nombre
        self.subcategoria = subcategoria
        
    def __str__(self):
        return f"{self.nombre} / {self.subcategoria}"
    
class Producto:
    def __init__(self, nombre: str, cantidad: int, precio_unitario:float, categoria: Categoria, id:int = None):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.valor_total = self.cantidad * self.precio_unitario
        self.categoria = categoria
        self.id = id

    def __str__(self):
        return f"""
ID : {self.id}
Categoría: {self.categoria}
Producto: {self.nombre}
Cantidad: {self.cantidad}
Precio Unitario: ${self.precio_unitario:,.2f}
Valor Total: ${self.valor_total:,.2f}
"""