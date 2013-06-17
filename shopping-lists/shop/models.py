from django.db import models

# Create your models here.

from django.core.urlresolvers import reverse

#class User(models.Model):
#    firstname = models.CharField(max_length=200)
#    lastname = models.CharField(max_length=200)
#
#    def __unicode__(self):
#        return '%s %s' % (self.firstname, self.lastname)


class ShopList(models.Model):
    name = models.CharField(max_length=200)
    items = models.ManyToManyField('Item')

    def __unicode__(self):
        return '%s' % (self.name)

class Item(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200,default='',blank=True)
    outOfStock = models.BooleanField()
    cathegory = models.ForeignKey('Category')

    def __unicode__(self):
        return '%s' % (self.name)

class Category(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200,default='',blank=True)

    def __unicode__(self):
        return '%s' % (self.name)

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200,default='',blank=True)
    items = models.ManyToManyField('Item')

    def __unicode__(self):
        return '%s' % (self.name)

#  `liste_user_id` int(11) NOT NULL,
