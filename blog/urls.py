from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recetas/", views.receta_list, name="receta_list"),
    path("recetas/nueva/", views.receta_create, name="receta_create"),
    path("chefs/nuevo/", views.chef_create, name="chef_create"),
    path("categorias/nueva/", views.categoria_create, name="categoria_create"),
]