from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Ministry


class MinistryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MinistryForm, self).__init__(*args, **kwargs)
        for MinistryName in self.fields.keys():
            self.fields[MinistryName].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Ministry
        fields = ['MinistryName','MinisterName','Email']