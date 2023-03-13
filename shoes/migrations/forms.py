from django import forms
from shoes.models import shoes
class shoesForm(forms.ModelForm):
    class Meta:
        model = shoes
        fields = "__all__"
