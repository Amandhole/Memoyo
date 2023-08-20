from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Website/htmls/index.html')

# registration form
def registration(request):
    return render(request, 'Website/htmls/registration.html')

# login form
def login(request):
    return render(request, 'Website/htmls/login.html')