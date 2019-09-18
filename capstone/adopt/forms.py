from django import forms
from .models import Adopt

class AdoptForm(forms.ModelForm):

    class Meta:
        model = Adopt
        fields = (
            'name', 'breed', 'description', 'image',
            'years_old', 'location', 
            # 'posted_by',
        )