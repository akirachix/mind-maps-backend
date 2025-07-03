from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rewards.models import Rewards
from attendance.models import Attendance
from farmer.models import Farmer
from schedules.models import Schedules
from trainings.models import Trainings
from village.models import Village
from extension.models import ExtensionWorker
from datetime import date

class RewardsAPITestCase(APITestCase):
    def setUp(self):
        self.village = Village.objects.create(
            village_name="Test Village",
            village_cell="Test Cell"
        )
        self.farmer = Farmer.objects.create(
            full_name="Test Farmer",
            phone_number="0712345678",
            village_id=self.village,
            password="testpass"
        )
        self.training = Trainings.objects.create(
            topic="Test Topic",
            description="Test Description",
            amount=50.00
        )
        self.extensionworker = ExtensionWorker.objects.create(
            name="Test EW",
            village_id=self.village,
            phone_number="0711111111",
            password="extpass123",
            email="testew@example.com"
        )
        self.schedule = Schedules.objects.create(
            training=self.training,
            village=self.village,
            date=date.today(),
            extensionworker=self.extensionworker
        )
        self.attendance = Attendance.objects.create(
            farmer=self.farmer,
            schedule=self.schedule,
            village=self.village
        )
        self.reward = Rewards.objects.create(
            farmer_id=self.farmer,
            attendance_id=self.attendance,
            farmer_points=100
        )
        self.list_url = reverse('rewards-list')
        self.detail_url = reverse('rewards-detail', args=[self.reward.id])

    def test_list_rewards(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_reward(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)

    def test_create_reward(self):
        data = {
            "farmer_id": self.farmer.id,
            "attendance_id": self.attendance.id,
            "farmer_points": 50
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, 201)

    def test_update_reward(self):
        data = {
            "farmer_id": self.farmer.id,
            "attendance_id": self.attendance.id,
            "farmer_points": 200
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, 200)

    def test_delete_reward(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)