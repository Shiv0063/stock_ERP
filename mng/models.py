from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.

class customers(models.Model):
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    Phone_no = models.IntegerField()
    status = models.IntegerField(default=0)

    
class product(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='',null=True,blank=True)
    status = models.IntegerField(default=0)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

class mainamount(models.Model):
    date = models.DateTimeField(default=datetime.now())
    amount = models.IntegerField()
    status = models.IntegerField(default=0)

    def dateamount(self):
        return self.date.strftime('%B %d %Y')

class purchaser(models.Model):
    date = models.DateTimeField(default=datetime.now())
    seller_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)
    weight = models.CharField(max_length=100)
    w_amount = models.IntegerField()
    amount = models.IntegerField()
    status = models.IntegerField(default=0)


    def datepurchas(self):
        return self.date.strftime('%B %d %Y')

    def daypurchas(self):
        return self.date.strftime('%A')

class sales(models.Model):
    date = models.DateTimeField(default=datetime.now())
    purchaser_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)
    weight = models.CharField(max_length=100)
    w_amount = models.IntegerField()
    amount = models.IntegerField()
    status = models.IntegerField(default=1)


    def datesales(self):
        return self.date.strftime('%B %d %Y')

    def daysales(self):
        return self.date.strftime('%A')


class expenses(models.Model):
    exdate = models.DateTimeField(default=datetime.now())
    exname = models.CharField(max_length=100)
    examount = models.IntegerField()
    expstatus = models.IntegerField(default=0)

    def expdate(self):
        return self.exdate.strftime('%B %d %Y')

    def expday(self):
        return self.exdate.strftime('%A')

    def exptime(self):
        return self.exdate.strftime('%H %M %S')

class dailystatus(models.Model):
    date = models.DateTimeField(default=datetime.now())
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    status = models.IntegerField(default=0)
    bkamount = models.IntegerField()
    
    def datdaily(self):
        return self.date.strftime('%B %d %Y')

    def daydaily(self):
        return self.date.strftime('%A')

class stock(models.Model):
    product_name = models.CharField(max_length=100)
    w_amount = models.IntegerField()
    amount = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)

class salesdt(models.Model):
    date = models.DateTimeField(default=datetime.now())
    purchaser_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    old_rate = models.IntegerField(default=0)
    old_amount = models.IntegerField()
    new_rate = models.IntegerField(default=0)
    new_amount = models.IntegerField()
    profit = models.IntegerField(default=0)
    weight = models.CharField(max_length=100)
    w_amount = models.IntegerField()
    status = models.IntegerField(default=0)


    def datesales(self):
        return self.date.strftime('%B %d %Y')

    def daysales(self):
        return self.date.strftime('%A')