from django.db import models
from django.contrib.auth.models import UserManager as AbstractUserManager,AbstractUser
# Create your models here.

class Usermanager(AbstractUserManager):
    pass

class Account(AbstractUser):
    email = models.EmailField(verbose_name='email',unique=True)
    username = models.CharField(max_length=60,null=True,unique=True)
    is_admin = models.BooleanField(default=False,null=True,blank=True)
    is_staff = models.BooleanField(default=True,null=True,blank=True)
    is_superuser = models.BooleanField(default=False,null=True,blank=True)

    objects = Usermanager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "email"
    ]

    