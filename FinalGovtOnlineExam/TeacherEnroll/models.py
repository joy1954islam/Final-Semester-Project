from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
# Create your models here.
from django.urls import reverse
from django.utils import timezone
from GovernmentEmployee.models import Course


class TeacherEnroll(models.Model):

    TeacherName = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    limit_choices_to={'is_trainer': True}, )
    CourseName = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}'.format(self.TeacherName)


