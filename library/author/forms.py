# forms.py
from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']

        labels = {
            'name': 'First Name',
            'surname': 'Last Name',
            'patronymic': 'Patronymic (Middle Name)',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'patronymic': forms.TextInput(attrs={'placeholder': 'Enter patronymic'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        for field in ['name', 'surname', 'patronymic']:
            value = cleaned_data.get(field)
            if value and len(value) > 20:
                self.add_error(field, "Maximum length is 20 characters.")
        return cleaned_data
