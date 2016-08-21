from django.contrib import admin
from searcher import models


admin.site.register(models.Ingredient)
admin.site.register(models.Variation)
admin.site.register(models.Recipie)