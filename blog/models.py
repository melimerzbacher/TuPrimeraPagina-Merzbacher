from django.db import models

# Create your models here.

class Chef(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    especialidad = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
        nombre = models.CharField(max_length=50, unique = True)
        slug = models.SlugField(unique=True)
        
        def __str__(self):
            return self.nombre
    
class Receta(models.Model):
        titulo = models.CharField(max_length=150)
        slug = models.SlugField(unique=True)
        ingredientes = models.TextField()
        procedimiento = models.TextField()
   
        chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name="recetas")
        categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name="recetas")

        def __str__(self):
            return self.titulo