from django.test import TestCase
from django.urls import reverse
from .models import ClubType, Product, Review
from django.contrib.auth.models User


# Create your tests here.
class ClubPypeTest(TestCase):
    def test_string(self):
        type=ClubType(clubtypename='latop')
        self.assertEqual(str(ClubType),type.clubtypename)

    def test_table(self):
        self.assertEqual(str(ClubType._meta.db_table),'clubtype')

class ProductTest(TestCase):
    def setUp(self):
        self.type=ClubType(clubtypename='tablet')
        self.prod=Product(productname='Ipad',clubtype=self.type, productprice=800.00)
    
    def test_string(self):
        self.assertEqual(str(self.prod),self.prod.productname)

    def test_type(self):
        self.assertEqual(str(self.prod.techtype),'tablet')
        
    def test_discount(self):
        self.assertEqual(self.prod.memeberDiscount(),40.00)

#test for views
class IndexText(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class GetProductsTest(TestCase):
    def setUp(self):
        self.u=User.objects.create(username='myUser')
        self.type=ClubType.objects.create(clubtypename='laptop')
        self.prod=Product.objects.create(productname='product1', clubtype=self.type,
        user=self.u,productprice=500.00,productentrydate='2019-04-02',
        productdescription="some kind of laptop")

    def test_product_detail_success(self):
        response=self.client.get(reverse('productdetail'), args=(self.prod.id))
        self.assertEqual(response.status_code, 200)

