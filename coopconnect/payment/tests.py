from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Payment
from farmer.models import Farmer
from schedules.models import Schedules

class PaymentAPITests(APITestCase):
    def setUp(self):
        # Create a farmer and schedule for testing
        self.farmer = Farmer.objects.create(name="Test Farmer")  # Adjust fields as needed
        self.schedule = Schedules.objects.create(name="Test Schedule")  # Adjust fields as needed

    def test_create_payment(self):
        url = reverse('payment-list-create')
        data = {
            "farmer_id": self.farmer.id,
            "schedule_id": self.schedule.id,
            "amount": 100.00,
            "payment_method": "MTN",
            "status": "Completed",
            "transaction_code": "TX123456",
            "points_deducted": 10
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(Payment.objects.get().amount, 100.00)

    def test_list_payments(self):
        url = reverse('payment-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_payment(self):
        payment = Payment.objects.create(
            farmer_id=self.farmer,
            schedule_id=self.schedule,
            amount=100.00,
            payment_method="MTN",
            status="Completed",
            transaction_code="TX123456",
            points_deducted=10
        )
        url = reverse('payment-detail', kwargs={'pk': payment.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['amount'], 100.00)

    def test_update_payment(self):
        payment = Payment.objects.create(
            farmer_id=self.farmer,
            schedule_id=self.schedule,
            amount=100.00,
            payment_method="MTN",
            status="Completed",
            transaction_code="TX123456",
            points_deducted=10
        )
        url = reverse('payment-detail', kwargs={'pk': payment.pk})
        data = {
            "amount": 150.00,
            "status": "Pending"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        payment.refresh_from_db()
        self.assertEqual(payment.amount, 150.00)

    def test_delete_payment(self):
        payment = Payment.objects.create(
            farmer_id=self.farmer,
            schedule_id=self.schedule,
            amount=100.00,
            payment_method="MTN",
            status="Completed",
            transaction_code="TX123456",
            points_deducted=10
        )
        url = reverse('payment-detail', kwargs={'pk': payment.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Payment.objects.count(), 0)
