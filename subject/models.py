from django.db import models

class Subject(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length = 30)

