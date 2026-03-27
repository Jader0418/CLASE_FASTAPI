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