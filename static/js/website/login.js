import { log, emailValidator, callAjax, fieldsValidator, removeError, sweetAlertMsg } from '../common.js';

window.removeError = removeError;

window.Login = async function(_this, email, password)
{
	var email_val = await emailValidator(email);
	if (email_val)
	{
		var fields = await fieldsValidator([password]);
		if (fields)
		{
			fields[email] = email_val;
			
			var response = await callAjax('/login_aj/', fields, _this, 'Logging In...', 'Log In');

			if (response.status == 1)
			{
				location.href = response.redirect;
			}
			else
			{
				await sweetAlertMsg('Error', response.msg, 'error');
			}
		}
	}
}

$('#email').bind('keypress', function(e) {
	if(e.keyCode==13){
		$('#login_btn').trigger('click');
	}
});
$('#password').bind('keypress', function(e) {
	if(e.keyCode==13){
		$('#login_btn').trigger('click');
	}
});