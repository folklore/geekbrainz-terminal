from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import home_action, RecipesController, sign_up_action


router = SimpleRouter(trailing_slash=False)
router.register(r'recipes', RecipesController)

urlpatterns = [
    path('', home_action, name='home'),
    path('', include(router.urls)),
    path('sign_up', sign_up_action, name='sign-up'),
]
