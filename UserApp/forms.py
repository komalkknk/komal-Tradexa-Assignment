from django import forms
from .models import usermodel,postmodel


class usermodelFrom(forms.ModelForm):
    class Meta:
        model = usermodel
        fields = '__all__'


class postform(forms.ModelForm):
    class Meta:
        model=postmodel
        fields=['text']