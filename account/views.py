from django.shortcuts import render
from django.shortcuts import (
    redirect,
    HttpResponseRedirect,
)
from django.contrib.auth.decorators import login_required

# Create your views here.


from .forms import NewUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def SignUp(request):
    form = NewUserCreationForm()
    if request.method == "POST":
        form = NewUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, "account/signup.html", {"form": form})


def SignIn(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")

    return render(request, "account/login.html", {"form": form})


@login_required
def UserProfile(request):
    return render(request, "account/profile.html")


@login_required
def logout_user(request):
    logout(request)
    return redirect("/")
