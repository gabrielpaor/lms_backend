from django.db import models
from teacher_backend.models import Grades, Schoolworks, ProfSubject

# Create your models here.


class StudentProfile(models.Model):
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
    )

    STATUS = (
        ("Active", "Acitive"),
        ("Offline", "Offline"),
        ("Do Not Disturb", "Do not Disturb"),
        ("Idle", "Idle"),
    )

    name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    studid = models.IntegerField()
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=50, null=True)
    bdate = models.DateField()
    placebirth = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


# relations per teacher = subject
class Subject(models.Model):
    subcode = models.ForeignKey(ProfSubject, on_delete=models.SET_NULL, null=True)


class StudGrades(models.Model):
    studgrades = models.ForeignKey(Grades, on_delete=models.SET_NULL, null=True)


# class Group(models.Model):
# Twillo


# relations to all the upcoming assignments, quizz, and activities
class Reminder(models.Model):
    reminders = models.ForeignKey(Schoolworks, on_delete=models.SET_NULL, null=True)
