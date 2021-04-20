from Teacher.models import Student
from django import forms

from TeacherEnroll.models import TeacherEnroll


class StudentEnrollForm(forms.ModelForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=TeacherEnroll.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Student
        fields = ['user', 'interests', 'is_enroll']
