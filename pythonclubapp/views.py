from django.shortcuts import render, get_object_or_404
from .models import Clubtype, Product, Review
from .forms import ProductForm,ReviewForm
from django.contrib.auth.decorators import login_required


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
@login_required
def newProduct(request):
    form=ProductForm
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ProductForm()
        else:
            form=ProductForm
        return render(request, 'ClubReviewApp/newproduct.html', {'form' :form})

@login_required
def newReview(request):
    form=ReviewForm
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
        else:
            form=ReviewForm
        return render(request, 'ClubReviewApp/newproduct.html', {'form' :form})

def loginMessage(request)
return render(request, 'ClubReviewApp/loginmessage.html')

def logoutMessage(request)
return render(request, 'ClubReviewApp/logoutmessage.html')
