# Generated by Django 3.1.1 on 2020-09-10 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Email_Address', models.EmailField(max_length=254)),
                ('Phone_number', models.CharField(max_length=15)),
                ('Message', models.TextField()),
            ],
        ),
    ]