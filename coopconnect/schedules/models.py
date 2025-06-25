from django.db import models
from trainings.models import Trainings
from extension.models import ExtensionWorker

class Schedules(models.Model):
    training = models.ForeignKey('trainings.Trainings', on_delete=models.CASCADE)
    village = models.ForeignKey('village.Village', on_delete=models.CASCADE)
    date = models.DateField()
    extensionworker = models.ForeignKey('extension.ExtensionWorker', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
<<<<<<< HEAD
        return f"{self.topic} ({self.date})"

from django.db import models
class Trainings(models.Model):
    topic = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    amount = models.DecimalField(max_digits=10 ,decimal_places=2)


=======
        return f" ({self.date})"
>>>>>>> 637313f7c580ebaf2fada4e6a490309d0853c26b
