from django import forms
from .models import Item


class CreateToDoItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'details', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


class UpdateToDoItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'details', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
