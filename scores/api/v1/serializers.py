from rest_framework import serializers
from scores.models import Point, Score

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = "__all__"

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['points','points2','level']#"__all__"
        