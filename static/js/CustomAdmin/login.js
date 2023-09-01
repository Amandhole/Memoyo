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
                    console.log('call ajax...')
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
    $("#" + id).css("border-color", "#ced4da");
    if ('email' == id) {        
        $("#"+id).css("border-color", emailPattern.test($('#'+id).val()) ? "#ced4da" : "#EE4B2B");
    }
}

window.Login = async function (email, password) {
    var useremail = $('#' + email).val()
    var userpassword = $('#'+password).val()
    if (!useremail) {
        $("#"+email).focus();
        $("#"+email).css("border-color", "#EE4B2B");
        showToastMsg('Error',"Please Enter Email",'error')
    }

    else if (!emailPattern.test(useremail)) {
        $("#"+email).css("border-color", "#EE4B2B");
        showToastMsg('ERROR','Enter Valid Email Address', 'error')
    }
       
    else if (!userpassword) {
        $("#"+password).focus();
        $("#"+password).css("border-color", "#EE4B2B");
        showToastMsg('Error',"Please Enter Password",'error')        
    }

    else {
        var data = {
            'email': JSON.stringify(useremail),
            'password':JSON.stringify(userpassword)
        }
        var response = await callAjax('/LoginAjax/', data)
        if (response.status == 1) {
            location.href="/index/"
        }
        else {
            var preference = await sweetAlertMsg(response['title'],response['msg'],'warning')
        }
    }
}

$('.form-control').keypress(function(event) {
    if (event.which === 13) {
        $('#loginbtn').click();
    }
});

