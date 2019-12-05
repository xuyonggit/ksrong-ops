$(function () { $(".popover-options a").popover({html : true });});
function Passwd_make() {
	var param = $("#make-passwd").serializeArray();
	// var jsonObj={};
	// $(param).each(function () {
	// 	jsonObj[this.name]=this.value;
	// });
	$.ajax({
		url: "/tools/make_passwd/",
		method: "post",
		data: param,
		dateType: "json",
		success: function (data) {
			var json = eval("("+data+")");
			var result = json.passwd;
			$("#passwd_result").val(result);
		}
	})
}

// 快速选择密码
function quick_choice_passwd(type) {
	if (type==1){       // type = 1 服务器密码
		$("#passwd_num").val(24);
		$("#passwd_level3").prop("checked", true);
	} else if (type==2){    // type = 2 数据库密码
		$("#passwd_num").val(18);
		$("#passwd_level3").prop("checked", true);
	} else if (type==3){    // type = 3 普通密码
		$("#passwd_num").val(16);
		$("#passwd_level2").prop("checked", true);
	}
}

$(function () {
	$(".pull-right").mouseover(function () {
		$(this).addClass();
	})
});

function Finance_check() {
	var param = $("#finance_check").serializeArray();
	$.ajax({
		url: "/tools/finance_check/",
		method: "post",
		data: param,
		dateType: "json",
		success: function (data) {
			var json = eval("("+data+")");
			var r_state = json.state;
			if (r_state == 'success'){
				$("#finance_result").val(json.mon);
			} else {
				swal("ERROR", json.msg, "error");
			}
		}
	})
}