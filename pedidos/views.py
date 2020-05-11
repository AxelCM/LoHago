from django.shortcuts import render
from django.core import serializers
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


from django.http import HttpResponse , HttpResponseRedirect , JsonResponse

from django.views.generic import TemplateView , DetailView
from django.urls import reverse , reverse_lazy

#for security views
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

import json
from datetime import *
from pedidos.models import Category, Type, SubMenu, Pedido, Items
from users.models import User

class Welcome(LoginRequiredMixin,TemplateView):
    template_name= "pedidos/components/welcome.html"

class IndexView(SuccessMessageMixin, LoginRequiredMixin, TemplateView):
    template_name = "pedidos/init.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self , *args, **kwargs):
        # list = self.request.session["cart"]
        # self.request.session["cart"] = []
        # print(list)
        today = date.today()
        categorys = Category.objects.all()
        session = self.request.session.session_key
        types = Type.objects.all()
        return {"categorys": categorys , "types":types , "sesion":session , "list":list , "today":today}


class DetailCategory(DetailView):
    template_name = "pedidos/menu.html"
    slug_field = 'name'
    slug_url_kwarg = 'name'
    queryset = Category.objects.all()
    context_object_name = 'menu'

    def get_context_data(self, *args , **kwargs):
        target = []
        context = super().get_context_data(**kwargs)
        category_id = self.get_object().pk
        context['types'] = Type.objects.filter(category=category_id).order_by('name')
        return context

class DetailMenu(DetailView):
    template_name = "pedidos/menu_options.html"
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    queryset = Type.objects.all()
    context_object_name = 'options'

    def get_context_data(self, *args , **kwargs):
        context = super().get_context_data(**kwargs)
        menu_id = self.get_object().pk
        context['types'] = SubMenu.objects.filter(type=menu_id).order_by('name')
        return context


def add_cart(request , cat , id_item):
    menu = cat
    id = id_item
    cart = []
    # cart = {}
    #se hace el query del elemento que se quiere agregar al carrito
    data = SubMenu.objects.get(type=menu , pk=id)
    #instancia de arreglo sessions para darle datos
    cart = request.session["cart"]
    # cart.update({'pk':data.name})

    #se agrega la primary key del menu seleccionado
    cart.append(data.pk)
    # print("El carrito es este {}".format(cart))
    # se agregar la instancia al lugar del arreglo
    request.session["cart"] = cart
    # safeCart(request)
    messages.success(request, 'Se agrego {} a tu carrito'.format(data.name))
    return HttpResponseRedirect(reverse('index'))

def safeCart(request):
    data = request.session["cart"]
    cart_dict = {}
    # cart = dict(enumerate(data))
    cart = dict(zip(range(len(data)), data))
    # print("DICCIONARIO REAL {}".format(cart))
    for key,value in cart.items():
        print(value)
        item = SubMenu.objects.get(pk=value)
        # print("MENU: {} PRECIO: Q.{}".format(item.name, item.price))
        menu = item.name
        precio = item.price
        cart_dict.update({key:precio})
    return cart_dict

def popCart(request , item):
    id = item
    data = request.session["cart"]
    data.remove(id)
    request.session["cart"] = data
    messages.success(request, "SE ELIMINO ARTICULO DE TU LISTA DE CARRITO")
    return HttpResponseRedirect(reverse('cart'))

def CreatePedido(request):
    total = 0
    user = User.objects.get(pk=request.user.pk)
    pedido = Pedido.objects.create(
    user = user
    )
    pedido.save()
    id = 0
    items = request.session["cart"]
    pedidos_user = Pedido.objects.filter(user=user).order_by('-create_at')
    last_pedido = pedidos_user[:1]
    for i in last_pedido:
        id = i.pk
    set_pedido = Pedido.objects.get(pk=id)
    for i in items:
        set_item = SubMenu.objects.get(pk=i)
        item_add = Items.objects.create(
        pedido = set_pedido,
        item= set_item
        )
        total += set_item.price
    item_add.save()
    update = Pedido.objects.filter(pk=id).update(total=total)
    request.session["cart"] = []
    messages.success(request, "TU PEDIDO SE CONFIRMO CORRECTAMENTE")
    return HttpResponseRedirect(reverse('index'))

def cleanCart(request):
    request.session["cart"] = []
    return HttpResponseRedirect(reverse('index'))


def safeCartName(request):
    data = request.session["cart"]
    cart_name = {}
    # cart = dict(enumerate(data))
    cart = dict(zip(range(len(data)), data))
    for key,value in cart.items():
        item = SubMenu.objects.get(pk=value)
        menu = item.name
        cart_name.update({key:menu})
    print("AGREGANDO EL PRECIO")
    return cart_name

def safeIdItem(request):
    data = request.session["cart"]
    cart_id = {}
    # cart = dict(enumerate(data))
    cart = dict(zip(range(len(data)), data))
    for key,value in cart.items():
        item = SubMenu.objects.get(pk=value)
        menu = item.pk
        cart_id.update({key:menu})
    print(cart_id)
    return cart_id

def totalCart(data):
    cart = data
    total = 0
    for key,value in cart.items():
        print("Q{}".format(value))
        total += value
    print(cart)
    print(total)
    return total

class CartView(TemplateView):
    template_name = 'pedidos/components/cart.html'

    def get_context_data(self , *args , **kwargs):
        # cart = self.request.session['cart']
        cart = safeCart(self.request)
        cart_name = safeCartName(self.request)
        cart_id = safeIdItem(self.request)
        total = totalCart(cart)
        print(cart)
        return {"cart":cart , "total":total , "items_cart":cart_name , "cart_id":cart_id}


class MyOrders(LoginRequiredMixin, TemplateView):
    template_name = "pedidos/my_orders.html"

    def get_context_data(self , *args , **kwargs):
        user = User.objects.get(pk=self.request.user.pk)
        my_orders = Pedido.objects.filter(user=user)
        return{"orders": my_orders}

def calculateTotal(id):
    id_pedido = id


#
# def add_cart(request , cat , id_item):
#     menu = cat
#     id = id_item
#     # search_filter = '"type_id":{0} , "pk":{1}'.format(menu, id)
#     p = SubMenu.objects.get(jsonfield__contains=search_filter)
#     list = request.session["cart"]
#     list.append(p)
#     request.session["cart"] = list
#     print(list)
#     return HttpResponseRedirect(reverse('index'))
