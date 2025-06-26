from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from schedules.models import Schedules
from trainings.models import Trainings
from village.models import Village
from extension.models import ExtensionWorker
from django.contrib.auth.models import User  
class SchedulesAPITestCase(APITestCase):
    def setUp(self):

        self.training = Trainings.objects.create(topic="Soil Health", description="Improving soil quality",amount=100.0)
        self.village = Village.objects.create(village_name="Kijiji",longitude=0.0 ,latitude=0.0)
        self.extensionworker = ExtensionWorker.objects.create(name="Jane Doe",  village_id=self.village )  
        self.schedule = Schedules.objects.create(
            training=self.training,
            village=self.village,
            date="2025-06-27",
            extensionworker=self.extensionworker
        )
        self.list_url = reverse('schedules-list')

        
    def test_list_schedules(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    def test_retrieve_schedule(self):
        url = reverse('schedules-detail', kwargs={'pk': self.schedule.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.schedule.pk)
    def test_create_schedule(self):
        data = {
            'training': self.training.id,
            'village': self.village.id,
            'date': "2025-07-01",
            'extensionworker': self.extensionworker.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Schedules.objects.count(), 2)
    def test_update_schedule(self):
        url = reverse('schedules-detail', kwargs={'pk': self.schedule.pk})
        new_date = "2025-07-15"
        data = {
            'training': self.training.id,
            'village': self.village.id,
            'date': new_date,
            'extensionworker': self.extensionworker.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.schedule.refresh_from_db()
        self.assertEqual(str(self.schedule.date), new_date)
    def test_delete_schedule(self):
        url = reverse('schedules-detail', kwargs={'pk': self.schedule.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Schedules.objects.filter(pk=self.schedule.pk).exists())










