from rest_framework import serializers
from games.models import (
    Game,
    Player,
    Category
)

class GamesSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    def get_description(self, instance):
        return str(instance.description.html)

    class Meta:
        model = Game
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"