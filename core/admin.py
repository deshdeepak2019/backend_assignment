from django.contrib import admin

from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    model = Animal
    can_delete = False
    can_change = False
    list_display = ("id", "name", "age", "color", "sound", "deleted_on")
