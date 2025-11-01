from django import forms
from .models import Movie
from django.core.exceptions import ValidationError

class MovieForm(forms.ModelForm):
    description = forms.CharField(min_length=5)
    name = forms.CharField(min_length=2)
    class Meta:
        model = Movie
        fields = [
            'name',
            'description',
            'year',
            'poster',
            'type',
            'category',
        ]
    def clean(self):
        cleaned_data=super().clean()
        name=cleaned_data.get('name')
        description = cleaned_data.get('description')
        if name == description:
            raise ValidationError({
                "description": "Название не может совпадать с описанием"
            })
        if name in not None and name[0].islower():
            raise ValidationError({
                "description": "Название должно начинаться с большой буквы"
            })
        if description in not None and description[0].islower():
            raise ValidationError({
                "description": "Описание должно начинаться с большой буквы"
            })

        return cleaned_data

