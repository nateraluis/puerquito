from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registro/', views.register),
    path('panel/', views.panel_control),
    path('ingreso/', views.ingreso),
    path('egreso/', views.egreso)
]
