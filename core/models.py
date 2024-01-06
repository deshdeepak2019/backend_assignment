from django.db import models


class AnimalType(models.IntegerChoices):
    """
    Choices for running status of the Animal Type Based on food
    """

    HERBIVORE = 1
    CARNIVORE = 2
    OMNIVORE = 3


class Animal(models.Model):
    class Meta:
        constraints = [
            models.CheckConstraint(
                name="age_should_be_greater_than_zero",
                check=models.Q(age__gte=0),
            ),
        ]

    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Datetime when this object was created",
    )
    modified_on = models.DateTimeField(
        auto_now=True,
        help_text="Datetime when this object was last modified",
    )
    name = models.CharField(
        max_length=64, help_text="Name of animal like lion,tiger,etc.."
    )
    age = models.FloatField(help_text="Age of animal in years")
    type = models.IntegerField(
        choices=AnimalType.choices,
        default=0,
        help_text="Type of animal based on food",
    )
    sound = models.CharField(max_length=64, help_text="Sound of animal")
    color = models.CharField(max_length=64, help_text="Color of animal")
    deleted_on = models.DateTimeField(
        default=None,
        null=True,
        blank=True,
        help_text="When this animal was deleted from our database",
    )


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
