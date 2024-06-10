from django import forms
from .models import Feedback
from .models import Reserva

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['data_hora', 'numero_pessoas']