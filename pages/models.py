from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=200)
    body = RichTextField()                      # texto enriquecido
    image = models.ImageField(upload_to="pages/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self): return self.title
    