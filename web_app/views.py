from django.shortcuts import render
from .models import Recipe


def home(request):
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'web/home.html', {'recipes': recipes})
