# Generated by Django 3.1.1 on 2020-09-26 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CourseMaterial', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadLecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video', models.FileField(blank=True, default=True, null=True, upload_to='Videos/')),
                ('Pdf', models.FileField(blank=True, default=True, null=True, upload_to='PDF/')),
                ('Image', models.FileField(blank=True, default=True, null=True, upload_to='Image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('MaterialName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CourseMaterial.coursematerial')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
