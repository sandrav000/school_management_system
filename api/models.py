from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Office Staff'),
        ('librarian', 'Librarian'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username  


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    student_class = models.CharField(max_length=50)

    def __str__(self):
        return self.name  


class LibraryHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default="Borrowed")

    def __str__(self):
        return self.book_name  


class FeesHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_type = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.fee_type 

