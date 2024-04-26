from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Player)
admin.site.register(models.Nationality)
admin.site.register(models.HeightType)
admin.site.register(models.BowlerType)
admin.site.register(models.BattingType)
admin.site.register(models.BowlingType)




