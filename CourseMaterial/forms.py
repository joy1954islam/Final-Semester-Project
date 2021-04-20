from django import forms
from CourseMaterial.models import CourseMaterial
from django.contrib.auth import get_user_model
User = get_user_model()


class CourseMaterialForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourseMaterialForm, self).__init__(*args, **kwargs)
        for CourseName in self.fields.keys():
            self.fields[CourseName].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = CourseMaterial
        fields = ['CourseName', 'MaterialName']