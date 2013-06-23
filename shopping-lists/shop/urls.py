# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('shop.views',
    url(r'^showlist/(?P<listID>([0-9]+|all))/(?P<clean>[a-z]+)?',
        'list.showlist',
        name='showlist'),
    url(r'^showrecipe/(?P<recipeID>([0-9]+))',
        'recipe.showrecipe',
        name='showrecipe'),
    #url(r'^showlist/all','shop.views.list.showfulllist'),
    url(r'^changeitemstock/(?P<itemID>[0-9]+)',
        'item.changeitemstock',
        name='changeitemstock'),
    url(r'^test$','test.index'),
    url(r'^$','index.index'),
    #url(r'^','shop.views.index', name='index'),
    #url(r'^test','shop.views.index', name='index'),
)
