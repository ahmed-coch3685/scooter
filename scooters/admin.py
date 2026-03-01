from django.contrib import admin
from .models import *



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
class ProductDetailInline(admin.TabularInline):
    model = ProductDetail
    extra = 1
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductDetailInline]

admin.site.register(Category)

