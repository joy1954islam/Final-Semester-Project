from django import forms

from django.contrib.auth import get_user_model

from TeacherEnroll.models import TeacherEnroll

User = get_user_model()


class TeacherEnrollForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeacherEnrollForm, self).__init__(*args, **kwargs)
        for TeacherName in self.fields.keys():
            self.fields[TeacherName].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = TeacherEnroll
        fields = ['TeacherName','CourseName',]

