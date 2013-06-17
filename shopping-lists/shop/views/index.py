# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse

from shop.models import *

def index(request):
    #items = Item.objects.all()
    lists = ShopList.objects.all().order_by('name')
    recipes = Recipe.objects.all().order_by('name')

    #request.path
    the_title = "Index";
    t = loader.get_template('index.html')
    c = Context({
        'the_title': the_title,
        'recipes': recipes,
        'lists': lists,
        'request': request,
        
    })
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
