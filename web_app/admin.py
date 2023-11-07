from django.contrib import admin
from .models import Category, Recipe, Product, Ingredient

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Product)
admin.site.register(Ingredient)
