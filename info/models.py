from django.db import models
from grade.models import Grade

class FeesStructure(models.Model):
    """The system should have the calender for only the current year at a time"""
    def __str__(self):
        year = str(self.year)
        term = str(self.term)
        grade = str(self.grade)
        
        return 'Year: '+ year + ' Term: '+term + 'Grade: '+grade

    year = models.IntegerField()
    term = models.IntegerField()
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    admission = models.IntegerField()
    diary_and_report_book = models.IntegerField()
    interview_fee = models.IntegerField()
    tuition_fee = models.IntegerField()
    hot_lunch = models.IntegerField()
    transport = models.IntegerField()


class AcademicCalendar(models.Model):
    """The system should have only one academic calendar at any given time"""
    def __str__(self):
        year = self.year
        year = str(year)
        return year

    year = models.IntegerField()
    term_1_start_date = models.DateTimeField()
    term_1_mid_term_break_start = models.DateTimeField()
    term_1_mid_term_break_end = models.DateTimeField()
    term_1_end_date = models.DateTimeField()
    term_2_start_date = models.DateTimeField()
    term_2_mid_term_break_start = models.DateTimeField()
    term_2_mid_term_break_end = models.DateTimeField()
    term_2_end_date = models.DateTimeField()
    term_3_start_date = models.DateTimeField()
    term_3_mid_term_break_start = models.DateTimeField()
    term_3_mid_term_break_end = models.DateTimeField()
    term_3_end_date = models.DateTimeField()
    kcpe_start_date = models.DateTimeField()
    kcpe_end_date = models.DateTimeField()
    

