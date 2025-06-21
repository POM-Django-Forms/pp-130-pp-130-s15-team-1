from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'middle_name', 'last_name', 'password', 'role']

    def clean_email(self):
        email = self.cleaned_data['email']
        existing = CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk)
        if existing.exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if self.instance.pk is None and not password:
            raise forms.ValidationError("Password is required.")
        return password
