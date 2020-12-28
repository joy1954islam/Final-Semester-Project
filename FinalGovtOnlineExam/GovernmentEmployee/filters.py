import django_filters

from CourseMaterial.models import CourseMaterial
from Teacher.models import Student
from TeacherEnroll.models import TeacherEnroll
from django import forms


class CourseMaterialApprovedFilter(django_filters.FilterSet):
    # Batch = django_filters.CharFilter(lookup_expr='icontains')
    # interests = django_filters.ModelMultipleChoiceFilter(queryset=TeacherEnroll.objects.all(),
    #                                                         widget=forms.CheckboxSelectMultiple
    #                                                         )

    class Meta:
        model = CourseMaterial
        fields = ['CourseName']