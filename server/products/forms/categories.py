from django import forms
from products.models import ProductCategory


# class CategoryForm(forms.Form):
#     name = forms.CharField(
#         max_length=255,
#         widget=forms.widgets.TextInput(
#             attrs={'class': 'create_form_field'}
#         )
#     )
#     description = forms.CharField(
#         required=False,
#         widget=forms.widgets.Textarea(
#             attrs={'class': 'create_form_field'}
#         )
#     )


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
