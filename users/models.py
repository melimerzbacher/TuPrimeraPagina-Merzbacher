from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    bio = models.TextField(blank=True)
    link = models.URLField(blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self): return f"Perfil de {self.user.username}"