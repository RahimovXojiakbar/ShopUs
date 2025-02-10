from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models

@admin.register(models.Bigcategory)
class BigCategoryAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(models.Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('uuid', 'name', 'product', 'created_at')
    search_fields = ('name', 'product__name')



@admin.register(models.SmallCategory)
class SmallCategoryAdmin(ModelAdmin):
    list_display = ['name', 'big_category']
    search_fields = ['name']
    list_filter = ['big_category']


@admin.register(models.Product)
class ProductAdmin(ModelAdmin):
    list_display = ['uuid','name', 'big_category', 'small_category', 'price']
    search_fields = ['name']
    list_filter = ['uuid', 'big_category', 'small_category']


