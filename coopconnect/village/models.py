from django.db import models

class Village(models.Model):
    name = models.CharField(max_length=100, unique=True)
    village_cell = models.CharField(max_length=100, blank=True)
    sector = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    province = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Village"
        verbose_name_plural = "Villages"
        ordering = ['name']
