from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password','last_login','is_superuser','is_staff','date_joined','user_permissions','groups',)

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('last_login','is_superuser','is_staff','date_joined','user_permissions','groups')

class ObtainTokenPairWithEmailSerializer(TokenObtainPairSerializer):
    """Serializer para el inicio de sesión con email en lugar de usuario."""
    @classmethod
    def get_token(cls, user):
        """Sobrescribimos el método get_token para devolver el token con el email del usuario."""
        token = super().get_token(user)
        token['email'] = user.email
        return token

    def validate(self, attrs):
        """Sobrescribimos el método validate para permitir el inicio de sesión con email."""
        credentials = {
            'email': attrs.get('email'),
            'password': attrs.get('password')
        }

        if not all(credentials.values()):
            raise serializers.ValidationError('Por favor, ingrese ambos campos "email" y "password".')

        user = authenticate(**credentials)

        if not user:
            raise serializers.ValidationError('No se pudo iniciar sesión con las credenciales proporcionadas.')

        if not user.is_active:
            raise serializers.ValidationError('Esta cuenta ha sido desactivada.')

        refresh = self.get_token(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return data
    
class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        refresh_token = attrs['refresh']
        token = RefreshToken(refresh_token)

        try:
            token.verify()
        except:
            raise serializers.ValidationError('Token de actualización no válido o expirado')

        data = {}
        data['access'] = str(token.access_token)

        return data





