from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ministry
from django.conf import settings
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


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


# class UserUpdateForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(UserUpdateForm, self).__init__(*args, **kwargs)
#         for username in self.fields.keys():
#             self.fields[username].widget.attrs.update({
#                 'class': 'form-control',
#             })
#
#     class Meta:
#         model = User
#         fields = ['username','email','first_name','last_name',]


class GovtSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','MinistryName', 'password1', 'password2']
            # settings.SIGN_UP_FIELDS

    email = forms.EmailField(label=_('Email'), help_text=_('Required. Enter an existing email address.'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_governmentEmployee = True
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))

        return email