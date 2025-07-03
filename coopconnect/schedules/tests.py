
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from schedules.models import Schedules
from trainings.models import Trainings
from village.models import Village
from extension.models import ExtensionWorker

class SchedulesAPITestCase(APITestCase):
    def setUp(self):
       
        self.training = Trainings.objects.create(
            topic="Soil Health",
            description="Learn about soil.",
            amount=100.0
        )
        self.village = Village.objects.create(
            village_name="MyVillage",
            village_cell= "VillageOne"
        )
        self.worker = ExtensionWorker.objects.create(
            name="John Doe",
            village_id=self.village
        )
        self.schedule = Schedules.objects.create(
            training=self.training,
            village=self.village,
            date="2025-07-01",
            extensionworker=self.worker
        )
        self.list_url = reverse('schedules-list')
        self.detail_url = reverse('schedules-detail', args=[self.schedule.id])

    def test_list_schedules(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_schedule(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_schedule(self):
        data = {
            "training": self.training.id,
            "village": self.village.id,
            "date": "2025-08-01",
            "extensionworker": self.worker.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_schedule(self):
        data = {
            "training": self.training.id,
            "village": self.village.id,
            "date": "2025-09-01",
            "extensionworker": self.worker.id
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_schedule(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)










