from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registro/", views.register, name="registro"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("panel/", views.panel_control, name="panel"),
    path("ingreso/", views.ingreso, name="ingreso"),
    path("egreso/", views.egreso, name="egreso"),
    path("resumen/", views.resumen, name="resumen"),
]
