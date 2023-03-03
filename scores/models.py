from django.db import models
from users.models import User
from games.models import Game

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Score(models.Model):
    points = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(default=0)
    
    @property
    def points2(self):
        puntos = 0
        lista = Point.objects.filter(user=self.user)
        for li in lista:
            puntos +=li.points

        return puntos
    
    def __str__(self) -> str:
        return self.user.username

@receiver(post_save, sender=User)
def create_score(sender, instance, created, **kwargs):
    if created:
        Score.objects.create(user=instance)
        instance.save()
    

class Point(models.Model):
    points = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=200)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user} - {self.points} puntos"
    