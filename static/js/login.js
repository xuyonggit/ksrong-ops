function login() {
	var user = $('#user').val();
	var password = $('#password').val();
	$.ajax({
		method: "post",
		url: "/user/login/",
		dateType: "json",
		data: {
			"username": user,
			"password": password
		},
		success: function (data) {
			window.open('/');
		}
	})
}