from django.db import models

# Create your models here.

class Palavra(models.Model):
    nome = models.CharField(max_length=200)
    sinal = models.ImageField(upload_to='media', null=True)

    def __str__(self):
        return self.nome
