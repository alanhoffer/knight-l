extends Node

## Gestiona la navegación entre escenas
## Autoload: SceneManager

signal scene_changed(scene_name: String)

var current_scene: String = ""


func change_scene(scene_path: String, transition: String = "none") -> void:
	match transition:
		"fade":
			await _transition_fade(scene_path)
		"slide":
			_transition_slide(scene_path)
		_:
			get_tree().change_scene_to_file(scene_path)
			current_scene = scene_path
			scene_changed.emit(scene_path)


func _transition_fade(scene_path: String) -> void:
	var fade = ColorRect.new()
	fade.name = "TransitionFade"
	fade.set_anchors_preset(Control.PRESET_FULL_RECT)
	fade.color = Color.BLACK
	fade.modulate.a = 0.0
	get_tree().root.add_child(fade)

	var tween = create_tween()
	tween.tween_property(fade, "modulate:a", 1.0, 0.25)
	await tween.finished

	get_tree().change_scene_to_file(scene_path)
	current_scene = scene_path
	scene_changed.emit(scene_path)

	tween = create_tween()
	tween.tween_property(fade, "modulate:a", 0.0, 0.25)
	await tween.finished
	fade.queue_free()


func _transition_slide(scene_path: String) -> void:
	get_tree().change_scene_to_file(scene_path)
	current_scene = scene_path
	scene_changed.emit(scene_path)
