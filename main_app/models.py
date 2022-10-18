from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Build(models.Model):
    build_name = models.CharField(max_length=100)
    mythic = models.CharField(max_length=100)
    boots = models.CharField(max_length=100)
    legendary_1 = models.CharField(max_length=100)
    legendary_2 = models.CharField(max_length=100)
    legendary_3 = models.CharField(max_length=100)
    legendary_4 = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')

    def __str__(self):
        return self.build_name