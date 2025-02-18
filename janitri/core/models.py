from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Unique related_name
        blank=True
    )

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    contact = models.CharField(max_length=15)

class HeartRate(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rate = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)