from fastapi import FastAPI

app = FastAPI()
@app.get("/")

async def incio():
    return {"message": "Hola, ya estoy usando FastAPI! "}

@app.get("/saludo/{nombre}")
async def saludo(nombre: str):
    return {"message": f"Hola {nombre}, bienvenido a FastAPI!"}

@app.get("/cuadrado/{numero}")
async def cuadrado(numero: int):
    cuadrado = numero ** numero
    return {"numero": numero, "cuadrado": cuadrado}

