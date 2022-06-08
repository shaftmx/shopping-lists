from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import *

def index(request):
    full_list = Item.objects.all().order_by('name')
    lists = ShopList.objects.all().order_by('name')
    recipes = Recipe.objects.all().order_by('name')

    the_title = "Index";
    unknow_cat = RecipeCategory.objects.create(name="unknown")
    recipes_by_cat = {}
    for recipe in recipes:
        if recipe.category is None:
            recipe.category = unknow_cat

        if recipe.category not in recipes_by_cat.keys():
            recipes_by_cat[recipe.category] = []
        recipes_by_cat[recipe.category].append(recipe)

    context = {
        'the_title': the_title,
        'recipes': recipes,
        'recipes_by_cat': recipes_by_cat,
        'lists': lists,
        'full_list': full_list,
        'request': request,

    }
    return render(request, 'index.html', context)

def changeitemstock(request,itemID):
    #myItem = Item.objects.get(id=itemID)
    myItem = get_object_or_404(Item, id=itemID)

    myItem.outOfStock = not myItem.outOfStock
    myItem.save()

    result = myItem.outOfStock

    t = loader.get_template('raw.html')
    context = {
        'request': request,
        'result': result,
    }
    return render(request, 'raw.html', context)



def showlist(request, listID, clean=None):
    if listID == "all":
        myitems = Item.objects.all().order_by('category','name')
        mylist = "Full list"
    else:
        #mylist = ShopList.objects.get(id=listID)
        mylist = get_object_or_404(ShopList, id=listID)
        myitems = mylist.items.all().order_by('category','name')
    items={}
    for item in myitems:
        if not item.outOfStock and clean is not None:
            continue
        if not item.category in items:
            items[item.category]=[]
        items[item.category].append(item)
    #request.path
    the_title = "Liste : %s" % mylist;
    context = {
        'the_title': the_title,
        'items': items,
        'request': request,
    }
    if clean is None:
        return render(request, 'listshow.html', context)
    else:
        return render(request, 'listshowclean.html', context)


def showrecipe(request,recipeID):
    #myrecipe = Recipe.objects.get(id=recipeID)
    myrecipe = get_object_or_404(Recipe, id=recipeID)
    myitems = myrecipe.items.all().order_by('category','name')

    items={}
    for item in myitems:
        if not item.category in items:
            items[item.category]=[]
        items[item.category].append(item)

    the_title = "Recette : %s" % myrecipe.name
    context = {
        'the_title': the_title,
        'recipe': myrecipe,
        'items': items,
        'request': request,
        'description_html': myrecipe.html_desc(),

    }
    return render(request, 'recipeshow.html', context)
