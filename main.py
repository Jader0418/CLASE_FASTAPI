from fastapi import FastAPI, HTTPException

app = FastAPI()


productos = {
    1: {"nombre": "Jamón", "stock": 20, "valor": 8000},
    2: {"nombre": "Salchicha", "stock": 35, "valor": 12000},
    3: {"nombre": "Chorizo", "stock": 15, "valor": 15000},
    4: {"nombre": "Mortadela", "stock": 10, "valor": 9000},
    5: {"nombre": "Tocineta", "stock": 8, "valor": 18000}
}

@app.get("/")
async def incio():
    return {"message": "Hola, ya estoy usando FastAPI! "}

@app.get("/saludo/{nombre}")
async def saludo(nombre: str):
    return {"message": f"Hola {nombre}, bienvenido a FastAPI!"}

@app.get("/cuadrado/{numero}")
async def calcular_cuadrado(numero: int):
    cuadrado = numero * numero
    return {"numero": numero, "cuadrado": cuadrado}


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
    
@app.post("/producto/{id}")
async def crear_producto(id: int, nombre: str, stock: int, valor: float):
    if id in productos:
        raise HTTPException(status_code=400, detail="El producto ya existe")

    productos[id] = {
        "nombre": nombre,
        "stock": stock,
        "valor": valor
    }

    return {"mensaje": "Producto creado", "producto": productos[id]}


# Actualizar producto
@app.put("/producto/{id}")
async def actualizar_producto(id: int, nombre: str, stock: int, valor: float):
    if id not in productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    productos[id] = {
        "nombre": nombre,
        "stock": stock,
        "valor": valor
    }

    return {"mensaje": "Producto actualizado", "producto": productos[id]}


# Eliminar producto 
@app.delete("/producto/{id}")
async def eliminar_producto(id: int):
    if id not in productos:
        
        raise HTTPException(status_code=404, detail="Producto no encontrado") 
# raise : generar un error / detiene inmediamente la ejecución de la función y devuelve una respuesta con el código de estado y el mensaje especificados.
# HTPException(...)  Es el tipo de error que estás enviando / No es un error cualquiera / Es un error especial para APIs web
# 404: significa que el recurso solicitado no se encontró en el servidor / El cliente hizo una solicitud para un recurso que no existe


    producto_eliminado = productos.pop(id)

    return {"mensaje": "Producto eliminado", "producto": producto_eliminado}