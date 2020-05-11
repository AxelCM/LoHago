from django.contrib import admin

# Register your models here.
from pedidos.models  import Category, Type, SubMenu , Pedido, Items


class CategoryAdmin(admin.ModelAdmin):

    list_display=['pk' , 'name']

class TypeAdmin(admin.ModelAdmin):

    list_display=['pk' , 'name']

class SubMenuAdmin(admin.ModelAdmin):

    list_display=['pk' , 'name']

class PedidoAdmin(admin.ModelAdmin):

    list_display=['pk' , 'user']

class ItemsAdmin(admin.ModelAdmin):

    list_display=['pk' , 'pedido']




admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Items, ItemsAdmin)
