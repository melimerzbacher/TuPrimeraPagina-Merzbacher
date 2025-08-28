from django import forms
from .models import Chef, Categoria, Receta

class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = ["nombre", "email", "especialidad"]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre", "slug"]

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ["titulo", "slug", "ingredientes", "procedimiento", "chef", "categoria"]

class SearchForm(forms.Form):
    q = forms.CharField(label="Buscar receta", required=False)
    