from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from PIL import Image
# Create your models here.


class Course(models.Model):
    CourseName = models.CharField(max_length=150)
    Description = models.TextField()
    picture = models.ImageField(default='default.jpg', upload_to='Course_Pic/')
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.CourseName

    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)




