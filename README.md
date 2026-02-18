# KnightL / IronClash

Juego 2D Action RPG - Godot 4 + FastAPI

## Estructura

```
├── backend/          # API FastAPI (Python)
├── docs/             # Documentación
├── scenes/           # Escenas Godot
│   └── ui/           # MainMenu, Home, Combat, Settings
├── src/               # Scripts GDScript
│   ├── ui/
│   ├── network/       # APIClient, AuthManager
│   ├── systems/       # GameState
│   └── utils/         # SceneManager
├── config/            # api_config.gd
├── assets/            # sprites, audio, fonts
└── project.godot
```

## Requisitos

- Godot 4.2+
- Python 3.11+ (para backend)
- Backend corriendo en http://localhost:8000

## Ejecutar

### Backend
```bash
cd backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

### Cliente Godot
1. Abrir Godot 4
2. Importar proyecto (project.godot)
3. F5 o Play para ejecutar
4. Escena inicial: MainMenu (login)
5. API configurada en `config/api_config.gd` → localhost:8000

## Autoloads

- **ApiConfig** - URL del backend
- **SceneManager** - Navegación entre escenas
- **APIClient** - Cliente HTTP para la API
- **AuthManager** - Login/Logout
- **GameState** - Estado global del juego
