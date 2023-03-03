from rest_framework import routers
from django.urls import path, include

from .views import (
    PointModelViewSet,
    ScoreModelViewSet
)

router_score = routers.DefaultRouter()

router_score.register('point',PointModelViewSet,"point")
router_score.register('',ScoreModelViewSet, "score")

urlpatterns = [
    path('v1/score/',include(router_score.urls)),
]
