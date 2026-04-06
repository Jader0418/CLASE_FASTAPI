from fastapi import FastAPI, HTTPException

app = FastAPI()


productos = {
    1: {"nombre": "Jamón", "stock": 20, "valor": 8000},
    2: {"nombre": "Salchicha", "stock": 35, "valor": 12000},
    3: {"nombre": "Chorizo", "stock": 15, "valor": 15000},
    4: {"nombre": "Mortadela", "stock": 10, "valor": 9000},
    5: {"nombre": "Tocineta", "stock": 8, "valor": 18000}
}

# Generar ID automático
def generar_id():
    if productos:
        return max(productos.keys()) + 1
    return 1

@app.get("/")
async def incio():
    return {"message": "INICIO DE INVENTARIO !! QUESOS UBATE !!! "}

@app.get("/saludo/{nombre}")
async def saludo(nombre: str):
    return {"message": f"Hola {nombre}, bienvenido a FastAPI!"}

@app.get("/cuadrado/{numero}")
async def calcular_cuadrado(numero: int):
    cuadrado = numero * numero
    return {"numero": numero, "cuadrado": cuadrado}


# Listar productos de forma organizada
@app.get("/productos")
async def listar_productos():
    lista = []
    for id, datos in productos.items():
        lista.append({
            "id": id,
            "nombre": datos["nombre"],
            "stock": datos["stock"],
            "valor": datos["valor"]
        })
    return {"productos": lista}


@app.get("/producto/{id}")
async def obtener_producto(id: int):
    
    if id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return {
        "id": id,
        "nombre": productos[id]["nombre"],
        "stock": productos[id]["stock"],
        "valor": productos[id]["valor"]
    }
    

# Crear producto con ID automático y validación de nombre
@app.post("/producto")
async def crear_producto(nombre: str, stock: int, valor: float):

    # Validar que el nombre no exista
    for producto in productos.values():
        if producto["nombre"].lower() == nombre.lower():
            raise HTTPException(status_code=400, detail="El producto ya existe")

    nuevo_id = generar_id()

    productos[nuevo_id] = {
        "nombre": nombre,
        "stock": stock,
        "valor": valor
    }

    return {
        "mensaje": "Producto creado",
        "producto": {
            "id": nuevo_id,
            "nombre": nombre,
            "stock": stock,
            "valor": valor
        }
    }


# Actualizar producto
@app.put("/producto/{id}")
async def actualizar_producto(id: int, nombre: str, stock: int, valor: float):
    if id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    # Validar nombre duplicado en otros productos
    for clave, producto in productos.items():
        if clave != id and producto["nombre"].lower() == nombre.lower():
            raise HTTPException(status_code=400, detail="El nombre ya está en uso")

    productos[id] = {
        "nombre": nombre,
        "stock": stock,
        "valor": valor
    }

    return {"mensaje": "¡¡ Producto actualizado !! ", "producto": productos[id]}


# Eliminar producto 
@app.delete("/producto/{id}")
async def eliminar_producto(id: int):
    if id not in productos:
    
        raise HTTPException(status_code=404, detail="Producto no encontrado") 
    
# """raise : generar un error / detiene inmediamente la ejecución de la función y devuelve una respuesta con el código de estado y el mensaje especificados.
# HTPException(...)  Es el tipo de error que estás enviando / No es un error cualquiera / Es un error especial para APIs web
# 404: significa que el recurso solicitado no se encontró en el servidor / El cliente hizo una solicitud para un recurso que no existe


    producto_eliminado = productos.pop(id) 
    #pop: Elimina el elemento con la clave especificada y devuelve su valor. Si la clave no existe, se puede proporcionar un valor predeterminado opcional que se devolverá en su lugar. Si no se proporciona un valor predeterminado y la clave no existe, se generará un error KeyError.

    return {"mensaje": "Producto eliminado", "producto": producto_eliminado}