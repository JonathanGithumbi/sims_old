
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from django.utils import timezone
class CustomUser(AbstractUser):
    def __str__(self):
        return self.first_name+' '+self.middle_name+' '+self.last_name

    GENDER_CHOICES = [
        ('male','Male'),
        ('female','Female')
    ]
    email = models.EmailField(_("email address"), unique=True)
    middle_name = models.CharField(_("Middle Name"), max_length=50)
    image = models.ImageField(_("Picture"), upload_to='images/',default='images/default_user_avatar.png')
    gender = models.CharField(max_length = 6, choices= GENDER_CHOICES, default='male')
    date_of_birth = models.DateField(default=timezone.now)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    

