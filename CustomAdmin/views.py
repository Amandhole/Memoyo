from django.shortcuts import render
from django.views.decorators.cache import cache_control
from ProjectUtilities.decorators import *


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @is_authenticated
def login(request):
    return render(request, 'CustomAdmin/Htmls/login.html')


# registration form
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def registration(request):
    return render(request, 'CustomAdmin/htmls/registration.html')


def index(request):
    return render(request, 'CustomAdmin/htmls/index.html')
