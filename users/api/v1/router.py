from rest_framework import routers
from django.urls import path, include
from .views import UserModelViewSet, ObtainTokenPairWithEmailView, RefreshTokenView

router_user = routers.DefaultRouter()

router_user.register(r'',UserModelViewSet,'users')

urlpatterns = [
    path('v1/token/',ObtainTokenPairWithEmailView.as_view(), name="token"),
    path('v1/token/refresh', RefreshTokenView.as_view(),name="token_refresh"),
    path('v1/users/',include(router_user.urls)),
    #path('api/usuarios/', UserModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='usuario_list'),

]
