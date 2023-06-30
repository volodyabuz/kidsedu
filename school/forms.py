from django import forms
from .models import *
from django.core.exceptions import ValidationError

class AddPostForm(forms.ModelForm):
    class Meta:
        model = PhotoEducations
        fields = ['name_edu', 'slug', 'photo']
        widgets = {
            'name_edu': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
        }

    def clean_name_edu(self):
        name_edu = self.cleaned_data['name_edu']
        if len(name_edu) > 30:
            raise ValidationError('Длина больше 30 символов')
        return name_edu
