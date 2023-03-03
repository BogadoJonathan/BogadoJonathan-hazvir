from django.contrib import admin
from games.models import Game, Category, Player
# Register your models here.

modelos = [Game,Category,Player]

admin.site.register(modelos)
