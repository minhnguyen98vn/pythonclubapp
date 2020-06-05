from django import forms
from .models import ClubType, Product, Review

class ProductForm(forms.ModelForm):
    model=Product
    class Meta:
        fields='_all_'

class ReviewForm(Form.ModelForm):
    class Meta:
        model=Review
        fields='_all_'