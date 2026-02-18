extends Node2D

## Pantalla de combate - Placeholder
## Sistema de combate en Sprint 3

@onready var back_button: Button = $UILayer/BackButton


func _ready() -> void:
	back_button.pressed.connect(_on_back_pressed)


func _on_back_pressed() -> void:
	SceneManager.change_scene("res://scenes/ui/home.tscn", "fade")
