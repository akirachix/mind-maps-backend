from django.test import TestCase
from .models import Village



class VillageModelTest(TestCase):
        def test_village_creation(self):
            village = Village.objects.create(
                village_name="Test Village",
                longtitude=10.123,
                latitude=20.456
            )
            self.assertEqual(village.village_name, "Test Village")
            self.assertIsInstance(village.longtitude, float)
            self.assertIsInstance(village.latitude, float)




class VillageModelTest(TestCase):
        def test_str_method(self):
            village = Village.objects.create(
                village_name="Another Village",
                longtitude=30.789,
                latitude=40.012
            )
            self.assertEqual(str(village), "Another Village")



class VillageModelTest(TestCase):
        def test_database_interaction(self):
            Village.objects.create(
                village_name="DB Village",
                longtitude=50.321,
                latitude=60.654
            )
            retrieved_village = Village.objects.get(village_name="DB Village")
            self.assertEqual(retrieved_village.longtitude, 50.321)




            