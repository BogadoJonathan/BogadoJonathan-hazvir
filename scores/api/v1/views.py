from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated



from scores.models import Point,Score

from .serializers import (
    PointSerializer,
    ScoreSerializer
)

# @permission_classes([IsAuthenticatedOrReadOnly])
class PointModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PointSerializer
    queryset = Point.objects.all()
    

class ScoreModelViewSet(ModelViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()