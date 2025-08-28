from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Receta
from .forms import ChefForm, CategoriaForm, RecetaForm, SearchForm

# Create your views here.
def home(request):
    form = SearchForm(request.GET or None)
    recetas = Receta.objects.all()
    if form.is_valid() and form.cleaned_data.get("q"):
     q = form.cleaned_data["q"]
     recetas = recetas.filter(Q(titulo__icontains=q) | Q(ingredientes__icontains=q))
    return render(request, "blog/inicio.html", {"form": form, "recetas": recetas})

def receta_list(request):
    recetas = Receta.objects.all()
    return render(request, "blog/receta_list.html", {"recetas": recetas})

def receta_create(request):
    form = RecetaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("receta_list")
    return render(request, "blog/receta_form.html", {"form": form})

def chef_create(request):
    form = ChefForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "blog/chef_form.html", {"form": form})

def categoria_create(request):
    form = CategoriaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "blog/categoria_form.html", {"form": form})
