from django import forms


class TestForm(forms.Form):
    f_name = forms.CharField()
    m_name = forms.CharField(required=False)
    l_name = forms.CharField()
    email = forms.EmailField()
    # dob = forms.DateField(input_formats= '%d-%m-%y')
    Address = forms.CharField(widget=forms.Textarea)
    gender = forms.ChoiceField(choices=(('1', 'Male'),('2', 'Female')))
