from .models import Film
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ["name", "year", "description", "grade", "favorite"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название фильма'
            }),
            "year": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год выпуска'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание фильма'
            }),
            "grade": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценка из 10'
            }),
            "favorite": CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
            })
        }
