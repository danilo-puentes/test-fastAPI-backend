# FastAPI TODO (Hexagonal Architecture)

Aplicación TODO con FastAPI siguiendo una arquitectura hexagonal sencilla.

## Ejecutar con Docker

```bash
docker build -t fastapi-todo .
docker run -p 8000:8000 fastapi-todo
```

API disponible en `http://localhost:8000`. Documentación interactiva en `/docs` y `/redoc`.

## Endpoints

- `GET /api/tasks/` listar tareas
- `POST /api/tasks/` crear tarea
- `GET /api/tasks/{id}/` obtener tarea
- `PUT /api/tasks/{id}/` actualizar tarea
- `DELETE /api/tasks/{id}/` eliminar tarea

## Desarrollo local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

La base de datos usa SQLite por defecto (`sqlite:///./db.sqlite3`). Ajusta `DATABASE_URL` en un archivo `.env` si necesitas otro motor.
