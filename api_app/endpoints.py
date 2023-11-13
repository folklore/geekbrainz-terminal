from fastapi import APIRouter
from web_app.models import Recipe, Category
from django.core import serializers
from asgiref.sync import sync_to_async
from django.forms.models import model_to_dict


api_router = APIRouter()


@api_router.get("/recipes")
async def recipes_action():
    recipes = await sync_to_async(Recipe.objects.all)()
    data = serializers.serialize("json", recipes)
    return data


@api_router.get("/recipes/{title}")
async def recipes_by_title_action(title: str):
    recipe = await sync_to_async(Recipe.objects.get)(title__iexact=title)
    data = serializers.serialize("json", [recipe])
    return data


@api_router.get("/recipes/category/{category}")
async def recipes_by_category_action(category: str):
    recipes = await sync_to_async(Recipe.objects.filter)(categories__title__iexact=category)
    data = serializers.serialize("json", recipes)
    return data


@api_router.get("/recipes/ingredient/{ingredient}")
async def recipes_by_ingredient_action(ingredient: str):
    recipes = await sync_to_async(Recipe.objects.filter)(ingredients__name__iexact=ingredient)
    data = serializers.serialize("json", recipes)
    return data
