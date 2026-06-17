from django import forms
from .models import UserCar

class UserCarForm(forms.ModelForm):
    class Meta:
        model = UserCar
        fields = ['car_base', 'engine', 'year','fuel_type', 'stage', 'specs',]
        
        widgets = {
            'specs': forms.Textarea(attrs={'rows': 3, 'placeholder': 'for example: Downpipe, intercooler, ECU tune Stage 2...'}),
        }