extends Node2D

## Pantalla principal del jugador (casa/housing)
## Placeholder - se expande en sprints posteriores

@onready var combat_button: Button = $UILayer/CombatButton
@onready var settings_button: Button = $UILayer/SettingsButton
@onready var logout_button: Button = $UILayer/LogoutButton


func _ready() -> void:
	combat_button.pressed.connect(_on_combat_pressed)
	settings_button.pressed.connect(_on_settings_pressed)
	logout_button.pressed.connect(_on_logout_pressed)


func _on_combat_pressed() -> void:
	SceneManager.change_scene("res://scenes/ui/combat.tscn", "fade")


func _on_settings_pressed() -> void:
	SceneManager.change_scene("res://scenes/ui/settings.tscn", "fade")


func _on_logout_pressed() -> void:
	AuthManager.logout()
	SceneManager.change_scene("res://scenes/ui/main_menu.tscn", "fade")
