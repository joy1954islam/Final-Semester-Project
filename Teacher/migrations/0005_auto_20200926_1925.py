# Generated by Django 3.1.1 on 2020-09-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherEnroll', '0004_auto_20200920_2145'),
        ('Teacher', '0004_auto_20200926_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='interests',
            field=models.ManyToManyField(related_name='interested_students', to='TeacherEnroll.TeacherEnroll'),
        ),
    ]
