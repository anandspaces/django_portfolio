# new
from django.forms import ModelForm
from .models import Audience


class AudienceForm(ModelForm):
    class Meta:
        model = Audience
        fields = '__all__'
        