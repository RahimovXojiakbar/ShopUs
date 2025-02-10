from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models

@admin.register(models.Bigcategory)
class BigCategoryAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(models.MiddleCategory)
class MiddleCategoryAdmin(ModelAdmin):
    list_display = ['name', 'big_category']
    search_fields = ['name']
    list_filter = ['big_category']


@admin.register(models.SmalllCategory)
class SmallCategoryAdmin(ModelAdmin):
    list_display = ['name', 'middle_category']
    search_fields = ['name']
    list_filter = ['middle_category']


@admin.register(models.Product)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'big_category', 'middle_category', 'small_category', 'price']
    search_fields = ['name']
    list_filter = ['big_category', 'middle_category', 'small_category']


