__author__ = 'eri'

# coding: utf-8
from django.db import models
from polymorphic.manager import PolymorphicManager
# from shop.models.productmodel import Product
from shop_categories.models.defaults.product.base import CategoryProductBase

class DumbManager(PolymorphicManager):
    """A dumb manager to test the behavior with poylmorphic"""
    def get_all(self):
        return self.all()


class SimpleProduct(CategoryProductBase):
    objects = DumbManager()
    ident = models.CharField(max_length=40,unique=True)
    class Meta:
        pass