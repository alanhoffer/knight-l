extends Control

## Pantalla principal - Login / Registro
## Conecta con AuthManager y cambia a Home al autenticarse

@onready var username_input: LineEdit = $VBox/LoginPanel/VBoxLogin/UsernameInput
@onready var password_input: LineEdit = $VBox/LoginPanel/VBoxLogin/PasswordInput
@onready var login_button: Button = $VBox/LoginPanel/VBoxLogin/LoginButton
@onready var register_button: Button = $VBox/LoginPanel/VBoxLogin/RegisterButton
@onready var error_label: Label = $VBox/ErrorLabel


func _ready() -> void:
	login_button.pressed.connect(_on_login_pressed)
	register_button.pressed.connect(_on_register_pressed)
	AuthManager.login_success.connect(_on_login_success)
	AuthManager.login_failed.connect(_on_login_failed)


func _on_login_pressed() -> void:
	error_label.text = ""
	var username := username_input.text.strip_edges()
	var password := password_input.text

	if username.is_empty() or password.is_empty():
		error_label.text = "Usuario y contraseña requeridos"
		return

	login_button.disabled = true
	var ok := await AuthManager.login(username, password)
	login_button.disabled = false

	if ok:
		SceneManager.change_scene("res://scenes/ui/home.tscn", "fade")


func _on_register_pressed() -> void:
	# Por ahora va a la misma pantalla - la UI de registro se añade en la tarea siguiente
	error_label.text = "Ir a pantalla de registro (próximamente)"


func _on_login_success(_user_data: Dictionary) -> void:
	SceneManager.change_scene("res://scenes/ui/home.tscn", "fade")


func _on_login_failed(error: String) -> void:
	error_label.text = error
