from django.db import models
from subject.models import Subject
from user_account.models import CustomUser

class Teacher(models.Model):

    subjects = models.ManyToManyField(Subject)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    