from django.urls import path

from pedidos.views import IndexView , DetailCategory , DetailMenu , add_cart

urlpatterns = [
    path('' , IndexView.as_view() , name='index'),
    path('<str:name>/' , DetailCategory.as_view() , name='menu'),
    path('<str:type>/<int:pk>/' , DetailMenu.as_view() , name='menu_options'),
    path('add/<str:cat>/<int:id_item>/' , add_cart , name='add_to_cart'),
]
