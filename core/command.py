from django.core.management.base import BaseCommand

from core.models import Animal, AnimalType


class Command(BaseCommand):
    help = "Create an Animal object from the command line"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Name of the animal")
        parser.add_argument("age", type=float, help="Age of the animal")
        parser.add_argument(
            "animal_type",
            type=int,
            choices=[t[0] for t in AnimalType.choices],
            help="Type of the animal (HERBIVORE = 1, CARNIVORE = 2, OMNIVORE = 3)",
        )
        parser.add_argument("sound", type=str, help="Sound of the animal")
        parser.add_argument("color", type=str, help="Color of the animal")

    def handle(self, *args, **options):
        name = options["name"]
        age = options["age"]
        animal_type = options["animal_type"]
        sound = options["sound"]
        color = options["color"]

        # Create the Animal object
        animal = Animal.objects.create(
            name=name, age=age, type=animal_type, sound=sound, color=color
        )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created animal with ID {animal.pk}")
        )
