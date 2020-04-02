from django import forms 
from .models import ClientsFile
  
class ClientsFileForm(forms.ModelForm):
    class Meta: 
        model = ClientsFile 
        fields = ['name', 'document']

