from django.forms import ModelForm
from .models import Usuarios
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
    
