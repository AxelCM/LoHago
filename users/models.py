# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_rep = models.BooleanField('Repartidor', default=False)

    def __str__(self):
        return "@{} - {} {}".format(self.username, self.first_name , self.last_name)

class Repartidor(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    active = models.BooleanField('Activo', default=False)
    busy = models.BooleanField('Libre', default=False)

    def __str__(self):
        return "{} {}".format(self.user.first_name , self.user.last_name)
