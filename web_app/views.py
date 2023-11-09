from django.shortcuts import render
from rest_framework import viewsets
from .models import Recipe


def home(request):
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'web/home.html', {'recipes': recipes})


class RecipeViewSet(viewsets.ViewSet):
    queryset = Recipe.objects.all()

    def list(self, request):
        recipes = Recipe.objects.all()
        return render(request, 'web/recipes/list.html', {'recipes': recipes})

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        recipe = Recipe.objects.get(pk=pk)
        return render(request, 'web/recipes/retrieve.html', {'recipe': recipe})

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
