
from django.contrib import admin
from shop.models import *

from django.forms import SelectMultiple
from django.db import models
from models import *

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': SelectMultiple(attrs={'size':'30'},)
        },
    }

class RecipeAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': SelectMultiple(attrs={'size':'30'},)
        },
    }

class ItemAdmin(admin.ModelAdmin):
    #def queryset(self, request):
    #    qs = super(MyModelAdmin, self).queryset(request)
    #    if request.user.is_superuser:
    #        return qs.
    #    return qs.filter(author=request.name)
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': SelectMultiple(attrs={'size':'30'},)
        },
    }

admin.site.register(ShopList, YourModelAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
