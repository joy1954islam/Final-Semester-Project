from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from GovernmentEmployee.models import Course, CourseContent
from django.contrib.auth import get_user_model
User = get_user_model()


class CourseForm(forms.ModelForm):
    CourseStartDate = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date"}))

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
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for CourseCode in self.fields.keys():
            self.fields[CourseCode].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Course
        fields = ['CourseCode','CourseName', 'CourseStartDate','CourseDuration','picture']


class CourseContentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourseContentForm, self).__init__(*args, **kwargs)
        for CourseName in self.fields.keys():
            self.fields[CourseName].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = CourseContent
        fields = ['CourseName', 'TopicName']


# Teacher SignUpForm
class TeacherSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = settings.SIGN_UP_FIELDS

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