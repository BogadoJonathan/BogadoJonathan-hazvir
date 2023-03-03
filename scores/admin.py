from django.contrib import admin
from scores.models import Point,Score

modelos = [Point,Score]

admin.site.register(Point)

class ScoreAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields':('level','points2',),
        }),
        )
    readonly_fields = ('points2',)

admin.site.register(Score,ScoreAdmin)