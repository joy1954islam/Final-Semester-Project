from django.db import models
from django.conf import settings
# Create your models here.


class Education(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    Institute_name = models.CharField('Institute Name ', max_length=100, null=True, blank=True)
    degree = models.CharField('Degree', max_length=100, null=True, blank=True)
    result = models.FloatField('Result', null=True, blank=True)
    Major = models.CharField('Major', max_length=100, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_student = models.BooleanField('I currently study here', default=False)
    Description = models.TextField(null=True, blank=True)
