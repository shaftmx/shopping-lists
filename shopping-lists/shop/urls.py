# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^showlist/(?P<listID>([0-9]+|all))','shop.views.list.showlist'),
    url(r'^showrecipe/(?P<recipeID>([0-9]+))','shop.views.recipe.showrecipe'),
    #url(r'^showlist/all','shop.views.list.showfulllist'),
    url(r'^changeitemstock/(?P<itemID>[0-9]+)','shop.views.item.changeitemstock'),
    url(r'^test$','shop.views.test.index'),
    url(r'^$','shop.views.index.index'),
    #url(r'^','shop.views.index', name='index'),
    #url(r'^test','shop.views.index', name='index'),
)
