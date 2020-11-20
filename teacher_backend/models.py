from django.db import models

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

    def __str__(self):
        return self.schoolwork


class Grades(models.Model):
    grades = models.FloatField()


# relations to all students


# class Group(models.Model):
# Twillo

# class Reminder(models.Model):
# relations to all the upcoming assignments, quizz, and activities
