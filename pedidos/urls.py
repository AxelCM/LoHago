from django.urls import path

from pedidos.views import (IndexView , DetailCategory , DetailMenu , add_cart,
CartView, popCart , cleanCart , CreatePedido , MyOrders , Welcome
)

urlpatterns = [
    path('' , IndexView.as_view() , name='index'),
    path('welcome' , Welcome.as_view() , name='welcome'),
    path('my-orders/' , MyOrders.as_view() , name='my_orders'),
    path('remove/<int:item>/' , popCart , name='pop_cart'),
    path('<str:name>/' , DetailCategory.as_view() , name='menu'),
    path('<str:type>/<int:pk>/' , DetailMenu.as_view() , name='menu_options'),
    path('my/cart/' , CartView.as_view() , name='cart'),
    path('add/<str:cat>/<int:id_item>/' , add_cart , name='add_to_cart'),
    path('clean/cart' , cleanCart , name='clean_cart'),
    path('generate/pedido' , CreatePedido , name='create_pedido'),
]
