from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect , JsonResponse

from django.views.generic import TemplateView , DetailView
from django.urls import reverse , reverse_lazy

#for security views
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


from pedidos.models import Category, Type, SubMenu



class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "pedidos/init.html"
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self , *args, **kwargs):
        list = self.request.session["cart"] = []
        print(list)
        categorys = Category.objects.all()
        session = self.request.session.session_key
        types = Type.objects.all()
        return {"categorys": categorys , "types":types , "sesion":session}


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
    queryset = SubMenu.objects.all()
    context_object_name = 'menu'

    def get_context_data(self, *args , **kwargs):
        target = []
        context = super().get_context_data(**kwargs)
        menu_id = self.get_object().pk
        context['types'] = SubMenu.objects.filter(type=menu_id).order_by('name')
        return context

def add_cart(request , cat , id_item):
    menu = cat
    id = id_item
    # search_filter = '"type_id":{0} , "pk":{1}'.format(menu, id)
    p = SubMenu.objects.get(jsonfield__contains=search_filter)
    list = request.session["cart"]
    list.append(p)
    request.session["cart"] = list
    print(list)
    return HttpResponseRedirect(reverse('index'))
