from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Recipe

from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, SignInForm, RecipeForm


def home_action(request):
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'web/home.html', {'recipes': recipes})


class RecipesController(viewsets.ViewSet):
    queryset = Recipe.objects.all()

    def list(self, request):
        recipes = self.queryset
        return render(request, 'web/recipes/list.html', {'recipes': recipes})

    @action(detail=False, methods=['get'])
    def new(self, request):
        recipe = Recipe()
        form = RecipeForm(instance=recipe)
        return render(request, 'web/recipes/new.html', {
            'recipe_form': form,
            'recipe': recipe
        })

    def create(self, request):
        recipe = Recipe(author = request.user)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect(f'/recipes/{recipe.pk}')
        return render(request, 'web/recipes/new.html', {'recipe_form': form, 'recipe': recipe})

    def retrieve(self, request, pk=None):
        recipe = get_object_or_404(self.queryset, pk=pk)
        return render(request, 'web/recipes/retrieve.html', {'recipe': recipe})

    @action(detail=True, methods=['get'])
    def edit(self, request, pk=None):
        recipe = get_object_or_404(self.queryset, pk=pk)
        form = RecipeForm(instance=recipe)
        return render(request, 'web/recipes/edit.html', {
            'recipe_form': form,
            'recipe': recipe
        })

    def update(self, request, pk=None):
        recipe = get_object_or_404(self.queryset, pk=pk)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect(f'/recipes/{recipe.pk}')
        return render(request, 'web/recipes/edit.html', {'recipe_form': form, 'recipe': recipe})

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


def sign_in_action(request):
    if request.method == 'POST':
        form = SignInForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                messages.success(request, 'Вы успешно авторизовались!')
                return redirect('home')

        messages.error(request, 'В форме авторизации допущены ошибки ...')

    form = SignInForm()
    return render(request, 'web/auth/sign_in.html', {'sign_in_form': form})


def sign_out_action(request):
    logout(request)
    messages.info(request, 'До встречи!')

    return redirect('home')
