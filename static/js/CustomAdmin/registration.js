import { log, callAjax, sweetAlertMsg ,showToastMsg} from '../common.js';

!function ()
{
    "use strict";
    window.addEventListener("load",function()
    {
        var t = document.getElementsByClassName("needs-validation");
        Array.prototype.filter.call(t, function(e)
        {
            e.addEventListener("submit", function(t)
            {
                t.preventDefault();
                1===e.checkValidity() && (t.stopPropagation()), e.classList.add("was-validated");
                if (e.checkValidity())
                {
                    console.log('call ajax here')
                }
            },!1)
        })
    },!1)
}();

window.ShowPassword = async function (id,iconid) {
    var type = $("#"+id).attr("type");
    if (type == 'password') {        
        $("#"+id).attr("type",'text');
        $("#"+iconid).removeClass("fa fa-eye");
        $("#"+iconid).addClass("fa fa-eye-slash");
    }
    else {
        $("#"+id).attr("type",'password');
        $("#"+iconid).removeClass("fa fa-eye-slash");
        $("#"+iconid).addClass("fa fa-eye");

    }
}

var emailPattern = /^[\w\.-]+@[\w\.-]+\.\w+$/;
window.RemoveError = async function (id) {
    $("#"+id).css("border-color", "#ced4da");
    if ('useremail' == id) {        
        $("#"+id).css("border-color", emailPattern.test($('#'+id).val()) ? "#ced4da" : "#EE4B2B");
    }
}

// call function registration
window.Registration = async function (name, useremail, userpassword, confirmpassword, _this) {
    
    var user_name= $('#'+name).val()
    var user_email = $('#'+useremail).val() 
    var password = $('#'+userpassword).val() 
    var confirm_password = $('#' + confirmpassword).val()
    if (!user_name) {
        $("#"+name).focus();
        $("#"+name).css("border-color", "#EE4B2B");
        showToastMsg('Error', "Please Enter Name", 'error')
    }

    else if (!user_email) {
        $("#"+useremail).focus();
        $("#"+useremail).css("border-color", "#EE4B2B");
        showToastMsg('Error',"Please Enter Email",'error')
    }
        
    else if (!emailPattern.test(user_email)) {
        showToastMsg('ERROR','Enter Valid Email Address', 'error')
    }
        
    else if (!password) {
        $("#"+userpassword).focus();
        $("#" + userpassword).css("border-color", "#EE4B2B");
        showToastMsg('Error',"Please Enter Password",'error')        
    }
    else if (password.length < 8) {
        $("#"+userpassword).focus();
        $("#" + userpassword).css("border-color", "#EE4B2B");
        showToastMsg('Error',"Please enter a password with at least 8 characters.",'error')
        
    }
    else if (!confirm_password) {
        $("#"+confirmpassword).focus();
        $("#"+confirmpassword).css("border-color", "#EE4B2B");
        showToastMsg('Error',"Please Enter Confirm Password",'error')
    }

    else if (password!=confirm_password) {
        $("#"+confirmpassword).focus();
        $("#"+confirmpassword).css("border-color", "#EE4B2B");
        showToastMsg('Error',"Please make sure the passwords you entered match.",'error')
    }

    else {
        var data = {
            'name': JSON.stringify(user_name),
            'email': JSON.stringify(user_email),
            'password':JSON.stringify(password)
        }
        var response = await callAjax('/Registration_Ajax/', data, _this, 'Processing', 'Done')
        if (response.status == 1) {
            var preference = await sweetAlertMsg(response['title'], response['msg'], 'success')
            if (preference) {
                var response = await callAjax('/LoginAjax/', data)
                if (response.status == 1) {
                    location.href="/"
                }
                else {
                    sweetAlertMsg('Warning','Something Went Wrong','error')
                }
            }
        }
        else {
            var preference = await sweetAlertMsg(response['title'],response['msg'],'error')
        }
    }
    

}



$('.form-control').keypress(function(event) {
    if (event.which === 13) {
        $('#registrationbtn').click();
    }
});