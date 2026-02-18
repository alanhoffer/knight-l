extends Node

## Estado global del juego
## Autoload: GameState

var current_character: Dictionary = {}
var inventory: Array = []
var current_map: String = ""
var in_combat: bool = false
var combat_id: String = ""

signal character_changed(character: Dictionary)
signal inventory_updated(items: Array)


func set_character(character: Dictionary) -> void:
	current_character = character
	character_changed.emit(character)


func update_inventory(items: Array) -> void:
	inventory = items
	inventory_updated.emit(items)
