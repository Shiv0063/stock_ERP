from django.test import TestCase
from .models import customers,product,mainamount,purchaser
# Create your tests here.
def pro():
    pl=[]
    prod=product.objects.all()
    for i in prod:
        pl.append(i.name)
        
    return pl