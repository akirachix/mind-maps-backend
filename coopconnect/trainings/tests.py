

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from trainings.models import Trainings

class TrainingsAPITestCase(APITestCase):
    def setUp(self):
        
        self.training = Trainings.objects.create(
            topic="Agroforestry",
            description="Learn agroforestry basics.",
            amount=500.00
        )
        self.list_url = reverse('trainings-list')
        self.detail_url = reverse('trainings-detail', args=[self.training.id])

    def test_list_trainings(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_training(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_training(self):
        data = {
            "topic": "Composting",
            "description": "How to compost organic waste.",
            "amount": 200.00
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_training(self):
        data = {
            "topic": "Agroforestry Updated",
            "description": "Learn agroforestry basics.",
            "amount": 500.00
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_training(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




