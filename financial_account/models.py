from django.db import models
from student.models import Student

class FinancialAccount(models.Model):
    """a financial account constitutes of financial statements"""

    def __str__(self):
        return self.student.__str__()
        
    date_of_payment = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)