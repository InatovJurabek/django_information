from django import forms
from .models import New

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['title', 'image', 'content', 'category']


             