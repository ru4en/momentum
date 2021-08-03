from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def login(response):
    return render(response, "register/login.html", 
    {
        "title": "Login"
        }
        )

def logout(response):
    return render(response, "register/logout.html", 
    {
        "title": "Logout"
        }
        )

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()

    return render(response, "register/register.html", 
    {
        "title": "Register",
        "form": form
        }
        )
    