from django import forms
from django.contrib.auth.models import User

from GovernmentEmployee.models import Course, CourseContent


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



