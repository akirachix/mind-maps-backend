from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Attendance
from farmer.models import Farmer
from schedules.models import Schedules
from village.models import Village
from trainings.models import Trainings
from extension.models import ExtensionWorker

class AttendanceModelTest(TestCase):
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
        self.attendance = Attendance.objects.create(
            farmer=self.farmer,
            schedule=self.schedule,
            village=self.village
        )
    def test_attendance_creation(self):
         self.assertEqual(self.attendance.farmer, self.farmer)
         self.assertEqual(self.attendance.schedule, self.schedule)
         self.assertEqual(self.attendance.village, self.village)
         self.assertIsInstance(self.attendance, Attendance)


    def test_str_method(self):
        self.assertTrue(str(self.attendance))