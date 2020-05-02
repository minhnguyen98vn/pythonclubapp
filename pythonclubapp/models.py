from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Clubtype(models.Model):
 clubtypename=models.CharField(max_length=255)
 clubdescription=models.TextField(null=True, blank=True)

 def _str_(self):
     return self.clubtypename
 class Meta():
     db_table='clubtype'
     verbose_name_plural='clubtypes'

class Product(models.Model):
    productname=models.CharField(max_length=255)
    clubtype=models.ForeignKey(Clubtype, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    productprice=models.DecimalField(max_digits=10, decimal_places=2)
    productentrydate=models.DateField()
    productURL=models.URLField(null=True, blank=True)

    def _str_(self):
        return self.productname

    def memberdiscount(self):
        discount=.05
        return float(self.productprice) * discount

    def discountedprice(self):
        discount=self.memberdiscount()
        return float(self.productprice)-discount

    class Meta:
        db_table='product'
        verbose_name_plural='products'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    product=models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user=models.ManyToManyField(User)
    rating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def _str_(self):
        return self.reviewtitle

    class Meta:
        db_table='review'
