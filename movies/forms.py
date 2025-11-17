from django import forms
from .models import Movie, Review
from django.core.exceptions import ValidationError

class MovieForm(forms.ModelForm):
    description = forms.CharField(min_length=5)
    name = forms.CharField(min_length=2)
    year = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
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
        if name is not None and name[0].islower():
            raise ValidationError({
                "description": "Название должно начинаться с большой буквы"
            })
        if description is not None and description[0].islower():
            raise ValidationError({
                "description": "Описание должно начинаться с большой буквы"
            })

        return cleaned_data


class ReviewForm(forms.ModelForm):
    # description = forms.CharField(min_length=5)
    # name = forms.CharField(min_length=2)
    # year = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Review
        fields = [
            'title',
            'text',
            'grade',
        ]
    def clean(self):
        cleaned_data=super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')
        grade = cleaned_data.get('grade')
        if title == text:
            raise ValidationError({
                "text": "Название не может совпадать с описанием"
            })
        if title is not None and title[0].islower():
            raise ValidationError({
                "text": "Название должно начинаться с большой буквы"
            })
        if text is not None and text[0].islower():
            raise ValidationError({
                "text": "Описание должно начинаться с большой буквы"
            })
        if 10 > grade < 0:
            raise ValidationError({
                "grade": "Оценка должна быть между 0 и 10"
            })

        return cleaned_data
