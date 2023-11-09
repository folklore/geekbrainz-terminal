from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import home, RecipeViewSet


router = SimpleRouter(trailing_slash=False)
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
]
