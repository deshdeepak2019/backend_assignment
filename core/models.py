from django.db import models


class AnimalType(models.IntegerChoices):
    """
    Choices for running status of the elevator system
    """

    HERBIVORE = 1
    CARNIVORE = 2
    OMNIVORE = 3


class Animal(models.Model):
    class Meta:  # pylint: disable=R0903
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
