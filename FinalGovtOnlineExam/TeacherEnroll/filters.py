
import django_filters
from TeacherEnroll.models import TeacherEnroll


class CourseAssignFilter(django_filters.FilterSet):
    Batch = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TeacherEnroll
        fields = ['Batch','CourseName']