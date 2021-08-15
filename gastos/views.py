from django.shortcuts import render, redirect
from .forms import CreateUserForm, CreateExpenseForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "gastos/index.html")


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("panel")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("panel")
        else:
            messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, "gastos/login.html", context)


def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                print(user)
                messages.success(request, "Account created for " + user)
                return render(request, "gastos/registro.html")
    context = {"form": form}
    return render(request, "gastos/registro.html", context)


@login_required(login_url="login")
def panel_control(request):
    return render(request, "gastos/panel.html")


@login_required(login_url="login")
def ingreso(request):
    return render(request, "gastos/ingreso.html")


@login_required(login_url="login")
def egreso(request):
    form = CreateExpenseForm()
    if request.method == "POST":
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            your_object = form.save(commit=False)
            your_object.user = request.user
            your_object.save()
    context = {"form": form}
    return render(request, "gastos/egreso.html", context)


@login_required(login_url="login")
def resumen(request):
    return render(request, "gastos/resumen.html")


def logoutUser(request):
    logout(request)
    return redirect("login")
