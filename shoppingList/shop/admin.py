from django.contrib import admin
from django import forms
from django.utils.html import format_html
import io

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

class RecipeAdminForm(forms.ModelForm):
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': SelectMultiple(attrs={'size':'30'},)
        },
    }
    photo_upload = forms.ImageField(
        label="Photo (upload)",
        required=False,
        help_text="Formats acceptés : JPG, PNG, WEBP. Compressé automatiquement (max 800px, qualité 75%)."
    )

    class Meta:
        model = Recipe
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        photo_file = self.cleaned_data.get('photo_upload')
        if photo_file:
            try:
                from PIL import Image
                img = Image.open(photo_file)
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                max_size = 800
                if img.width > max_size or img.height > max_size:
                    img.thumbnail((max_size, max_size), Image.LANCZOS)
                buffer = io.BytesIO()
                img.save(buffer, format='JPEG', quality=75, optimize=True)
                instance.photo = buffer.getvalue()
                instance.photo_content_type = 'image/jpeg'
            except Exception:
                pass
        if commit:
            instance.save()
            self.save_m2m()
        return instance

class RecipeAdmin(admin.ModelAdmin):
    form = RecipeAdminForm
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        url = obj.get_photo_url_data() if obj and obj.pk else None
        if url:
            return format_html(
                '<img src="{}" style="max-height:200px; max-width:400px; border-radius:8px;" />',
                url
            )
        return "(aucune photo)"
    photo_preview.short_description = "Aperçu"

    # Adapter les fieldsets selon tes champs existants
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'items')
        }),
        ('Photo', {
            'fields': ('photo_preview', 'photo_upload'),
        }),
    )

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
admin.site.register(RecipeCategory)
admin.site.register(Recipe, RecipeAdmin)
