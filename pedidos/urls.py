from django.urls import path

from pedidos.views import (IndexView , DetailCategory , DetailMenu , add_cart,
CartView, popCart , cleanCart , CreatePedido , MyOrders , Welcome, Deliveryman,
PendindDelivery ,  SendOrder, MyDeliveris
)

urlpatterns = [
    path('' , IndexView.as_view() , name='index'),
    # path('delivermans/' , Deliveryman.as_view() , name='view_deliverman'),
    path('delivermans/' , MyDeliveris.as_view() , name='view_deliverman'),
    path('welcome' , Welcome.as_view() , name='welcome'),
    path('view/orders' , PendindDelivery.as_view() , name='view_orders'),
    path('create/order' , SendOrder.as_view() , name='create_order'),
    path('my-orders/' , MyOrders.as_view() , name='my_orders'),
    path('remove/<int:item>/' , popCart , name='pop_cart'),
    path('<str:name>/' , DetailCategory.as_view() , name='menu'),
    path('<str:type>/<int:pk>/' , DetailMenu.as_view() , name='menu_options'),
    path('my/cart/' , CartView.as_view() , name='cart'),
    path('add/<str:cat>/<int:id_item>/' , add_cart , name='add_to_cart'),
    path('clean/cart' , cleanCart , name='clean_cart'),
    path('generate/pedido' , CreatePedido , name='create_pedido'),
]
