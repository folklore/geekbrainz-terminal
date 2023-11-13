from django.contrib import admin
from .models import Category, Ingredient, Recipe

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)
