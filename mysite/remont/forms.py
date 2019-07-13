from django import forms
from .models import *

class VisitorsForm(forms.ModelForm):
    class Meta:
        model = Visitors
        exclude = [""]