# new
from django.forms import ModelForm, TextInput
from .models import Audience


class AudienceForm(ModelForm):
    class Meta:
        model = Audience
        fields = '__all__'
        widgets = {
            'name':TextInput(attrs={'class':'form-control'}),
            'email':TextInput(attrs={'class':'form-control'}),
            'message':TextInput(attrs={'class':'form-control'}),
        }