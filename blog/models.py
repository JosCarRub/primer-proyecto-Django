from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=60)
    cuerpo = models.CharField(max_length=5000)

    def __str__(self):
        return self.titulo
    
