from django import forms
from .models import BooK,Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),

        }


class BookForm(forms.ModelForm):
    class Meta:
        model = BooK
        fields = [
            'title',
            'auther',
            'photo_book',
            'photo_auther',
            'pages',
            'price',
            'retal_price',
            'retal_period',
            'total_retal',
            'active',
            'status',
            'category',

        ]

        widgets = {

            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'auther': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_book': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_auther': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'retal_price': forms.NumberInput(attrs={'class': 'form-control', 'id':'retal_price'}),
            'retal_period': forms.NumberInput(attrs={'class': 'form-control', 'id':'retal_period'}),
            'total_retal': forms.NumberInput(attrs={'class': 'form-control', 'id': 'total_retal'}),
            #'active': forms.BooleanField(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),

        }
