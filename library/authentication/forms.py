from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'middle_name', 'last_name', 'password', 'role']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if self.instance.pk is None and not password:
            raise forms.ValidationError("Password is required.")
        return password
