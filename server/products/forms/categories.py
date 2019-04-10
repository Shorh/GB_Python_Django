from django import forms
from products.models import ProductCategory


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'description']
        widgets = {
            'name': forms.widgets.TextInput(
                attrs={'class': 'create_form_field'}
            ),
            'description': forms.widgets.Textarea(
                attrs={'class': 'create_form_field'}
            )
        }
