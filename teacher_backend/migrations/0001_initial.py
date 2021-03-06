# Generated by Django 3.1.3 on 2020-11-22 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfessProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('status', models.CharField(choices=[('Active', 'Acitive'), ('Offline', 'Offline'), ('Do Not Disturb', 'Do not Disturb'), ('Idle', 'Idle')], max_length=200, null=True)),
                ('numofstud', models.IntegerField()),
                ('contactno', models.IntegerField()),
                ('address', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('bdate', models.DateField()),
                ('placebirth', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schoolworks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolwork', models.CharField(choices=[('Assignments', 'Assignments'), ('Quiz', 'Quiz'), ('Activities', 'Activities'), ('Projects', 'Projects')], max_length=60)),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('duedate', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcode', models.CharField(max_length=50, null=True)),
                ('subname', models.CharField(max_length=200, null=True)),
                ('lec', models.FloatField()),
                ('lab', models.FloatField()),
                ('unit', models.FloatField()),
                ('sched', models.CharField(max_length=200, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher_backend.professprofile')),
            ],
        ),
    ]
