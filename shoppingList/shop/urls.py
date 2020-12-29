from django.urls import path, re_path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('<int:question_id>/', views.detail, name='detail'),
    ## ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    ## ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),




    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    
        re_path(r'^showlist/(?P<listID>([0-9]+|all))/(?P<clean>[a-z]+)?', views.showlist, name='showlist'),
        path('showrecipe/<int:recipeID>', views.showrecipe, name='showrecipe'),
        path('changeitemstock/<int:itemID>', views.changeitemstock, name='changeitemstock'),
        # re_path(r'^showrecipe/(?P<recipeID>([0-9]+))', views.showrecipe, name='showrecipe'),
        # re_path(r'^changeitemstock/(?P<itemID>[0-9]+)', views.changeitemstock, name='changeitemstock'),
        path('', views.index, name='index'),
]


# urlpatterns = patterns('shop.views',
#     url(r'^showlist/(?P<listID>([0-9]+|all))/(?P<clean>[a-z]+)?',
#         'list.showlist',
#         name='showlist'),
#     url(r'^showrecipe/(?P<recipeID>([0-9]+))',
#         'recipe.showrecipe',
#         name='showrecipe'),
#     #url(r'^showlist/all','shop.views.list.showfulllist'),
#     url(r'^changeitemstock/(?P<itemID>[0-9]+)',
#         'item.changeitemstock',
#         name='changeitemstock'),
#     url(r'^test$','test.index'),
#     url(r'^$','index.index'),
#     #url(r'^','shop.views.index', name='index'),
#     #url(r'^test','shop.views.index', name='index'),
# )
