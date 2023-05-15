import { log, callAjax, sweetAlertMsg } from '../common.js';

///// Logout user
window.logout = async function()
{
	var preference = await sweetAlertMsg('LOGOUT', 'Do you want to logout from your account ?', 'question', 'cancel', 'Yes', 'No');
	if (preference)
	{
		var response = await callAjax('/logout_aj/', {})
		if (response.status == 1){location.href = '/';}else{await sweetAlertMsg('Error', response.msg, 'error');}
	}
}