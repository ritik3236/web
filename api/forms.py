from django import forms
from django.forms import ModelForm, widgets
from api.models import FileUpload


class TestForm(ModelForm):
    class Meta:
        model = FileUpload
        exclude = ['uploaded_at']
        widgets = {
            'document' :forms.ClearableFileInput(attrs={'multiple': True}),
            'name': forms.TextInput(attrs={'placeholder': 'Your Name... '}),
            'email': forms.TextInput(attrs={'placeholder': 'Your Email... '}),
            'description': forms.Textarea(attrs={'rows': 3 , 'placeholder': 'Provide some information about file/doubt... '}),
        }