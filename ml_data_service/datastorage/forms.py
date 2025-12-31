from django.forms import ModelForm
from .models import Observation


class ObservationForm(ModelForm):

    class Meta:
        model = Observation
        fields = ('feature0', 'feature1', 'category',)


class PredictionForm(ModelForm):
    class Meta:
        model = Observation
        fields = ('feature0', 'feature1',)

