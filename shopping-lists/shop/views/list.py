# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse

from shop.models import *

def showlist(request,listID):
    if listID == "all":
        myitems = Item.objects.all().order_by('cathegory','name')
        mylist = "Full list"
    else:
        mylist = ShopList.objects.get(id=listID)
        myitems = mylist.items.all().order_by('cathegory','name')

    items={}
    for item in myitems:
        if not item.cathegory in items:
            items[item.cathegory]=[]
        items[item.cathegory].append(item)

    #request.path
    the_title = "Liste : %s" % mylist;
    t = loader.get_template('listshow.html')
    c = Context({
        'the_title': the_title,
        'items': items,
        'request': request,
        
    })
    return HttpResponse(t.render(c))

#def showfulllist(request):
#    #myitems = Item.objects.all().order_by('cathegory','name')
#    myitems = Item.objects.all().order_by('cathegory','name')
#    #myitems = Item.objects.all().order_by('name')
#
#    items={}
#    for item in myitems:
#        if not item.cathegory in items:
#            items[item.cathegory]=[]
#        items[item.cathegory].append(item)
#
#    #request.path
#    the_title = "Full list"
#    t = loader.get_template('listfullshow.html')
#    c = Context({
#        'the_title': the_title,
#        'items': items,
#        'request': request,
#        
#    })
#    return HttpResponse(t.render(c))



#class ShopList(models.Model):
#    name = models.CharField(max_length=200)
#    idems = models.ManyToManyField('Item')
#
#    def __unicode__(self):
#        return '%s' % (self.name)
#
#class Item(models.Model):
#    name = models.CharField(max_length=200)
#    desc = models.CharField(max_length=200,default='',blank=True)
#    outOfStock = models.BooleanField()
#    cathegory = models.ForeignKey('Category')
#
#    def __unicode__(self):
#        return '%s' % (self.name)
#
#class Category(models.Model):
#    name = models.CharField(max_length=200)
#    desc = models.CharField(max_length=200,default='',blank=True)
#
#    def __unicode__(self):
#        return '%s' % (self.name)
#
#class Recipe(models.Model):
#    name = models.CharField(max_length=200)
#    desc = models.CharField(max_length=200,default='',blank=True)
#    idems = models.ManyToManyField('Item')
