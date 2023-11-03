from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser, PermissionsMixin

from user.manager import UserManager


class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    

    


