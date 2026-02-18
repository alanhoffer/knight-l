extends Control

## Pantalla de ajustes - Placeholder
## Opciones de juego, audio, etc. en sprints posteriores

@onready var back_button: Button = $VBox/BackButton


func _ready() -> void:
	back_button.pressed.connect(_on_back_pressed)


func _on_back_pressed() -> void:
	SceneManager.change_scene("res://scenes/ui/home.tscn", "fade")
