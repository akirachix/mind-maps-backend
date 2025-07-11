from django.test import TestCase
from .models import Village

class VillageModelTest(TestCase):

    def test_village_creation(self):
        village = Village.objects.create(
            village_name="Muhoro",
            village_cell="Dani"
        )
        self.assertEqual(village.village_name, "Muhoro")
        self.assertEqual(village.village_cell, "Dani")

    def test_str_method(self):
        village = Village.objects.create(
            village_name="Kijiji",
            village_cell="Jiji"
        )
        self.assertEqual(str(village), "Kijiji")

    def test_database_interaction(self):
        Village.objects.create(
            village_name="Simba",
            village_cell="Waya"
        )
        retrieved_village = Village.objects.get(village_name="Simba")
        self.assertEqual(retrieved_village.village_cell, "Waya")