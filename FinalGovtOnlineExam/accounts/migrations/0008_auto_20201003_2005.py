# Generated by Django 3.1.1 on 2020-10-03 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SuperAdmin', '0001_initial'),
        ('accounts', '0007_auto_20200922_0814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='MinistryName',
        ),
        migrations.AddField(
            model_name='user',
            name='MinistryName',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='SuperAdmin.ministry'),
            preserve_default=False,
        ),
    ]
