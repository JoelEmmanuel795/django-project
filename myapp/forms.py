from django import forms

class DemoForm(forms.Form):
    name = forms.CharField(max_length=100)
