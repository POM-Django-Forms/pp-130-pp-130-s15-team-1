from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['book', 'user', 'plated_end_at', 'end_at']
