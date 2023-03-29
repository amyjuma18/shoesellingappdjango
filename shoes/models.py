from django.db import models

# Create your models here.
class Shoes(models.Model):
    shoes_name = models.CharField(max_length=100)
    shoes_image = models.URLField()
    shoes_price = models.CharField(max_length=1000000)
    class Meta:
        db_table = 'shoes'

class Adminshoe(models.Model):
    shoename = models.CharField(max_length=20)
    shoeimage = models.CharField(db_column='shoeimage', blank=False)
    shoeprice = models.CharField(db_column='shoeprice', max_length=200)
    class Meta:
        db_table = 'administration_shoe'
        verbose_name = 'Admin_shoe'
        verbose_name_plural = 'Admin_shoes'

    def __unicode__(self):
        return self.shoename
    def __str__(self):
        return self.shoename

class Checkout(models.Model):
    transactionID = models.CharField(db_column='transactionID', max_length=100, blank=False)
    pricetobepaid = models.CharField(db_column='pricetobepaid', max_length=100, blank=False)
    phone_number = models.CharField(db_column='phone_number', max_length=100, blank=False)
    class Meta:
        db_table = 'Check_out'
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'

    def __unicode__(self):
        return self.transactionID
    def __str__(self):
        return self.transactionID