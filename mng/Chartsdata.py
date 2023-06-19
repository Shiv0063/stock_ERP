from .models import customers,product,mainamount,purchaser
from .form import customersf,productf,mainamountf,purchaserf
from django.db.models import Max
from django.contrib import messages


def value():
    pdata=purchaser.objects.all()
    prod=product.objects.get(id=2)

def pro():
    pl=[]
    prod=product.objects.all()
    for i in prod:
        pl.append(i.name)
        
    return pl

