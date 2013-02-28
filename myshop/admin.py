__author__ = 'eri'
from django.contrib import admin

from models import SimpleProduct
from models.category import Category

class ProductAdmin(admin.ModelAdmin):
    pass



from shop_categories.admin import ProductCategoryAdmin


admin.site.register(SimpleProduct, ProductAdmin)
admin.site.register(Category, ProductCategoryAdmin)