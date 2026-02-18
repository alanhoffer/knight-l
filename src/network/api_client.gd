extends Node

## Cliente HTTP para comunicación con el backend
## Autoload: APIClient

var base_url: String = ApiConfig.API_BASE_URL
var auth_token: String = ""

signal request_completed(response: Dictionary)
signal request_failed(error: String)


func set_auth_token(token: String) -> void:
	auth_token = token


func get_headers() -> PackedStringArray:
	var headers = PackedStringArray([
		"Content-Type: application/json",
		"Accept: application/json"
	])
	if auth_token != "":
		headers.append("Authorization: Bearer " + auth_token)
	return headers


func request(
	endpoint: String,
	method: String = "GET",
	body: Dictionary = {}
) -> Dictionary:
	var url = base_url + endpoint
	var http_request = HTTPRequest.new()
	add_child(http_request)

	var headers = get_headers()
	var error_code: Error

	match method:
		"GET":
			error_code = http_request.request(url, headers)
		"POST":
			error_code = http_request.request(url, headers, HTTPClient.METHOD_POST, JSON.stringify(body))
		"PUT":
			error_code = http_request.request(url, headers, HTTPClient.METHOD_PUT, JSON.stringify(body))
		"DELETE":
			error_code = http_request.request(url, headers, HTTPClient.METHOD_DELETE)
		_:
			error_code = http_request.request(url, headers)

	if error_code != OK:
		request_failed.emit("Request failed: " + str(error_code))
		http_request.queue_free()
		return {}

	var result = await http_request.request_completed
	http_request.queue_free()

	var _req_result: int = result[0]
	var response_code: int = result[1]
	var _headers: PackedStringArray = result[2]
	var response_body: PackedByteArray = result[3]

	if response_code >= 200 and response_code < 300:
		if response_body.size() > 0:
			var json = JSON.new()
			var parse_err = json.parse(response_body.get_string_from_utf8())
			if parse_err == OK:
				request_completed.emit(json.get_data())
				return json.get_data()
			else:
				request_failed.emit("Invalid JSON response")
				return {}
		else:
			return {"success": true}
	else:
		var err_msg = "HTTP " + str(response_code)
		var err_data := {}
		if response_body.size() > 0:
			var json = JSON.new()
			if json.parse(response_body.get_string_from_utf8()) == OK:
				err_data = json.get_data()
				if err_data.get("detail"):
					err_msg = str(err_data["detail"])
		request_failed.emit(err_msg)
		return {"detail": err_msg}
