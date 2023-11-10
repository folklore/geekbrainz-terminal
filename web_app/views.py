from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Recipe
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib import messages

def home_action(request):
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'web/home.html', {'recipes': recipes})


class RecipesController(viewsets.ViewSet):
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


def sign_up_action(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')

        messages.error(request, 'В форме регистрации допущены ошибки ...')

    form = SignUpForm()
    return render(request, 'web/auth/sign_up.html', {'sign_up_form': form})
