from django.contrib import admin

from .models import Animal


@admin.register(Animal)
class ElevatorAdmin(admin.ModelAdmin):  # type:ignore[type-arg]
    model = Animal
    can_delete = False
    can_change = False
    list_display = (
        "id",
        "name",
        "age",
        "color",
    )
