from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from trainings.models import Trainings
class TrainingsAPITestCase(APITestCase):
    def setUp(self):
        self.training = Trainings.objects.create(
            topic="Agroforestry Basics",
            description="Learn how trees benefit soil and yield",
            amount=500.00
        )
        self.list_url = reverse('trainings-list')
    def test_list_trainings(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    def test_retrieve_training(self):
        url = reverse('trainings-detail', kwargs={'pk': self.training.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['topic'], self.training.topic)
    def test_create_training(self):
        data = {
            'topic': "Post-Harvest Management",
            'description': "Reduce losses after harvest with smart storage",
            'amount': "300.00"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trainings.objects.count(), 2)
    def test_update_training(self):
        url = reverse('trainings-detail', kwargs={'pk': self.training.pk})
        updated_data = {
            'topic': "Agroforestry Updated",
            'description': self.training.description,
            'amount': self.training.amount
        }
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.training.refresh_from_db()
        self.assertEqual(self.training.topic, "Agroforestry Updated")
    def test_delete_training(self):
        url = reverse('trainings-detail', kwargs={'pk': self.training.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Trainings.objects.filter(pk=self.training.pk).exists())






