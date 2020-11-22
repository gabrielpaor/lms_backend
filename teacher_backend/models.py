from django.db import models
from student_backend.models import *

# Create your models here.


class ProfessProfile(models.Model):
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
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    numofstud = models.IntegerField()
    contactno = models.IntegerField()
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=50, null=True)
    bdate = models.DateField()
    placebirth = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Schoolworks(models.Model):
    WORKS = (
        ("Assignments", "Assignments"),
        ("Quiz", "Quiz"),
        ("Activities", "Activities"),
        ("Projects", "Projects"),
    )

    schoolwork = models.CharField(max_length=60, choices=WORKS)
    title = models.CharField(max_length=100, null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    duedate = models.DateTimeField(null=True)

    def __str__(self):
        return self.title


class Schedule(models.Model):
    days = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.days


class ProfSubject(models.Model):
    subcode = models.CharField(max_length=50, null=True)
    subname = models.CharField(max_length=200, null=True)
    lec = models.FloatField(max_length=3)
    lab = models.FloatField(max_length=3)
    unit = models.FloatField(max_length=3)
    schedule = models.ManyToManyField(Schedule)
    name = models.ForeignKey(ProfessProfile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.subname


class Grades(models.Model):
    grades = models.FloatField()


# relations to all students


# class Group(models.Model):
# Twillo
