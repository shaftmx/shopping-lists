from django.db import models
from django.utils import timezone

import markdown

# Create your models here.

class ShopList(models.Model):
    name = models.CharField(max_length=200)
    items = models.ManyToManyField('Item')
    def __str__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class Item(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='', blank=True)
    outOfStock = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.RESTRICT)
    # recipes = models.ForeignKey('Recipe', on_delete=models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name', 'category']

class Category(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, default='', blank=True)
    def __str__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(default='', blank=True)
    items = models.ManyToManyField('Item')
    def __str__(self):
        return '%s' % (self.name)
    def html_desc(self):
        return markdown.markdown(self.desc)
    class Meta:
        ordering = ['name']


# # Legacy (keeping for migration generation)
# class ShopList(models.Model):
#     name = models.CharField(max_length=200)
#     items = models.ManyToManyField('Item')
#
#     def __unicode__(self):
#         return '%s' % (self.name)
#
#     class Meta:
#         ordering = ['name']
#
# class Item(models.Model):
#     name = models.CharField(max_length=200)
#     desc = models.CharField(max_length=200,default='',blank=True)
#     outOfStock = models.BooleanField()
#     cathegory = models.ForeignKey('Category', on_delete=models.RESTRICT )
#
#     def __unicode__(self):
#         return '%s' % (self.name)
#
#     class Meta:
#         ordering = ['name', 'cathegory']
#
# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     desc = models.CharField(max_length=200,default='',blank=True)
#
#     def __unicode__(self):
#         return '%s' % (self.name)
#
#     class Meta:
#         ordering = ['name']
#
# class Recipe(models.Model):
#     name = models.CharField(max_length=200)
#     desc = models.CharField(max_length=200,default='',blank=True)
#     items = models.ManyToManyField('Item')
#
#     def __unicode__(self):
#         return '%s' % (self.name)
#     class Meta:
#         ordering = ['name']
