from django.db import models
from student.models import Student

class FinancialAccount(models.Model):
    """a financial account constitutes of financial statements"""
    date_of_payment = models.DateField()
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)