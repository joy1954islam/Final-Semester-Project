from django.db import models
from django.conf import settings

# Create your models here.
from TeacherEnroll.models import TeacherEnroll


class CourseMaterial(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                 limit_choices_to={'is_trainer': True}, )
    CourseName = models.ForeignKey(TeacherEnroll, on_delete=models.CASCADE)
    MaterialName = models.CharField(max_length=100)
    is_material_status = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.MaterialName)
