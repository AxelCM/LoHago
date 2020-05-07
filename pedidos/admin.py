from django.contrib import admin

# Register your models here.
from pedidos.models  import Category, Type, SubMenu


class CategoryAdmin(admin.ModelAdmin):

    list_display=['pk' , 'name']

class TypeAdmin(admin.ModelAdmin):

    list_display=['pk' , 'name']

class SubMenuAdmin(admin.ModelAdmin):

    list_display=['pk' , 'name']




admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(SubMenu, SubMenuAdmin)