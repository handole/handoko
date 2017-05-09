from django import forms

from .models import Portofol

class PortoForm(forms.ModelForm):
    class Meta:
        model = Portofol
        fields = [
            "title",
            "content",
            "image",
        ]
