from django import forms
from UploadLecture.models import UploadLecture


class UploadLectureForm(forms.ModelForm):
    Video = forms.URLField(required=False)
    Pdf = forms.FileField(required=False)
    Text = forms.Textarea()

    class Meta:
        model = UploadLecture
        fields = ('MaterialName','Video', 'Pdf', 'Text',)
