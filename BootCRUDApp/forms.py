from django import forms
from .models import ItemModel


# Item model bound form
class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemModel
        fields = '__all__'
