# Generated by Django 4.1.5 on 2023-01-06 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_alter_student_stud_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stud_user',
        ),
    ]
