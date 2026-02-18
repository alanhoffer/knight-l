extends Node

## Gestiona autenticación y sesión del usuario
## Autoload: AuthManager

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
		APIClient.set_auth_token(response["access_token"])
		var user = await get_current_user()
		if not user.is_empty():
			current_user = user
			is_logged_in = true
			login_success.emit(current_user)
			return true

	var err_msg: String = str(response.get("detail", "Invalid credentials"))
	login_failed.emit(err_msg)
	return false


func register(username: String, email: String, password: String) -> bool:
	var response = await APIClient.request("/auth/register", "POST", {
		"username": username,
		"email": email,
		"password": password
	})

	if response.has("user_id"):
		# Registro ok, hacer login
		return await login(username, password)

	login_failed.emit(str(response.get("detail", "Registration failed")))
	return false


func logout() -> void:
	APIClient.set_auth_token("")
	current_user = {}
	is_logged_in = false
	logout_complete.emit()


func get_current_user() -> Dictionary:
	return await APIClient.request("/auth/me")
