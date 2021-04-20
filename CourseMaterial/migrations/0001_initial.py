# Generated by Django 3.1.1 on 2020-09-21 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TeacherEnroll', '0004_auto_20200920_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaterialName', models.CharField(max_length=100)),
                ('is_material_status', models.BooleanField(default=False)),
                ('CourseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeacherEnroll.teacherenroll')),
                ('username', models.ForeignKey(limit_choices_to={'is_trainer': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]