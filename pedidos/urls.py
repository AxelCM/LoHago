from django.urls import path

from pedidos.views import IndexView , DetailCategory

urlpatterns = [
    path('' , IndexView.as_view() , name='index'),
    path('<str:name>/' , DetailCategory.as_view() , name='menu')
]
