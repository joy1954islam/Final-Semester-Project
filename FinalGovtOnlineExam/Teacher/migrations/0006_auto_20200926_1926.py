# Generated by Django 3.1.1 on 2020-09-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GovernmentEmployee', '0004_auto_20200920_2133'),
        ('Teacher', '0005_auto_20200926_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='interests',
            field=models.ManyToManyField(related_name='interested_students', to='GovernmentEmployee.Course'),
        ),
    ]
