from django.db import models
from student.models import Student

class FinancialAccount(models.Model):
    class Meta:
        ordering = ['-date_of_payment']

    """a financial account constitutes of financial transactions"""
    def __str__(self):
        return self.student.__str__()
    
    TRANSACTION_TYPE_CHOICES = (
        ('credit','Credit'),
        ('debit','Debit')
    )
    transaction_type = models.CharField(max_length=7,choices=TRANSACTION_TYPE_CHOICES,default='credit')
    date_of_payment = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    arrears = models.DecimalField(max_digits=8,decimal_places=2)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)


