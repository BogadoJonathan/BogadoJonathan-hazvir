from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from games.models import (
    Game,
    Category,
    Player
)

from .serializers import (
    GamesSerializer,
    CategorySerializer,
    PlayerSerializer
)

class GameModelViewSet(ModelViewSet):
    serializer_class = GamesSerializer
    queryset = Game.objects.all()

class CategoryModelViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class PlayerModelViewSet(ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    