from django import forms

import Persons
from shoes.models import shoes
class shoesForm(forms.ModelForm):
    class Meta:
        model = shoes
        fields = "__all__"



class PersonsForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = "__all__"

