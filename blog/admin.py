from django.contrib import admin
from .models import Chef, Categoria, Receta

# Register your models here.

admin.site.register(Chef)
admin.site.register(Categoria)
admin.site.register(Receta)
