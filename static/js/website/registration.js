!function()
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