from django import forms
from . models import Trainer

class TrainerCreationForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name','address','image','email','contact']