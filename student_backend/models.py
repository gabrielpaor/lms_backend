from django.db import models

# Create your models here.


class StudentProfile(models.Model):
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
    )

    name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    studid = models.IntegerField()
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=50, null=True)
    bdate = models.DateField()
    placebirth = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    subcode = models.CharField(max_length=50, null=True)
    subname = models.CharField(max_length=200, null=True)
    lec = models.FloatField()
    lab = models.FloatField()
    unit = models.FloatField()
    sched = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.subname


# class Grades(models.Model):
#     subgrades = models.FloatField()


# class Group(models.Model):
# Twillo

# class Reminder(models.Model):
# relations to all the upcoming assignments, quizz, and activities
