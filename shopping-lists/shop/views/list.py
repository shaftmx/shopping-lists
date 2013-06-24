# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from shop.models import *

def showlist(request, listID, clean=None):
    if listID == "all":
        myitems = Item.objects.all().order_by('cathegory','name')
        mylist = "Full list"
    else:
        #mylist = ShopList.objects.get(id=listID)
        mylist = get_object_or_404(ShopList, id=listID)
        myitems = mylist.items.all().order_by('cathegory','name')

    items={}
    for item in myitems:
        if not item.outOfStock and clean is not None:
            continue
        if not item.cathegory in items:
            items[item.cathegory]=[]
        items[item.cathegory].append(item)

    #request.path
    the_title = "Liste : %s" % mylist;
    if clean is None:
        t = loader.get_template('listshow.html')
    else:
        t = loader.get_template('listshowclean.html')
    c = Context({
        'the_title': the_title,
        'items': items,
        'request': request,
        
    })
    return HttpResponse(t.render(c))

