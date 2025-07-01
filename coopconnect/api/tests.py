from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from village.models import Village


class UserAPITests(APITestCase):
    def setUp(self):
        
        self.village = Village.objects.create(
            village_name="Kivu",
            longtitude=12.34,
            latitude=56.78
        )

        
        self.user_data = {
            "name": "Muhiri",
            "village_id": self.village.id,  
            "phone_number": "1234567890",
            "password": "testpass123",
            "email": "muhiri@example.com",
            "user_type": "Farmer"
        }

        self.list_url = reverse('user-list')

    def test_create_user(self):
        response = self.client.post(self.list_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, "Muhiri")

    def test_get_users_list(self):
        
        User.objects.create(**{
            k: v if k != 'village_id' else self.village for k, v in self.user_data.items()
        })

        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_user(self):
    
        user = User.objects.create(**{
            k: v if k != 'village_id' else self.village for k, v in self.user_data.items()
        })
        detail_url = reverse('user-detail', args=[user.id])
        response = self.client.get(detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], user.name)

    def test_update_user(self):
        
        user = User.objects.create(**{
            k: v if k != 'village_id' else self.village for k, v in self.user_data.items()
        })

        updated_data = self.user_data.copy()
        updated_data['name'] = 'Habimana'

        detail_url = reverse('user-detail', args=[user.id])
        response = self.client.put(detail_url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user.refresh_from_db()
        self.assertEqual(user.name, 'Habimana')

    def test_delete_user(self):
    
        user = User.objects.create(**{
            k: v if k != 'village_id' else self.village for k, v in self.user_data.items()
        })

        detail_url = reverse('user-detail', args=[user.id])
        response = self.client.delete(detail_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

