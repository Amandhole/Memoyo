from django.shortcuts import render
from django.views.decorators.cache import cache_control
from ProjectUtilities.decorators import *

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def LandingPage(request):
    user = is_authenticated(request)
    if user:
        return redirect('index')
    else:
        return render(request, 'Website/htmls/landing.html')

# login form
def Login(request):
    return render(request, 'Website/Htmls/login.html')
