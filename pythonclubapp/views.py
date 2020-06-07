from django.shortcuts import render
from .models import ClubType, Product, Review
# Create your views here.
def index(request):
    return render(request, 'pythonclubapp/index.html')
    
def getTypes(request):
    types_list=ClubType.object.all()
    context={'types_list' : types_list}
    return render(request, 'ClubReviewApp/types.html', context=context)
    
