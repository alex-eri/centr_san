__author__ = 'eri'
from django.db import models

from shop_categories.models.defaults.category.base import ProductCategoryBase


class Category(ProductCategoryBase):

    image = models.ImageField(upload_to='categoryimages/', null=True, blank=True)

    class Meta:
        abstract = False
        app_label = 'myshop'