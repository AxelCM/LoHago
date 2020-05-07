from django.shortcuts import render

from django.views.generic import TemplateView , DetailView
# Create your views here.

from pedidos.models import Category, Type

class IndexView(TemplateView):
    template_name = "pedidos/init.html"

    def get_context_data(self , *args, **kwargs):
        categorys = Category.objects.all()
        types = Type.objects.all()
        return {"categorys": categorys , "types":types}

# def get_marks(request, *args , **kwargs):
#     if request.method == 'POST':
#         categ = request.POST['cat']
#         enc = "<label>MARK</label> <select id='mark' name='mark' class='form-control'> "
#         cierre = "</select>"
#         components= ["<label>MARK</label> <select id='mark' name='mark'> "]
#         mark = Mark.objects.filter(category=categ).values('name' ,'id_mark' )  # or simply .values() to get all fields
#         mark_list = list(mark)  # important: convert the QuerySet to a list object
#         c=[]
#         overall = ''
#         #en este for se ingresan los valores del query mas las etiquetas html para insercsion
#         for val in mark:
#             c.append("<option value='{}'>{}</option>".format(val['id_mark'],val['name']))
#         #en este for se agregan todos los valores en un solo string y se suman para hacer una sola cadena
#         for i in c:
#             overall += "{}".format(i)
#         final ="{}{}{}".format(enc , overall , cierre)
#         return HttpResponse(final)

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
