from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users.manager import CustomUserManger
 
 
class User(AbstractBaseUser, PermissionsMixin):
    """
    Only admin exist i mean admin can create account. Visitors browse the site without any account.
    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
 
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
 
    objects = CustomUserManger()
 
    class Meta:
        db_table = "users"
        verbose_name = "Admin User"
        verbose_name_plural = "Admin users"
 
    def __str__(self):
        return self.email