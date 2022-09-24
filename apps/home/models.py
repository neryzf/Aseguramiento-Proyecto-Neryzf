from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class producto(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    imagen = models.CharField(max_length=1000)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.nombre)

class Usuario(models.Model):
    perfil = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.perfil.username

@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(perfil=instance)

@receiver(post_save, sender=User)
def guardar_usuario(sender, instance, created, **kwargs):
    instance.usuario.save()