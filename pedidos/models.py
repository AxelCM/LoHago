from django.db import models

from users.models import User , Repartidor
# Create your models here.


class Category(models.Model):
    name = models.CharField('Nombre' , max_length=30)
    picture = models.ImageField(
        upload_to='pedidos/categorys',
        blank=True,
        null=True
    )

    def __str__(self):
        return '{}'.format(self.name)

class Type(models.Model):
    name = models.CharField('Nombre' , max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(
        upload_to='pedidos/types',
        blank=True,
        null=True
    )

    def __str__(self):
        return '{}'.format(self.name)


class SubMenu(models.Model):
    name = models.CharField('Nombre' , max_length=30)
    type = models.ForeignKey(Type , on_delete=models.CASCADE)
    picture = models.ImageField(
        upload_to='pedidos/submenu',
        blank=True,
        null=True
    )
    price = models.IntegerField('Precio' , default=0)
    description = models.TextField('Descripcion' , blank=True , null=True)

    def __str__(self):
        return '{}{}'.format(self.name , self.price)

class Pedido(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(Type , on_delete=models.CASCADE)
    afectados = models.IntegerField('Personas Afectadas' , blank=True , null=True)
    rep = models.ForeignKey(Repartidor, on_delete=models.CASCADE)
    # geo = models.CharField(max_length=100 , blank=True , null=True)

class Cart(models.Model):
    active = models.BooleanField('Activo',default=True)
    create_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class ItemCart(models.Model):
    create_at= models.DateTimeField(auto_now=True)
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE)
    item = models.ForeignKey(SubMenu , on_delete=models.CASCADE)
