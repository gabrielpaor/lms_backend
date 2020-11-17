from django.db import models

# Create your models here.


class ProfessProfile(models.Model):
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
    )

    name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    numofstud = models.IntegerField()
    contactno = models.IntegerField(max_length=12)
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=50, null=True)
    bdate = models.DateField()
    placebirth = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Schoolworks(models.Model):
    WORKS = (
        ("As", "Assignments"),
        ("Qu", "Quiz"),
        ("Ac", "Activities"),
        ("Pr", "Projects"),
    )

    schoolwork = models.CharField(max_length=2, choices=WORKS)
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.schoolwork


# class Grades(models.Model):
#      subgrades = models.FloatField()
# relations to all students


# class Group(models.Model):
# Twillo

# class Reminder(models.Model):
# relations to all the upcoming assignments, quizz, and activities
