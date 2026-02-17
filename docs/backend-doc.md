# Backend Documentation - IronClash

## Tabla de Contenidos
1. [Arquitectura General](#arquitectura-general)
2. [Stack Tecnológico](#stack-tecnológico)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Configuración y Setup](#configuración-y-setup)
5. [Arquitectura de Código](#arquitectura-de-código)
6. [APIs y Endpoints](#apis-y-endpoints)
7. [Sistemas Principales](#sistemas-principales)
8. [Base de Datos](#base-de-datos)
9. [WebSockets](#websockets)
10. [Seguridad y Validación](#seguridad-y-validación)
11. [Convenciones de Código](#convenciones-de-código)

---

## Arquitectura General

### Patrón Arquitectónico
El backend sigue una **Arquitectura Limpia (Clean Architecture)** con separación de responsabilidades:

```
┌─────────────────────────────────────┐
│         API Layer (FastAPI)         │  ← Endpoints REST/WebSocket
├─────────────────────────────────────┤
│      Service Layer (Business)        │  ← Lógica de negocio
├─────────────────────────────────────┤
│      Domain Layer (Models)           │  ← Entidades y reglas de dominio
├─────────────────────────────────────┤
│   Infrastructure Layer (DB/Cache)   │  ← PostgreSQL, Redis, External APIs
└─────────────────────────────────────┘
```

### Principios
- **Separación de Responsabilidades**: Cada capa tiene una responsabilidad única
- **Dependencia Inversa**: Las capas superiores no dependen de las inferiores directamente
- **Autoritativo**: El servidor es la fuente de verdad para todas las acciones críticas
- **Validación en Servidor**: Todas las acciones del cliente se validan en el servidor

---

## Stack Tecnológico

### Core
- **Python 3.11+**: Lenguaje principal
- **FastAPI**: Framework web asíncrono
- **Pydantic**: Validación de datos y modelos
- **SQLAlchemy**: ORM para PostgreSQL
- **Alembic**: Migraciones de base de datos
- **Redis**: Caché y sesiones
- **WebSockets**: Comunicación en tiempo real (PvP, Torneos)

### Base de Datos
- **PostgreSQL 14+**: Base de datos principal
- **Redis 7+**: Caché y colas

### Herramientas
- **uvicorn**: Servidor ASGI
- **pytest**: Testing
- **black**: Formateo de código
- **mypy**: Type checking
- **pre-commit**: Hooks de git

---

## Estructura del Proyecto

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada FastAPI
│   ├── config.py               # Configuración (env vars)
│   │
│   ├── api/                    # API Layer
│   │   ├── __init__.py
│   │   ├── deps.py             # Dependencias (auth, DB)
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py         # Login, Register, Token
│   │   │   ├── characters.py   # CRUD personajes
│   │   │   ├── combat.py       # Iniciar combate, resultados
│   │   │   ├── maps.py         # Mapas, enemigos, drops
│   │   │   ├── gear.py         # Items, equipamiento
│   │   │   ├── housing.py      # Casa, muebles, almacenamiento
│   │   │   ├── pvp.py          # Matchmaking, ranking
│   │   │   ├── shop.py         # Tienda, compras
│   │   │   └── websocket.py    # WebSocket endpoints
│   │   │
│   ├── services/               # Service Layer
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── character_service.py
│   │   ├── combat_service.py
│   │   ├── map_service.py
│   │   ├── gear_service.py
│   │   ├── housing_service.py
│   │   ├── pvp_service.py
│   │   ├── matchmaking_service.py
│   │   └── ranking_service.py
│   │
│   ├── domain/                 # Domain Layer
│   │   ├── __init__.py
│   │   ├── models/             # Modelos de dominio
│   │   │   ├── user.py
│   │   │   ├── character.py
│   │   │   ├── gear.py
│   │   │   ├── combat.py
│   │   │   ├── map.py
│   │   │   └── housing.py
│   │   ├── schemas/            # Pydantic schemas
│   │   │   ├── user.py
│   │   │   ├── character.py
│   │   │   ├── combat.py
│   │   │   └── ...
│   │   └── enums.py            # Enumeraciones
│   │
│   ├── infrastructure/         # Infrastructure Layer
│   │   ├── __init__.py
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   ├── base.py         # Base de SQLAlchemy
│   │   │   ├── session.py       # Session manager
│   │   │   └── models/         # Modelos SQLAlchemy
│   │   │       ├── user.py
│   │   │       ├── character.py
│   │   │       ├── gear.py
│   │   │       └── ...
│   │   ├── cache/
│   │   │   ├── __init__.py
│   │   │   └── redis_client.py
│   │   └── repositories/       # Repositorios (acceso a datos)
│   │       ├── user_repository.py
│   │       ├── character_repository.py
│   │       └── ...
│   │
│   └── utils/                  # Utilidades
│       ├── __init__.py
│       ├── security.py         # JWT, hashing
│       ├── validators.py       # Validaciones custom
│       └── exceptions.py       # Excepciones custom
│
├── alembic/                    # Migraciones
│   ├── versions/
│   └── env.py
│
├── tests/                      # Tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_api/
│   ├── test_services/
│   └── test_domain/
│
├── .env.example               # Variables de entorno ejemplo
├── .gitignore
├── pyproject.toml             # Dependencias y config
├── alembic.ini
└── README.md
```

---

## Configuración y Setup

### Requisitos Previos
- Python 3.11+
- PostgreSQL 14+
- Redis 7+
- Git

### Instalación

1. **Clonar repositorio**
```bash
git clone <repo-url>
cd backend
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

5. **Configurar base de datos**
```bash
# Crear base de datos PostgreSQL
createdb ironclash_db

# Ejecutar migraciones
alembic upgrade head
```

6. **Iniciar servidor**
```bash
uvicorn app.main:app --reload
```

### Variables de Entorno (.env)

```env
# App
APP_NAME=IronClash Backend
APP_VERSION=1.0.0
DEBUG=True
ENVIRONMENT=development

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/ironclash_db

# Redis
REDIS_URL=redis://localhost:6379/0

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:8080

# Game Settings
MAX_LIVES=5
LIFE_REGENERATION_MINUTES=25
MAX_CHEST_SLOTS=5
```

---

## Arquitectura de Código

### Flujo de Request

```
Client Request
    ↓
API Endpoint (FastAPI Router)
    ↓
Dependency Injection (Auth, DB Session)
    ↓
Service Layer (Business Logic)
    ↓
Repository Layer (Data Access)
    ↓
Database/Redis
    ↓
Response (Pydantic Schema)
```

### Ejemplo de Flujo Completo

```python
# api/v1/characters.py
@router.get("/{character_id}", response_model=CharacterResponse)
async def get_character(
    character_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Obtener personaje del usuario"""
    character = await character_service.get_character(
        db=db,
        character_id=character_id,
        user_id=current_user.id
    )
    return character

# services/character_service.py
async def get_character(
    db: Session,
    character_id: int,
    user_id: int
) -> CharacterResponse:
    """Obtener personaje validando ownership"""
    character = await character_repository.get_by_id(db, character_id)
    
    if not character or character.user_id != user_id:
        raise NotFoundException("Character not found")
    
    return CharacterResponse.from_orm(character)
```

---

## APIs y Endpoints

### Autenticación

#### `POST /api/v1/auth/register`
Registrar nuevo usuario

**Request:**
```json
{
  "username": "player123",
  "email": "player@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "user_id": 1,
  "username": "player123",
  "email": "player@example.com",
  "created_at": "2024-01-01T00:00:00Z"
}
```

#### `POST /api/v1/auth/login`
Iniciar sesión

**Request:**
```json
{
  "username": "player123",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

#### `GET /api/v1/auth/me`
Obtener usuario actual (requiere autenticación)

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "user_id": 1,
  "username": "player123",
  "email": "player@example.com"
}
```

---

### Personajes

#### `POST /api/v1/characters`
Crear nuevo personaje

**Request:**
```json
{
  "name": "Warrior",
  "class": "warrior"
}
```

#### `GET /api/v1/characters`
Listar personajes del usuario

#### `GET /api/v1/characters/{character_id}`
Obtener personaje específico

#### `PUT /api/v1/characters/{character_id}`
Actualizar personaje

#### `POST /api/v1/characters/{character_id}/level-up`
Subir de nivel (seleccionar mejora)

**Request:**
```json
{
  "improvement_id": 2
}
```

---

### Combate

#### `POST /api/v1/combat/pve/start`
Iniciar combate PvE

**Request:**
```json
{
  "character_id": 1,
  "map_id": 1,
  "enemy_id": 5
}
```

**Response:**
```json
{
  "combat_id": "uuid-here",
  "enemy": {
    "id": 5,
    "name": "Goblin",
    "hp": 100,
    "max_hp": 100,
    "stats": {...}
  }
}
```

#### `POST /api/v1/combat/pve/action`
Enviar acción de combate

**Request:**
```json
{
  "combat_id": "uuid-here",
  "action_type": "attack",
  "timestamp": 1234567890
}
```

**Response:**
```json
{
  "action_id": "action-uuid",
  "damage_dealt": 25,
  "is_critical": false,
  "enemy_hp": 75,
  "validated": true
}
```

#### `POST /api/v1/combat/pve/end`
Finalizar combate

**Request:**
```json
{
  "combat_id": "uuid-here",
  "result": "victory"
}
```

**Response:**
```json
{
  "result": "victory",
  "xp_gained": 100,
  "items_dropped": [
    {"item_id": 1, "name": "Iron Sword", "rarity": "common"}
  ],
  "coins_gained": 50
}
```

---

### Mapas

#### `GET /api/v1/maps`
Listar mapas disponibles

**Response:**
```json
[
  {
    "map_id": 1,
    "name": "Forest",
    "level_requirement": 1,
    "enemy_types": [...],
    "loot_tables": [...]
  }
]
```

#### `GET /api/v1/maps/{map_id}`
Obtener información de mapa

#### `GET /api/v1/maps/{map_id}/enemies`
Listar enemigos del mapa

---

### Equipamiento

#### `GET /api/v1/gear/inventory`
Obtener inventario del personaje

#### `POST /api/v1/gear/equip`
Equipar item

**Request:**
```json
{
  "character_id": 1,
  "item_id": 5,
  "slot": "weapon"
}
```

#### `POST /api/v1/gear/unequip`
Desequipar item

---

### Housing

#### `GET /api/v1/housing`
Obtener layout de casa del usuario

#### `POST /api/v1/housing/furniture`
Colocar mueble

**Request:**
```json
{
  "furniture_id": 1,
  "position": {"x": 10, "y": 5},
  "layer": "floor"
}
```

#### `GET /api/v1/housing/storage`
Obtener items almacenados

#### `POST /api/v1/housing/storage/deposit`
Guardar item en cofre

**Request:**
```json
{
  "chest_id": 1,
  "item_id": 10,
  "quantity": 1
}
```

#### `POST /api/v1/housing/storage/withdraw`
Retirar item de cofre

---

### PvP

#### `POST /api/v1/pvp/matchmaking/queue`
Entrar a cola de matchmaking

**Request:**
```json
{
  "character_id": 1
}
```

**Response:**
```json
{
  "queue_id": "queue-uuid",
  "estimated_wait": 30
}
```

#### `GET /api/v1/pvp/matchmaking/status`
Estado de matchmaking

#### `POST /api/v1/pvp/matchmaking/cancel`
Cancelar búsqueda

#### `GET /api/v1/pvp/ranking`
Obtener ranking

**Query Params:**
- `league`: bronce, plata, oro, etc.
- `limit`: número de resultados
- `offset`: paginación

---

## Sistemas Principales

### Sistema de Combate

El servidor valida todas las acciones de combate en tiempo real.

**Flujo:**
1. Cliente envía acción (ataque, dodge, block)
2. Servidor valida acción (cooldowns, posición, stats)
3. Servidor calcula resultado (daño, crítico, etc.)
4. Servidor responde con resultado validado
5. Cliente aplica resultado visualmente

**Validaciones:**
- Cooldowns de habilidades
- Posición del jugador
- Stats actuales
- Prevención de spam de acciones

### Sistema de Matchmaking

**Algoritmo:**
1. Buscar jugadores con rating similar (±200 puntos)
2. Considerar nivel del personaje
3. Tiempo de espera máximo: 60 segundos
4. Si no hay match, expandir rango de búsqueda

**Implementación:**
- Usa Redis para cola de matchmaking
- WebSocket para notificaciones en tiempo real

### Sistema de Ranking

**Cálculo ELO-like:**
```python
def calculate_rating_change(
    player_rating: int,
    opponent_rating: int,
    result: str  # "win" | "loss"
) -> int:
    expected_score = 1 / (1 + 10 ** ((opponent_rating - player_rating) / 400))
    k_factor = 32
    
    if result == "win":
        actual_score = 1
    else:
        actual_score = 0
    
    rating_change = int(k_factor * (actual_score - expected_score))
    return rating_change
```

**Ligas:**
- Bronce: 0-999
- Plata: 1000-1999
- Oro: 2000-2999
- Platino: 3000-3999
- Diamante: 4000-4999
- Master: 5000+

### Sistema de Drops

**Tablas de Loot:**
```python
class LootTable:
    items: List[LootEntry]
    
class LootEntry:
    item_id: int
    drop_chance: float  # 0.0 - 1.0
    min_quantity: int
    max_quantity: int
```

**Cálculo de Drop:**
1. Roll aleatorio (0.0 - 1.0)
2. Comparar con drop_chance
3. Si pasa, generar item con cantidad aleatoria
4. Aplicar modificadores (bosses tienen mejor loot)

---

## Base de Datos

### Esquema Principal

#### Users
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    last_login TIMESTAMP
);
```

#### Characters
```sql
CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    name VARCHAR(50) NOT NULL,
    level INTEGER DEFAULT 1,
    experience INTEGER DEFAULT 0,
    hp INTEGER NOT NULL,
    max_hp INTEGER NOT NULL,
    atk INTEGER NOT NULL,
    def INTEGER NOT NULL,
    spd INTEGER NOT NULL,
    crit INTEGER NOT NULL,
    eva INTEGER NOT NULL,
    lives INTEGER DEFAULT 5,
    max_lives INTEGER DEFAULT 5,
    last_life_regen TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Gear
```sql
CREATE TABLE gear (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(20) NOT NULL,  -- 'weapon' | 'armor'
    rarity VARCHAR(20) NOT NULL,  -- 'common' | 'uncommon' | 'rare' | 'epic' | 'legendary'
    atk_bonus INTEGER DEFAULT 0,
    def_bonus INTEGER DEFAULT 0,
    spd_bonus INTEGER DEFAULT 0,
    crit_bonus INTEGER DEFAULT 0,
    eva_bonus INTEGER DEFAULT 0,
    passive_effect JSONB
);
```

#### Character_Gear (Inventario)
```sql
CREATE TABLE character_gear (
    id SERIAL PRIMARY KEY,
    character_id INTEGER REFERENCES characters(id),
    gear_id INTEGER REFERENCES gear(id),
    quantity INTEGER DEFAULT 1,
    is_equipped BOOLEAN DEFAULT FALSE,
    slot VARCHAR(20)  -- 'weapon' | 'armor' | null
);
```

#### Maps
```sql
CREATE TABLE maps (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    level_requirement INTEGER DEFAULT 1,
    description TEXT
);
```

#### Enemies
```sql
CREATE TABLE enemies (
    id SERIAL PRIMARY KEY,
    map_id INTEGER REFERENCES maps(id),
    name VARCHAR(100) NOT NULL,
    level INTEGER NOT NULL,
    hp INTEGER NOT NULL,
    atk INTEGER NOT NULL,
    def INTEGER NOT NULL,
    spd INTEGER NOT NULL,
    loot_table_id INTEGER
);
```

#### Housing
```sql
CREATE TABLE housing (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    floor_texture VARCHAR(100),
    wall_texture VARCHAR(100),
    layout JSONB  -- Posiciones de muebles
);

CREATE TABLE furniture (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    furniture_type_id INTEGER,
    position_x INTEGER,
    position_y INTEGER,
    layer VARCHAR(10)  -- 'floor' | 'wall'
);

CREATE TABLE storage_chests (
    id SERIAL PRIMARY KEY,
    housing_id INTEGER REFERENCES housing(id),
    furniture_id INTEGER REFERENCES furniture(id),
    capacity INTEGER DEFAULT 50
);

CREATE TABLE stored_items (
    id SERIAL PRIMARY KEY,
    chest_id INTEGER REFERENCES storage_chests(id),
    item_id INTEGER,
    quantity INTEGER DEFAULT 1
);
```

---

## WebSockets

### Conexión

**Endpoint:** `ws://api.ironclash.com/ws/pvp`

**Autenticación:**
```json
{
  "type": "auth",
  "token": "jwt-token-here"
}
```

### Mensajes

#### Cliente → Servidor

**Acción de Combate:**
```json
{
  "type": "combat_action",
  "combat_id": "uuid",
  "action": "attack",
  "timestamp": 1234567890
}
```

**Movimiento:**
```json
{
  "type": "movement",
  "position": {"x": 100, "y": 200},
  "velocity": {"x": 5, "y": 0}
}
```

#### Servidor → Cliente

**Acción Validada:**
```json
{
  "type": "action_validated",
  "action_id": "uuid",
  "damage": 25,
  "enemy_hp": 75
}
```

**Match Encontrado:**
```json
{
  "type": "match_found",
  "opponent": {
    "character_id": 2,
    "name": "Enemy",
    "rating": 1200
  },
  "arena_id": 1
}
```

---

## Seguridad y Validación

### Autenticación JWT

```python
from datetime import datetime, timedelta
from jose import JWTError, jwt

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

### Validación de Acciones

**Rate Limiting:**
- Máximo 10 acciones por segundo por jugador
- Usa Redis para tracking

**Validación de Posición:**
```python
def validate_position(
    current_pos: Position,
    new_pos: Position,
    max_speed: float,
    delta_time: float
) -> bool:
    distance = calculate_distance(current_pos, new_pos)
    max_distance = max_speed * delta_time
    
    if distance > max_distance * 1.2:  # 20% tolerancia
        return False  # Posible teleport/cheat
    return True
```

**Validación de Daño:**
```python
def validate_damage(
    attacker_stats: Stats,
    defender_stats: Stats,
    reported_damage: int
) -> bool:
    expected_damage = calculate_damage(attacker_stats, defender_stats)
    tolerance = expected_damage * 0.1  # 10% tolerancia
    
    if abs(reported_damage - expected_damage) > tolerance:
        return False  # Daño manipulado
    return True
```

---

## Convenciones de Código

### Nombres
- **Archivos**: `snake_case.py`
- **Clases**: `PascalCase`
- **Funciones/Métodos**: `snake_case`
- **Constantes**: `UPPER_SNAKE_CASE`
- **Variables**: `snake_case`

### Type Hints
Siempre usar type hints:
```python
def calculate_damage(
    attacker_atk: int,
    defender_def: int,
    is_critical: bool = False
) -> int:
    base_damage = max(1, attacker_atk - defender_def)
    if is_critical:
        return int(base_damage * 1.5)
    return base_damage
```

### Async/Await
Usar async para operaciones I/O:
```python
async def get_character(
    db: Session,
    character_id: int
) -> Character:
    result = await db.execute(
        select(Character).where(Character.id == character_id)
    )
    return result.scalar_one_or_none()
```

### Manejo de Errores
```python
from app.utils.exceptions import NotFoundException, ValidationException

async def get_character(...):
    character = await repository.get_by_id(db, character_id)
    if not character:
        raise NotFoundException("Character not found")
    return character
```

### Logging
```python
import logging

logger = logging.getLogger(__name__)

async def process_combat(...):
    logger.info(f"Processing combat {combat_id}")
    try:
        result = await combat_service.process(...)
        logger.info(f"Combat {combat_id} completed: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in combat {combat_id}: {e}", exc_info=True)
        raise
```

---

## Testing

### Estructura de Tests
```
tests/
├── conftest.py          # Fixtures compartidos
├── test_api/
│   ├── test_auth.py
│   ├── test_characters.py
│   └── test_combat.py
├── test_services/
│   ├── test_combat_service.py
│   └── test_matchmaking_service.py
└── test_domain/
    └── test_models.py
```

### Ejemplo de Test
```python
import pytest
from app.services.combat_service import calculate_damage

def test_calculate_damage():
    damage = calculate_damage(attacker_atk=100, defender_def=50)
    assert damage == 50

def test_calculate_critical_damage():
    damage = calculate_damage(attacker_atk=100, defender_def=50, is_critical=True)
    assert damage == 75
```

### Ejecutar Tests
```bash
pytest
pytest tests/test_combat_service.py -v
pytest --cov=app tests/  # Con coverage
```

---

## Deployment

### Docker

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/ironclash
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis

  db:
    image: postgres:14
    environment:
      - POSTGRES_DB=ironclash
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

---

## Recursos Adicionales

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
