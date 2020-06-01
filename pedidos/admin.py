from django.contrib import admin

# Register your models here.
from users.models import User, Repartidor
from pedidos.models  import Category, Type, SubMenu , Pedido, Items

class UserData(admin.TabularInline):
    model = User
    extra=0
    min_num = 1
    max_num =1

class DetailData(admin.TabularInline):
    model = Items
    extra = 0
    min_num = 1
    max_num = 5


class CategoryAdmin(admin.ModelAdmin):

    list_display=['pk' , 'name']

class TypeAdmin(admin.ModelAdmin):

    list_display=['pk' , 'name']

class SubMenuAdmin(admin.ModelAdmin):

    list_display=['pk' , 'name']

class PedidoAdmin(admin.ModelAdmin):
    inlines = [DetailData]
    list_display=['pk' , 'user']

class ItemsAdmin(admin.ModelAdmin):
    list_display=['pk' , 'pedido']

class DeliverymanAdmin(admin.ModelAdmin):
    list_display = ["pk" , "user"]
    autocomplete_fields = ['user']





admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Repartidor , DeliverymanAdmin)
