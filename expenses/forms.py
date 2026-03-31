from django import forms
from .models import Expense

INPUT_CLASS = 'w-full border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400'

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'date', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'amount': forms.NumberInput(attrs={'class': INPUT_CLASS}),
            'category': forms.Select(attrs={'class': INPUT_CLASS}),
            'date': forms.DateInput(attrs={'class': INPUT_CLASS, 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 3}),
        }