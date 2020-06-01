from django.db import models

from users.models import User , Repartidor
# Create your models here.

class Category(models.Model):
    """This model contain category for purchase
    #for example Restaurantes, Compras, Ofertas
    #have a picture for easly understand
    """
    name = models.CharField('Nombre' , max_length=30)
    picture = models.ImageField(
        upload_to='pedidos/categorys',
        blank=True,
        null=True
    )

    def __str__(self):
        return '{}'.format(self.name)

class Type(models.Model):
    """This model contain Types of category model for purchase
    #for example McDonalds, Campero, Taco Bell
    #have a picture for easly identifycation a type
    """
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
    """
    status True is for orders when not have rep assigned

    """


    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    total = models.IntegerField("Total" , default=0)
    rep = models.ForeignKey(Repartidor , on_delete=models.CASCADE)
    notes = models.TextField('Notas', blank=True, null=True)
    cat = models.PositiveIntegerField('Category' , default=0 , max_length=3)
    # geo = models.CharField(max_length=100 , blank=True , null=True)

    class Meta:
        permissions = [
            ("view_rep", "Can view functions related deliveriMan team"),
            ]

    def __str__(self):
        return "{}".format(self.pk)

class Items(models.Model):
    """model for purchase confirmation
    this object is instanced in fuction "create_pedido"
    """
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    item = models.ForeignKey(SubMenu , on_delete=models.CASCADE)


class Cart(models.Model):
    """now this model is not used
    #First we would be used for purchase but django sessions
    managed to complete to fuction
    """
    active = models.BooleanField('Activo',default=True)
    create_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class ItemCart(models.Model):
    """now this model is not used
    #First we would be used for purchase but django sessions
    managed to complete to fuction
    """
    create_at= models.DateTimeField(auto_now=True)
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE)
    item = models.ForeignKey(SubMenu , on_delete=models.CASCADE)
