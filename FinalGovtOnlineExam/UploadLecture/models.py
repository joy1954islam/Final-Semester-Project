from django.conf import settings
from django.db import models

# Create your models here.
from CourseMaterial.models import CourseMaterial


class UploadLecture(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                 limit_choices_to={'is_trainer': True},)
    MaterialName = models.ForeignKey(CourseMaterial,on_delete=models.CASCADE)
    Video = models.URLField(max_length=300, null=True, blank=True)
    Pdf = models.FileField(upload_to='PDF/',  null=True, blank=True)
    Text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.MaterialName)