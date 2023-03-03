from rest_framework.permissions import  IsAuthenticated

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from .serializers import UserSerializer, UserCreateSerializer, ObtainTokenPairWithEmailSerializer,TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




class ObtainTokenPairWithEmailView(TokenObtainPairView):
    serializer_class = ObtainTokenPairWithEmailSerializer
    
class RefreshTokenView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

class UserModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        #si es get se lanzara el serializer sin password
        if self.action == "list" or self.action == "retrieve":
            
            return UserSerializer
        #caso contrario tendra el password
        else:
            return UserCreateSerializer
        