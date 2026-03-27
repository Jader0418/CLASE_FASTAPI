from fastapi import FastAPI, HTTPException

app = FastAPI()

productos = {
    1: {"nombre": "Teclado", "stock": 10, "valor": 50000},
    2: {"nombre": "Mouse", "stock": 5, "valor": 30000},
    3: {"nombre": "Monitor", "stock": 2, "valor": 800000}
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
    
    return {
        "id": id,
        "nombre": productos[id]["nombre"],
        "stock": productos[id]["stock"],
        "valor": productos[id]["valor"]
    }