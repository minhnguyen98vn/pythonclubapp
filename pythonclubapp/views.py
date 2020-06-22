from django.shortcuts import render, get_object_or_404
from .models import ClubType, Product, Review
# Create your views here.
def index(request):
    return render(request, 'pythonclubapp/index.html')
    
def getTypes(request):
    types_list=ClubType.object.all()
    context={'types_list' : types_list}
    return render(request, 'ClubReviewApp/types.html', context=context)

def getProducts(request):
    product_list=Product.objects.all()
    return render(request, 'ClubReviewApp/products.html',{'product_list' : product_list} ) 

def productDetail(request, id):
    prod=Product.objects.get(pk=id)
    reviewcount=Review.objects.filter(product_id).count()
    review=Review.object.filter(product=id)
    context={
            'prod' : prod,
            'reviewcount' : reviewcount,
            'reviews':review, 
    }
    return render (request, 'ClubReviewApp/productdetail.html', context=context)
