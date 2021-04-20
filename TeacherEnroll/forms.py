from django import forms

from django.contrib.auth import get_user_model
from django.forms import CheckboxInput

from GovernmentEmployee.models import Course
from TeacherEnroll.models import TeacherEnroll

User = get_user_model()


class TeacherEnrollForm(forms.ModelForm):
    CourseStartDate = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    # def __init__(self, *args, **kwargs):
    #     super(TeacherEnrollForm, self).__init__(*args, **kwargs)
    #     for Batch in self.fields.keys():
    #         self.fields[Batch].widget.attrs.update({
    #             'class': 'form-control',
    #         })

    class Meta:
        model = TeacherEnroll
        fields = ['Batch', 'CourseName', 'TeacherName', 'CourseStartDate', 'CourseDuration', 'is_publish']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['TeacherName'].queryset = User.objects.none()
    #
    #     if 'TeacherName' in self.data:
    #         self.fields['TeacherName'].queryset = User.objects.all()
    #
    #     elif self.instance.pk:
    #         self.fields['TeacherName'].queryset = User.objects.all().filter(pk=self.instance.TeacherName.pk)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['CourseName'].queryset = Course.objects.filter(id=24)

    # def __init__(self, user, *args, **kwargs):  # Limits inside_room choices to same building only
    #     super(TeacherEnrollForm, self).__init__(*args, **kwargs)
    #     self.fields['CourseName'].queryset = TeacherEnroll.objects.filter(CourseName__username = user)


class TeacherCourseAssignForm(forms.ModelForm):
    CourseStartDate = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    class Meta:
        model = TeacherEnroll
        fields = ['Batch', 'CourseName', 'TeacherName', 'CourseStartDate', 'CourseDuration', 'is_publish']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['TeacherName'].queryset = User.objects.none()

        if 'TeacherName' in self.data:
            # teacher = User.objects.all().filter(is_trainer=True)
            self.fields['TeacherName'].queryset = User.objects.all().filter(is_trainer=True)

        elif self.instance.pk:
            self.fields['TeacherName'].queryset = User.objects.all().filter(pk=self.instance.TeacherName.pk)


