from django.test import TestCase

from core.models import Animal, AnimalType


class TestModel(TestCase):
    def test_animal_object(self) -> None:
        animal = Animal.objects.create(
            name="Lion",
            age=1.5,
            type=AnimalType.CARNIVORE,
            sound="Roar",
            color="Yellow",
        )
        self.assertEqual(Animal.objects.count(), 1)
        assert animal.type == AnimalType.CARNIVORE
        assert animal.deleted_on == None
