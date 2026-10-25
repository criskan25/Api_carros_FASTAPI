# API de Carros con FastAPI

API REST desarrollada con Python y FastAPI para administrar información de automóviles mediante operaciones CRUD.

## Funcionalidades

- GET: Consultar todos los carros.
- GET por ID: Consultar un carro específico.
- POST: Registrar un carro nuevo.
- PUT: Actualizar completamente un carro.
- PATCH: Actualizar parcialmente los datos de un carro.
- DELETE: Eliminar un carro por su ID.

## Tecnologías utilizadas

- Python
- FastAPI
- Pydantic
- Uvicorn

## Instalación

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar la API

Desde la carpeta del proyecto:

```bash
python -m uvicorn main:app --reload --port 8090
```

Abrir la documentación interactiva:

http://127.0.0.1:8090/docs

## Almacenamiento

Actualmente, los datos se almacenan en una lista de Python.

Los cambios se pierden al reiniciar el servidor.

## Objetivo

Proyecto desarrollado para practicar Python, FastAPI, creación de endpoints, operaciones CRUD y manejo de respuestas HTTP.
