from django.test import TestCase
from .models import Refund
from payment.models import Payment
from farmer.models import Farmer
from schedules.models import Schedules
from village.models import Village
from trainings.models import Trainings
from extension.models import ExtensionWorker

class RefundModelTest(TestCase):
    def setUp(self):

        self.village = Village.objects.create(
            village_name="Test Village",
            longtitude=36.8219,
            latitude=-1.2921
        )
       
        self.farmer = Farmer.objects.create(
            full_name="Test Farmer",
            phone_number="1234567890",
            village_id=self.village,
            password="testpassword"
        )
        self.training = Trainings.objects.create(
            topic="Test Training",
            description="Test description",
            amount=50.00
        )
    
        self.extensionworker = ExtensionWorker.objects.create(
            name="Test Worker",
            village_id=self.village,
            phone_number="0712345678",
            password="testpassword",
            email="worker@example.com"
        )
       
        self.schedule = Schedules.objects.create(
            training=self.training,
            village=self.village,
            date="2024-01-10",
            extensionworker=self.extensionworker
        )
       
        self.payment = Payment.objects.create(
            farmer_id=self.farmer,
            schedule_id=self.schedule,
            amount=100.0,
            payment_method="Cash",
            status="Completed",
            transaction_code="TX123456",
            points_deducted=10
        )
      
        self.refund = Refund.objects.create(
            payment_id=self.payment,
            farmer_id=self.farmer
        )

    def test_refund_creation(self):
        self.assertEqual(self.refund.payment_id, self.payment)
        self.assertEqual(self.refund.farmer_id, self.farmer)
        self.assertIsInstance(self.refund, Refund)

    def test_str_method(self):
        self.assertTrue(str(self.refund))