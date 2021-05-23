from django import forms
from django.forms import ModelForm, widgets
from home.models import FileUpload


class TestForm(ModelForm):
    class Meta:
        model = FileUpload
        exclude = ['uploaded_at']
        widgets = {
            'document' :forms.ClearableFileInput(attrs={'multiple': True})
        }