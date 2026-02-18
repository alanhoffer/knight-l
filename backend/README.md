# IronClash Backend

Backend API para IronClash - FastAPI + SQLite (local) / PostgreSQL (producción) + Redis.

## Estructura

```
backend/
├── app/
│   ├── api/          # API Layer - endpoints y dependencias
│   ├── services/     # Service Layer - lógica de negocio
│   ├── domain/       # Domain Layer - modelos y esquemas
│   ├── infrastructure/  # DB, Redis, repositorios
│   └── utils/        # Utilidades
├── alembic/          # Migraciones de BD
├── requirements.txt
└── .env.example
```

## Requisitos

- Python 3.11+
- SQLite (incluido en Python, sin instalación extra) para desarrollo local
- PostgreSQL 14+ y Redis 7+ para producción

## Instalación

1. **Crear entorno virtual**
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tus credenciales
   ```

4. **Base de datos**
   - Por defecto usa **SQLite**: se crea `ironclash.db` automáticamente al ejecutar migraciones
   - Para PostgreSQL en producción: crear la BD y poner `DATABASE_URL` en `.env`

5. **Ejecutar migraciones** (cuando existan)
   ```bash
   alembic upgrade head
   ```

## Ejecutar

```bash
uvicorn app.main:app --reload
```

- API: http://localhost:8000
- Docs: http://localhost:8000/docs (si DEBUG=True)

## Tests

```bash
pytest
pytest -v          # Verbose
pytest tests/test_api/  # Solo tests de API
```

Los tests usan SQLite en memoria; no requieren PostgreSQL ni Redis corriendo.
