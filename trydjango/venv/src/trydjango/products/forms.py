from django import forms

from .models import Product

class Product_add_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'desc',
            'price'
        ]
    
    def clean_title(self, *args,**kargs):
        my_title = self.cleaned_data.get('title')
        if my_title == '123':
            raise forms.ValidationError('this is not good title')
        else:
            return my_title
