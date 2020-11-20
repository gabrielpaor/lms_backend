# Generated by Django 3.1.3 on 2020-11-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_backend', '0002_auto_20201119_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolworks',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='schoolworks',
            name='schoolwork',
            field=models.CharField(choices=[('Assignments', 'Assignments'), ('Quiz', 'Quiz'), ('Activities', 'Activities'), ('Projects', 'Projects')], max_length=60),
        ),
    ]