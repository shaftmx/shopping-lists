# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse

from shop.models import *

def changeitemstock(request,itemID):
    myItem = Item.objects.get(id=itemID)

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
