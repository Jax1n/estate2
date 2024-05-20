from . models import *
from django.contrib import admin


class ProductImageInline(admin.TabularInline):
    model = Image

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = (ProductImageInline,)
