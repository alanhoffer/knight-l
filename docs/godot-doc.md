# Godot Client Documentation - IronClash

## Tabla de Contenidos
1. [Arquitectura General](#arquitectura-general)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Configuración y Setup](#configuración-y-setup)
4. [Sistemas Principales](#sistemas-principales)
5. [Escenas y Nodos](#escenas-y-nodos)
6. [Comunicación con Backend](#comunicación-con-backend)
7. [Sistema de Input](#sistema-de-input)
8. [Sistema de Combate](#sistema-de-combate)
9. [Sistema de Mapas](#sistema-de-mapas)
10. [Sistema de Housing](#sistema-de-housing)
11. [Convenciones de Código](#convenciones-de-código)

---

## Arquitectura General

### Patrón Arquitectónico
El cliente Godot sigue una arquitectura basada en **Escenas y Nodos** con separación de responsabilidades:

```
┌─────────────────────────────────────┐
│      UI Layer (Scenes/UI)           │  ← Menús, HUD, Paneles
├─────────────────────────────────────┤
│   Gameplay Layer (Scenes/Game)      │  ← Combate, Mapas, Housing
├─────────────────────────────────────┤
│   Entity Layer (Scenes/Entities)   │  ← Personajes, Enemigos, Items
├─────────────────────────────────────┤
│   System Layer (Systems)            │  ← Lógica de sistemas
├─────────────────────────────────────┤
│   Network Layer (Network)           │  ← API Client, WebSocket
├─────────────────────────────────────┤
│   Data Layer (Data)                 │  ← Models, Config, Cache
└─────────────────────────────────────┘
```

### Principios
- **Escenas Modulares**: Cada funcionalidad es una escena independiente
- **Autoloads (Singletons)**: Para sistemas globales (API, GameState, etc.)
- **Señales (Signals)**: Comunicación desacoplada entre nodos
- **Resource System**: Para datos compartidos (items, stats, configs)

---

## Estructura del Proyecto

```
iron-clash-s/
├── project.godot                    # Configuración del proyecto
│
├── scenes/                         # Escenas del juego
│   ├── ui/                         # Escenas de UI
│   │   ├── MainMenu.tscn
│   │   ├── Home.tscn
│   │   ├── Combat.tscn
│   │   ├── StatsPanel.tscn
│   │   └── LevelUpPanel.tscn
│   │
│   ├── entities/                   # Entidades del juego
│   │   ├── Character.tscn
│   │   ├── CharacterWbones.tscn
│   │   ├── Enemy.tscn
│   │   └── Camera.tscn
│   │
│   ├── housing/                    # Escenas de housing
│   │   └── FurnitureItem.tscn
│   │
│   └── hud/                        # HUD elements
│       ├── HealthBar.tscn
│       └── InventoryPanel.tscn
│
├── src/                            # Scripts GDScript
│   ├── ui/                         # Scripts de UI
│   │   ├── main_menu.gd
│   │   ├── home.gd
│   │   ├── combat.gd
│   │   └── inventory_panel.gd
│   │
│   ├── entities/                   # Scripts de entidades
│   │   ├── character.gd
│   │   ├── enemy.gd
│   │   └── camera.gd
│   │
│   ├── systems/                    # Sistemas del juego
│   │   ├── combat_system.gd
│   │   ├── player_data.gd
│   │   └── furniture_item.gd
│   │
│   ├── network/                    # Comunicación con backend
│   │   ├── api_client.gd
│   │   ├── websocket_client.gd
│   │   └── auth_manager.gd
│   │
│   └── utils/                      # Utilidades
│       ├── scene_manager.gd
│       └── input_handler.gd
│
├── assets/                         # Assets del juego
│   ├── sprites/
│   │   ├── character/
│   │   ├── furniture/
│   │   └── weapons/
│   ├── audio/
│   └── fonts/
│
├── shaders/                        # Shaders personalizados
│   └── tile_texture.gdshader
│
└── config/                         # Archivos de configuración
    ├── game_config.gd
    └── api_config.gd
```

---

## Configuración y Setup

### Requisitos Previos
- Godot 4.2+
- Git

### Instalación

1. **Clonar repositorio**
```bash
git clone <repo-url>
cd iron-clash-s
```

2. **Abrir en Godot**
- Abrir Godot Editor
- Importar proyecto: `project.godot`
- Esperar a que se importen los assets

3. **Configurar Autoloads**
En `Project Settings > Autoload`:
- `SceneManager` (res://src/utils/scene_manager.gd)
- `APIClient` (res://src/network/api_client.gd)
- `AuthManager` (res://src/network/auth_manager.gd)
- `GameState` (res://src/systems/game_state.gd)

4. **Configurar API Endpoint**
Editar `config/api_config.gd`:
```gdscript
const API_BASE_URL = "http://localhost:8000/api/v1"
const WS_URL = "ws://localhost:8000/ws"
```

---

## Sistemas Principales

### SceneManager (Autoload)

Gestiona la navegación entre escenas.

```gdscript
# src/utils/scene_manager.gd
extends Node

signal scene_changed(scene_name: String)

var current_scene: String = ""

func change_scene(scene_path: String, transition: String = "fade"):
	match transition:
		"fade":
			_transition_fade(scene_path)
		"slide":
			_transition_slide(scene_path)
		_:
			get_tree().change_scene_to_file(scene_path)

func _transition_fade(scene_path: String):
	# Implementar fade out/in
	var fade = ColorRect.new()
	fade.color = Color.BLACK
	fade.modulate.a = 0.0
	add_child(fade)
	
	var tween = create_tween()
	tween.tween_property(fade, "modulate:a", 1.0, 0.3)
	await tween.finished
	
	get_tree().change_scene_to_file(scene_path)
	
	tween = create_tween()
	tween.tween_property(fade, "modulate:a", 0.0, 0.3)
	await tween.finished
	fade.queue_free()
```

**Uso:**
```gdscript
SceneManager.change_scene("res://scenes/ui/Combat.tscn", "fade")
```

---

### APIClient (Autoload)

Cliente HTTP para comunicación con el backend.

```gdscript
# src/network/api_client.gd
extends Node

const BASE_URL = "http://localhost:8000/api/v1"

var auth_token: String = ""

signal request_completed(response: Dictionary)
signal request_failed(error: String)

func _ready():
	pass

func set_auth_token(token: String):
	auth_token = token

func get_headers() -> Dictionary:
	var headers = {
		"Content-Type": "application/json"
	}
	if auth_token != "":
		headers["Authorization"] = "Bearer " + auth_token
	return headers

func request(
	endpoint: String,
	method: String = "GET",
	body: Dictionary = {}
) -> Dictionary:
	var url = BASE_URL + endpoint
	var http_request = HTTPRequest.new()
	add_child(http_request)
	
	http_request.request_completed.connect(_on_request_completed.bind(http_request))
	
	var headers = get_headers()
	var error
	
	match method:
		"GET":
			error = http_request.request(url, headers)
		"POST", "PUT", "DELETE":
			var json_body = JSON.stringify(body)
			error = http_request.request(url, headers, HTTPClient.METHOD_POST, json_body)
	
	if error != OK:
		request_failed.emit("Request failed: " + str(error))
		http_request.queue_free()
		return {}
	
	# Esperar respuesta
	var response = await http_request.request_completed
	http_request.queue_free()
	return response

func _on_request_completed(
	result: int,
	response_code: int,
	headers: PackedStringArray,
	body: PackedByteArray,
	http_request: HTTPRequest
):
	if response_code == 200:
		var json = JSON.new()
		json.parse(body.get_string_from_utf8())
		request_completed.emit(json.get_data())
	else:
		request_failed.emit("HTTP Error: " + str(response_code))
```

**Uso:**
```gdscript
# Login
var response = await APIClient.request("/auth/login", "POST", {
	"username": "player123",
	"password": "password"
})

# Obtener personaje
var character = await APIClient.request("/characters/1")
```

---

### AuthManager (Autoload)

Gestiona autenticación y sesión del usuario.

```gdscript
# src/network/auth_manager.gd
extends Node

signal login_success(user_data: Dictionary)
signal login_failed(error: String)
signal logout_complete()

var current_user: Dictionary = {}
var is_logged_in: bool = false

func login(username: String, password: String) -> bool:
	var response = await APIClient.request("/auth/login", "POST", {
		"username": username,
		"password": password
	})
	
	if response.has("access_token"):
		APIClient.set_auth_token(response.access_token)
		current_user = await get_current_user()
		is_logged_in = true
		login_success.emit(current_user)
		return true
	else:
		login_failed.emit("Invalid credentials")
		return false

func logout():
	APIClient.set_auth_token("")
	current_user = {}
	is_logged_in = false
	logout_complete.emit()

func get_current_user() -> Dictionary:
	var response = await APIClient.request("/auth/me")
	return response
```

---

### GameState (Autoload)

Estado global del juego.

```gdscript
# src/systems/game_state.gd
extends Node

var current_character: Dictionary = {}
var inventory: Array = []
var current_map: String = ""
var in_combat: bool = false
var combat_id: String = ""

signal character_changed(character: Dictionary)
signal inventory_updated(items: Array)

func set_character(character: Dictionary):
	current_character = character
	character_changed.emit(character)

func update_inventory(items: Array):
	inventory = items
	inventory_updated.emit(items)
```

---

## Escenas y Nodos

### MainMenu

Escena principal de menú.

**Estructura:**
```
MainMenu (Control)
├── Background (ColorRect)
├── Title (Label)
├── LoginPanel (Panel)
│   ├── UsernameInput (LineEdit)
│   ├── PasswordInput (LineEdit)
│   └── LoginButton (Button)
└── RegisterPanel (Panel)
    └── ...
```

**Script:**
```gdscript
# src/ui/main_menu.gd
extends Control

@onready var username_input = $LoginPanel/UsernameInput
@onready var password_input = $LoginPanel/PasswordInput
@onready var login_button = $LoginPanel/LoginButton

func _ready():
	login_button.pressed.connect(_on_login_pressed)
	AuthManager.login_success.connect(_on_login_success)

func _on_login_pressed():
	var username = username_input.text
	var password = password_input.text
	await AuthManager.login(username, password)

func _on_login_success(user_data: Dictionary):
	SceneManager.change_scene("res://scenes/ui/Home.tscn")
```

---

### Home (Housing)

Escena principal del juego (casa del jugador).

**Estructura:**
```
Home (Node2D)
├── MapLayer (Node2D)
│   ├── FloorBounds (ColorRect)
│   ├── Floor (Sprite2D)
│   ├── WallBounds (ColorRect)
│   └── Wall (Sprite2D)
├── FurnitureLayer (Node2D)
│   └── [Furniture items]
├── CharacterLayer (Node2D)
│   └── PlayerCharacter (CharacterBody2D)
├── UILayer (CanvasLayer)
│   ├── InventoryButton (Button)
│   ├── CombatButton (Button)
│   └── InventoryPanel (Panel)
└── Camera (Camera2D)
```

**Script Principal:**
```gdscript
# src/ui/home.gd
extends Node2D

@onready var character = $CharacterLayer/PlayerCharacter
@onready var inventory_panel = $UILayer/InventoryPanel
@onready var inventory_button = $UILayer/InventoryButton

var furniture_items: Array = []

func _ready():
	_setup_character()
	_setup_housing()
	inventory_button.pressed.connect(_on_inventory_button_pressed)

func _setup_character():
	if GameState.current_character.is_empty():
		# Cargar personaje desde API
		pass
	else:
		character.load_character(GameState.current_character)

func _setup_housing():
	# Cargar layout de casa desde API
	var housing_data = await APIClient.request("/housing")
	_load_furniture(housing_data.layout)

func _on_inventory_button_pressed():
	inventory_panel.visible = !inventory_panel.visible
```

---

### Combat

Escena de combate.

**Estructura:**
```
Combat (Node2D)
├── Arena (Node2D)
│   ├── Player (CharacterBody2D)
│   └── Enemy (CharacterBody2D)
├── UILayer (CanvasLayer)
│   ├── PlayerHealthBar (ProgressBar)
│   ├── EnemyHealthBar (ProgressBar)
│   └── ActionButtons (HBoxContainer)
│       ├── AttackButton (Button)
│       ├── DodgeButton (Button)
│       └── BlockButton (Button)
└── Camera (Camera2D)
```

**Script:**
```gdscript
# src/ui/combat.gd
extends Node2D

@onready var player = $Arena/Player
@onready var enemy = $Arena/Enemy
@onready var attack_button = $UILayer/ActionButtons/AttackButton

var combat_id: String = ""
var is_player_turn: bool = true

func _ready():
	attack_button.pressed.connect(_on_attack_pressed)
	_start_combat()

func _start_combat():
	# Iniciar combate con servidor
	var response = await APIClient.request("/combat/pve/start", "POST", {
		"character_id": GameState.current_character.id,
		"map_id": 1,
		"enemy_id": 5
	})
	
	combat_id = response.combat_id
	enemy.load_enemy(response.enemy)

func _on_attack_pressed():
	if not is_player_turn:
		return
	
	# Enviar acción al servidor
	var response = await APIClient.request("/combat/pve/action", "POST", {
		"combat_id": combat_id,
		"action_type": "attack",
		"timestamp": Time.get_ticks_msec()
	})
	
	# Aplicar resultado visualmente
	_apply_combat_result(response)
```

---

## Sistema de Input

### InputHandler

Maneja input multiplataforma (teclado, mouse, touch, gamepad).

```gdscript
# src/utils/input_handler.gd
extends Node

enum InputType {
	KEYBOARD,
	TOUCH,
	GAMEPAD
}

var current_input_type: InputType = InputType.KEYBOARD

signal move_input(direction: Vector2)
signal attack_input()
signal dodge_input()
signal block_input()

func _ready():
	# Detectar tipo de input
	if Input.get_connected_joypads().size() > 0:
		current_input_type = InputType.GAMEPAD

func _process(_delta):
	_handle_movement()
	_handle_actions()

func _handle_movement():
	var direction = Vector2.ZERO
	
	match current_input_type:
		InputType.KEYBOARD:
			direction.x = Input.get_axis("ui_left", "ui_right")
			direction.y = Input.get_axis("ui_up", "ui_down")
		InputType.GAMEPAD:
			direction = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
		InputType.TOUCH:
			# Manejar touch input
			pass
	
	if direction.length() > 0:
		move_input.emit(direction.normalized())

func _handle_actions():
	if Input.is_action_just_pressed("attack"):
		attack_input.emit()
	if Input.is_action_just_pressed("dodge"):
		dodge_input.emit()
	if Input.is_action_just_pressed("block"):
		block_input.emit()
```

**Input Map (Project Settings):**
- `ui_left`: A / Left Arrow
- `ui_right`: D / Right Arrow
- `ui_up`: W / Up Arrow
- `ui_down`: S / Down Arrow
- `attack`: Space / Mouse Left
- `dodge`: Shift / Mouse Right
- `block`: Ctrl

---

## Sistema de Combate

### Character (Entity)

Script base para personajes (jugador y enemigos).

```gdscript
# src/entities/character.gd
extends CharacterBody2D

@export var max_hp: int = 100
@export var hp: int = 100
@export var atk: int = 10
@export var def: int = 5
@export var spd: int = 100
@export var crit: int = 10
@export var eva: int = 5

@onready var sprite = $Sprite2D
@onready var health_bar = $HealthBar

signal health_changed(new_hp: int)
signal died()

func _ready():
	_update_health_bar()

func take_damage(amount: int, is_critical: bool = false):
	if is_critical:
		amount = int(amount * 1.5)
	
	hp = max(0, hp - amount)
	health_changed.emit(hp)
	_update_health_bar()
	
	if hp <= 0:
		died.emit()

func heal(amount: int):
	hp = min(max_hp, hp + amount)
	health_changed.emit(hp)
	_update_health_bar()

func _update_health_bar():
	if health_bar:
		health_bar.value = (float(hp) / float(max_hp)) * 100.0
```

---

## Sistema de Mapas

### MapManager

Gestiona carga y transición entre mapas.

```gdscript
# src/systems/map_manager.gd
extends Node

var current_map: Node2D = null
var map_data: Dictionary = {}

signal map_loaded(map_id: int)
signal map_transition(map_id: int)

func load_map(map_id: int):
	# Cargar datos del mapa desde API
	map_data = await APIClient.request("/maps/" + str(map_id))
	
	# Cargar escena del mapa
	var map_scene = load("res://scenes/maps/Map" + str(map_id) + ".tscn")
	current_map = map_scene.instantiate()
	
	# Spawnear enemigos
	_spawn_enemies(map_data.enemies)
	
	map_loaded.emit(map_id)

func _spawn_enemies(enemies: Array):
	for enemy_data in enemies:
		var enemy_scene = load("res://scenes/entities/Enemy.tscn")
		var enemy = enemy_scene.instantiate()
		enemy.load_enemy_data(enemy_data)
		current_map.get_node("EnemyLayer").add_child(enemy)
```

---

## Sistema de Housing

### FurnitureItem

Item de mueble que se puede colocar en la casa.

```gdscript
# src/systems/furniture_item.gd
extends RigidBody2D

@export var furniture_id: int
@export var furniture_type: String  # "floor" | "wall"
@export var can_drag: bool = true

var is_being_dragged: bool = false
var original_position: Vector2

signal furniture_placed(position: Vector2)
signal furniture_removed()

func _ready():
	_setup_physics()

func _setup_physics():
	if furniture_type == "floor":
		gravity_scale = 1.0
		collision_layer = 4
		collision_mask = 2
	else:
		gravity_scale = 0.0
		lock_rotation = true

func _input_event(_viewport, event, _shape_idx):
	if event is InputEventMouseButton and event.pressed:
		if event.button_index == MOUSE_BUTTON_LEFT and can_drag:
			_start_drag()

func _start_drag():
	is_being_dragged = true
	original_position = global_position

func _process(_delta):
	if is_being_dragged:
		global_position = get_global_mouse_position()

func _input(event):
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_LEFT and not event.pressed:
			if is_being_dragged:
				_end_drag()

func _end_drag():
	is_being_dragged = false
	# Validar posición y guardar
	if _is_valid_position():
		furniture_placed.emit(global_position)
		_save_position()
	else:
		global_position = original_position

func _is_valid_position() -> bool:
	# Validar que no colisione con otros muebles
	# y que esté en la capa correcta
	return true

func _save_position():
	# Guardar posición en servidor
	await APIClient.request("/housing/furniture", "POST", {
		"furniture_id": furniture_id,
		"position": {"x": global_position.x, "y": global_position.y},
		"layer": furniture_type
	})
```

---

## Convenciones de Código

### Nombres
- **Archivos**: `snake_case.gd`
- **Clases**: `PascalCase` (en comentarios)
- **Variables**: `snake_case`
- **Constantes**: `UPPER_SNAKE_CASE`
- **Señales**: `signal_name_here`

### Type Hints
Siempre usar type hints cuando sea posible:
```gdscript
var health: int = 100
var position: Vector2 = Vector2.ZERO
var items: Array[Dictionary] = []

func calculate_damage(atk: int, def: int) -> int:
	return max(1, atk - def)
```

### @onready
Usar `@onready` para referencias a nodos:
```gdscript
@onready var health_bar = $HealthBar
@onready var attack_button = $UILayer/ActionButtons/AttackButton
```

### Señales
Usar señales para comunicación desacoplada:
```gdscript
signal health_changed(new_hp: int)
signal item_collected(item: Dictionary)

func _on_enemy_died():
	item_collected.emit(dropped_item)
```

### Async/Await
Usar `await` para operaciones asíncronas:
```gdscript
func load_character_data(character_id: int):
	var response = await APIClient.request("/characters/" + str(character_id))
	character.load_data(response)
```

### Grupos
Usar grupos para identificar nodos:
```gdscript
# En el editor o código
add_to_group("enemies")

# Buscar todos los enemigos
var enemies = get_tree().get_nodes_in_group("enemies")
```

---

## Recursos Adicionales

- [Godot Documentation](https://docs.godotengine.org/)
- [GDScript Style Guide](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html)
- [Godot Best Practices](https://docs.godotengine.org/en/stable/tutorials/best_practices/index.html)
