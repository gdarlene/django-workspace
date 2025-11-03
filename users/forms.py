from . models import Person
from django import forms
# forms file

class PersonForm (forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"