from django.db import models

# Create your models here.
class Build(models.Model):
    build_name = models.CharField(max_length=100)
    mythic = models.CharField(max_length=100)
    boots = models.CharField(max_length=100)
    legendary_1 = models.CharField(max_length=100)
    legendary_2 = models.CharField(max_length=100)
    legendary_3 = models.CharField(max_length=100)
    legendary_4 = models.CharField(max_length=100)

    def __str__(self):
        return self.build_name