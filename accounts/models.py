from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from tenant.models import Company

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STAFF = "STAFF", "Staff"

    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.STAFF)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
company = models.ForeignKey(
    Company,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='users'
)
