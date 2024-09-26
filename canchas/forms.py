from django import forms
from .models import Usuario, Reserva

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'cancha', 'hora_inicio', 'hora_fin']
