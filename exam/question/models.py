from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password, **extra_fields):
    
        if not phone:
            raise ValueError(_('The Phone must be set'))
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
    
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser) :
    username = None
    phone = models.CharField(max_length=11, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) : 
        return self.phone

class Question(models.Model):
    question = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User)
    
    def __str__(self):
        return self.question


class Option(models.Model):
    tilte = models.CharField(max_length=255)
    number_option = models.CharField(max_length=11)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='option')

    def __str__(self):
        return self.tilte


