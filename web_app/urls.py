from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    home_action,
    RecipesController,
    sign_up_action,
    sign_in_action,
    sign_out_action,
)

router = SimpleRouter(trailing_slash=False)
router.register(r'recipes', RecipesController)

urlpatterns = [
    path('', home_action, name='home'),
    path('', include(router.urls)),
    path('sign_up', sign_up_action, name='sign-up'),
    path('sign_in', sign_in_action, name='sign-in'),
    path('sign_out', sign_out_action, name= 'sign-out'),
]
