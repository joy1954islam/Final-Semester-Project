from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.db import transaction
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

from CourseMaterial.models import CourseMaterial
from GovernmentEmployee.models import Course
from django.contrib.auth import get_user_model

from SuperAdmin.models import Ministry
from Teacher.models import Student
from TeacherEnroll.models import TeacherEnroll

User = get_user_model()


class CourseForm(forms.ModelForm):
    # CourseStartDate = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

    # or
    # publication_date = forms.CharField(widget=forms.widgets.DateInput(attrs={"type": "date"}))
    #
    # publication_date = forms.DateField(
    # label='What is your publication date?',
    # # change the range of the years from 1980 to currentYear
    # widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year))
    # )

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        for CourseName in self.fields.keys():
            self.fields[CourseName].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Course
        fields = ['CourseName','Description','picture']


class CourseMaterialForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourseMaterialForm, self).__init__(*args, **kwargs)
        for CourseName in self.fields.keys():
            self.fields[CourseName].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = CourseMaterial
        fields = ['CourseName', 'MaterialName','is_material_status']


# Teacher SignUpForm
class TeacherSignUpForm(UserCreationForm):
    # MinistryName = forms.ModelMultipleChoiceField(queryset=Ministry.objects.all(),
    #                                widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    email = forms.EmailField(label=_('Email'), help_text=_('Required. Enter an existing email address.'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_trainer = True
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))

        return email


# class StudentEnrollForm(forms.ModelForm):
#     interests = forms.ModelMultipleChoiceField(
#         queryset=TeacherEnroll.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True
#     )
#
#     class Meta:
#         model = Student
#         fields = ['user','interests','is_enroll']


# Student SignUpForm
class StudentSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=TeacherEnroll.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = settings.SIGN_UP_FIELDS

    email = forms.EmailField(label=_('Email'), help_text=_('Required. Enter an existing email address.'))

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        # if commit:
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))

        return email
