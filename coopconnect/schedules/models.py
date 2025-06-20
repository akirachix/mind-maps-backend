from django.db import models


class Schedules(models.Model):
    training_id = models.ForeignKey(Trainings, )
    village_id = models.ForeignKey(Village, max_length=10)
    topic = models.CharField(max_length=200)
    date = models.DateField()
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    extensionworker = models.ForeignKey(ExtensionWorker, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.topic} ({self.date})"

