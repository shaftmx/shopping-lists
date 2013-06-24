# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from shop.models import *

def showrecipe(request,recipeID):
    #myrecipe = Recipe.objects.get(id=recipeID)
    myrecipe = get_object_or_404(Recipe, id=recipeID)
    myitems = myrecipe.items.all().order_by('cathegory','name')

    items={}
    for item in myitems:
        if not item.cathegory in items:
            items[item.cathegory]=[]
        items[item.cathegory].append(item)

    #request.path
    the_title = "Recette : %s" % myrecipe
    t = loader.get_template('recipeshow.html')
    c = Context({
        'the_title': the_title,
        'items': items,
        'request': request,
        
    })
    return HttpResponse(t.render(c))

