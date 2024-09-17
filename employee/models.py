from django.db import models

# Create your models here.


class Employee(models.Model):

    DESIGNATION_CHOICES = [
        ("manager", "Manager"),
        ("developer", "Developer"),
        ("designer", "Designer"),
        ("hr", "HR"),
        ("sales", "Sales"),
    ]
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.name
