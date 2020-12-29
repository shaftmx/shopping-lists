from django.contrib import admin

# Register your models here.

from django.forms import SelectMultiple
from django.db import models

from .models import *

class ShopListModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': SelectMultiple(attrs={'size':'30'},)
        },
    }

# Admin display model inline https://docs.djangoproject.com/fr/3.1/intro/tutorial07/
# class ItemInline(admin.TabularInline):
# # class ItemInline(admin.StackedInline):
#     model = Item
#     extra = 5
#     fields = ('name', 'desc')

class RecipeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': SelectMultiple(attrs={'size':'30'},)
        },
    }
    # inlines = [ItemInline]

#
# class ItemAdmin(admin.ModelAdmin):
#     #def queryset(self, request):
#     #    qs = super(MyModelAdmin, self).queryset(request)
#     #    if request.user.is_superuser:
#     #        return qs.
#     #    return qs.filter(author=request.name)
#     formfield_overrides = {
#         models.ManyToManyField: {
#             'widget': SelectMultiple(attrs={'size':'30'},)
#         },
#     }

admin.site.register(ShopList, ShopListModelAdmin)
admin.site.register(Item)
# admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
