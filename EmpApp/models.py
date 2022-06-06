from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Roll(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(models.Model):
    eid = models.IntegerField(unique=True, primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dept = models.ForeignKey(Department,  on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    roll = models.ForeignKey(Roll, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name
