from django.contrib import admin

# Register your models here.
from GovernmentEmployee.models import Course,CourseContent

admin.site.register(Course)
admin.site.register(CourseContent)