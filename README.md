# CLASE_FASTAPI

Una aplicación simple construida con **FastAPI** que proporciona tres endpoints básicos para demostrar los conceptos fundamentales del framework.

## 📋 Descripción

Este proyecto es una introducción práctica a FastAPI, mostrando:
- Creación de una aplicación FastAPI
- Definición de rutas GET
- Parámetros de rutas
- Respuestas JSON

## ⚙️ Requisitos

- Python 3.7+
- FastAPI
- Uvicorn

## 🚀 Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd CLASE_FASTAPI
   ```

2. **Crear un entorno virtual** (si aún no lo has hecho)
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**
   - En Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Instalar las dependencias**
   ```bash
   pip install fastapi uvicorn
   ```

## 📡 Uso

1. **Iniciar el servidor**
   ```bash
   uvicorn main:app --reload
   ```

   El servidor se ejecutará en `http://127.0.0.1:8000`

2. **Acceder a la documentación interactiva**
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## 🔗 Endpoints

### 1. Inicio
- **Ruta**: `GET /`
- **Descripción**: Devuelve un mensaje de bienvenida
- **Respuesta**:
  ```json
  {
    "message": "Hola, ya estoy usando FastAPI! "
  }
  ```

### 2. Saludo Personalizado
- **Ruta**: `GET /saludo/{nombre}`
- **Parámetro**: `nombre` (string) - Nombre de la persona
- **Descripción**: Saluda a una persona por su nombre
- **Ejemplo**: `GET /saludo/Juan`
- **Respuesta**:
  ```json
  {
    "message": "Hola Juan, bienvenido a FastAPI!"
  }
  ```

### 3. Cálculo de Potencia
- **Ruta**: `GET /cuadrado/{numero}`
- **Parámetro**: `numero` (integer) - Número para calcular
- **Descripción**: Calcula numero elevado a numero (número^número)
- **Ejemplo**: `GET /cuadrado/3`
- **Respuesta**:
  ```json
  {
    "numero": 3,
    "cuadrado": 27
  }
  ```

## 😊 Ejemplo de uso con curl

```bash
# Obtener el saludo inicial
curl http://127.0.0.1:8000/

# Saludo personalizado
curl http://127.0.0.1:8000/saludo/Carlos

# Calcular potencia
curl http://127.0.0.1:8000/cuadrado/5
```

## 📚 Más información

- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de Uvicorn](https://www.uvicorn.org/)

## 📝 Licencia

Este proyecto es de uso educativo.
