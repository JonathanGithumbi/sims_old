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

    def save(self, *args, **kwargs):
        """This method will update the StudentFees table"""
        curr_bal = CurrentBalance.objects.filter(student=self.student).exists()# Check whether the specified record exists
        if curr_bal:
            curr_bal_record = CurrentBalance.objects.get(student=self.student)
            curr_bal_record.current_balance = self.arrears
            curr_bal_record.save()
        else:
            curr_bal_record = CurrentBalance()# Create new record When registering students
            curr_bal_record.student=self.student
            curr_bal_record.current_balance=self.arrears
            curr_bal_record.save()
        super(FinancialAccount, self).save(*args, **kwargs)


class CurrentBalance(models.Model):
    """Contains current balance statements/records"""
    """For internal use: allows easier reading of students' fees arrears"""
    """This keeps a one to one record of the current balance per child every payment made updates the one record per student """
    student = models.OneToOneField(Student, on_delete=models.CASCADE,unique=True)
    current_balance = models.DecimalField(max_digits=8, decimal_places=2)

