from django.db import models


# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=200)
    secondname = models.CharField(max_length=200)
    emp_id = models.IntegerField()

    # return response ina string formst
    def __str__(self):
        return self.firstname
