from django import forms
from .models import customers,product,mainamount,purchaser

class customersf(forms.ModelForm):
    class Meta:
        model=customers
        fields=['name','Phone_no','village']

class productf(forms.ModelForm):
    class Meta:
        model=product
        fields=['name','image','status']

class mainamountf(forms.ModelForm):
    class Meta:
        model=mainamount
        fields=['amount',]

class purchaserf(forms.ModelForm):
    class Meta:
        model=purchaser
        fields=['seller_name','product_name','rate','weight','w_amount','amount',]