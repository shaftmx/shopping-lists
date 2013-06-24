# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from shop.models import *

def changeitemstock(request,itemID):
    #myItem = Item.objects.get(id=itemID)
    myItem = get_object_or_404(Item, id=itemID)

    myItem.outOfStock = not myItem.outOfStock
    myItem.save()

    result = myItem.outOfStock

    ##request.path
    #the_title = "Liste : %s" % mylist;
    t = loader.get_template('raw.html')
    #t = loader.get_template('listshow.html')
    c = Context({
        'request': request,
        'result': result,
        
    })
    #return HttpResponse(t.render(c))
    return HttpResponse(t.render(c))


