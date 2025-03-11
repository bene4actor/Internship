# forms.py
from django import forms

class InternshipForm(forms.Form):
    start_date = forms.DateField(label='Дата начала', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Дата окончания', widget=forms.DateInput(attrs={'type': 'date'}))
    full_name = forms.CharField(max_length=255, label='Полное имя')
    contact_info = forms.CharField(max_length=255, label='Контактная информация')
    email = forms.EmailField(label='Электронная почта')
