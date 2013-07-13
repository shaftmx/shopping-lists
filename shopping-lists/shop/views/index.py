# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse

from shop.models import *

def index(request):
    full_list = Item.objects.all().order_by('name')
    lists = ShopList.objects.all().order_by('name')
    recipes = Recipe.objects.all().order_by('name')

    #request.path
    the_title = "Index";
    t = loader.get_template('index.html')
    c = Context({
        'the_title': the_title,
        'recipes': recipes,
        'lists': lists,
        'full_list': full_list,
        'request': request,
        
    })
    return HttpResponse(t.render(c))

