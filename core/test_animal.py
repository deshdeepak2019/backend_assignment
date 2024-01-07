from django.contrib.auth.models import User
from django.test import TestCase

from core.models import Animal, AnimalType


class TestModel(TestCase):
    def setUp(self) -> None:
        # Create user
        self.user = User.objects.create_user(username="demo", password="demo@123")
        self.animal1 = Animal.objects.create(
            name="Lion",
            age=1.5,
            type=AnimalType.CARNIVORE,
            sound="Roar",
            color="Yellow",
        )
        self.animal2 = Animal.objects.create(
            name="Tiger",
            age=1.5,
            type=AnimalType.CARNIVORE,
            sound="Roar",
            color="Yellow",
        )

    # Model Test Case
    def test_animal_object(self) -> None:
        animal = Animal.objects.create(
            name="Lion",
            age=1.5,
            type=AnimalType.CARNIVORE,
            sound="Roar",
            color="Yellow",
        )
        self.assertEqual(Animal.objects.count(), 3)
        assert animal.type == AnimalType.CARNIVORE
        assert animal.deleted_on == None

    # API Test cases
    def test_only_authenticate_user_can_hit_animal_apis(self) -> None:
        response = self.client.get(
            "/animal/",
        )
        # If user is not logged in then 401(Unauthorised) will be status code.
        assert response.status_code == 401

        # Now User is logged in

        login_response = self.client.post(
            "/accounts/login/",
            {
                "username": self.user.username,
                "password": "demo@123",
            },
            content_type="application/json",
        )

        assert login_response.status_code == 200

        # User again hit Get API, Now status code should be 200 instead of 401

        response = self.client.get(
            "/animal/",
        )
        # If user is not logged in then 401(Unauthorised) will be status code.
        assert response.status_code == 200
        assert response.json()["count"] == 2

        # Only Super user can delete data
        # As it is normal user so status code should be 403(No permission)

        destroy_response = self.client.delete(
            f"/animal/{self.animal1.pk}/",
        )
        assert destroy_response.status_code == 403

        # Now we will enabled superuser field true for this user
        self.user.is_superuser = True
        self.user.save(update_fields=["is_superuser"])

        # Again this user hit delete API and get status code 204.

        destroy_response = self.client.delete(
            f"/animal/{self.animal1.pk}/",
        )
        assert destroy_response.status_code == 204
