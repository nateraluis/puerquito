from django.shortcuts import render


def index(request):
    return render(request, 'gastos/index.html')


def register(request):
    return render(request, 'gastos/registro.html')


def panel_control(request):
    return render(request, 'gastos/panel.html')


def ingreso(request):
    return render(request, 'gastos/ingreso.html')


def egreso(request):
    return render(request, 'gastos/egreso.html')
# Create your views here.
