from rest_framework import routers
from django.urls import path, include
from .views import (
    GameModelViewSet,
    CategoryModelViewSet,
    PlayerModelViewSet
)

router_game = routers.DefaultRouter()

router_game.register('v1/games',GameModelViewSet,"games")
router_game.register('v1/category',CategoryModelViewSet,"category")
router_game.register('v1/player',PlayerModelViewSet,"player")

urlpatterns = [
    path('game/',include(router_game.urls)),
]


router_game.urls
