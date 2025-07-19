from django.test import TestCase
from farmer.models import Farmer, Village
from schedules.models import Schedules
from trainings.models import Trainings
from extension.models import ExtensionWorker
from .models import Payment

class PaymentModelTest(TestCase):
    def setUp(self):
        self.village = Village.objects.create(name="Kijiji")
        self.training = Trainings.objects.create(topic="Animal Husbandry")
        self.extension_worker = ExtensionWorker.objects.create(full_name="Rambina Sambo")
      
        self.farmer = Farmer.objects.create(
            transaction_code="FARMTRAN123",
            full_name="Habimana Nshute",
            phone_number="0700000000",
            village_id=self.village,
            password="rasb18934"
        )

        
        self.schedule = Schedules.objects.create(
            training=self.training,
            village=self.village,
            date="2025-07-11",
            extensionworker=self.extension_worker,
            image_url="https://example.com/image.jpg"
        )

    def test_create_payment(self):
        payment = Payment.objects.create(
            farmer_id=self.farmer,
            schedule_id=self.schedule,
            amount=1200.50,
            payment_method="Points",
            status="Completed",
            transaction_code="PAYTRAN456",
            points_deducted=615
        )
        self.assertEqual(payment.farmer_id, self.farmer)
        self.assertEqual(payment.schedule_id, self.schedule)
        self.assertEqual(payment.amount, 1200.50)
        self.assertEqual(payment.payment_method, "Points")
        self.assertEqual(payment.status, "Completed")
        self.assertEqual(payment.transaction_code, "PAYTRAN456")
        self.assertEqual(payment.points_deducted, 615)
        self.assertIsNotNone(payment.createdat)

    def test_blank_amount_and_points(self):
        payment = Payment.objects.create(
            farmer_id=self.farmer,
            schedule_id=self.schedule,
            payment_method="Momo",
            status="Pending",
            transaction_code="MMOORAN789"
        )
        self.assertIsNone(payment.amount)
        self.assertIsNone(payment.points_deducted)