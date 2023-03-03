from django.db import models
from users.models import User
from django_quill.fields import QuillField


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=240, blank=True)
    emoji = models.CharField(max_length=10, default='✋')
    
    def __str__(self) -> str:
        return f"{self.title} {self.emoji}"
    
class Game(models.Model):
    STATUS = (
        ('S','Sin Empezar'),
        ('P','En Proceso'),
        ('T','Terminado'),
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS, help_text='Selecciona el estado del juego')
    description = QuillField(blank=True)
    rating = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.title} ({self.creator})"

class Player(models.Model):
    STATUS = (
        ('J','En Juego'),
        ('E','Eliminado'),
        ('G','Ganador'),
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(default=0)
    note = models.CharField(max_length=70)
    status = models.CharField(max_length=1, choices=STATUS, help_text='Selecciona el estado del jugador')
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user} - {self.game.title}"