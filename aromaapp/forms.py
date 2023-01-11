from django import forms
from django.forms import  widgets
from .models import CustomersTable,ProductTable


class CustomersForm(forms.ModelForm):
    class Meta:
        model = CustomersTable
        fields = ('namesurname','tc','phoneNum')
        error_messages = {
            "namesurname": {
                "required": "name gerekli alan...",
                "max_length": "maksimum 50 karakter girmelisiniz."
            }
        }
        labels = {
            
            "namesurname": "Adı Soyadı",
            "tc": "TC Kimlik no",
            "phoneNum": "Daralı ağırlık"
        }
        widgets = {
            
            "namesurname": widgets.TextInput(attrs={"class":"form-control"}),
            "tc": widgets.NumberInput(attrs={"class":"form-control"}),
            "phoneNum": widgets.TextInput(attrs={"class":"form-control"}),
            
        }


class ProductsForm(forms.ModelForm):
    class Meta:
        model = ProductTable
        fields = ('namesurname','adet','daralı')
        error_messages = {
            "namesurname": {
               
                "max_length": "maksimum 50 karakter girmelisiniz."
            }
        }
        labels = {
            
            "namesurname": "Adı Soyadı",
            "adet": "Adet",
            "daralı": "Daralı Ağırlık"
        }
        widgets = {
            
            "namesurname": widgets.TextInput(attrs={"class":"form-control"}),
            "adet": widgets.NumberInput(attrs={"class":"form-control"}),
            "daralı": widgets.NumberInput(attrs={"class":"form-control"}),
            
        }

from django import forms



class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = CustomersTable
        fields = ('customerImage',)


