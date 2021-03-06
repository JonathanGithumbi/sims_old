from django.db import models

from user_account.models import CustomUser
from grade.models import Grade

class Student(models.Model):

    def __str__(self):
        user = self.user
        return user.first_name +' '+user.middle_name+' '+user.last_name

    grade_admitted_to = models.ForeignKey(Grade,on_delete = models.DO_NOTHING)
    current_grade = models.ForeignKey(Grade,null=True,related_name='current_grade',on_delete = models.DO_NOTHING)
    primary_contact_name = models.CharField(max_length = 30)
    primary_contact_phone_number = models.CharField(max_length = 14)
    secondary_contact_name = models.CharField(max_length = 30)
    secondary_contact_phone_number = models.CharField(max_length=14)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # optionals 
    hot_lunch = models.BooleanField(default=False)
    transport = models.BooleanField(default=False)
    

