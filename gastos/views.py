from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages


def index(request):
    return render(request, 'gastos/index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                print(user)
                messages.success(request, 'Account created for '+user)
                return render(request, 'gastos/registro.html')
    context = {'form': form}
    return render(request, 'gastos/registro.html', context)


def panel_control(request):
    return render(request, 'gastos/panel.html')


def ingreso(request):
    return render(request, 'gastos/ingreso.html')


def egreso(request):
    return render(request, 'gastos/egreso.html')
# Create your views here.
