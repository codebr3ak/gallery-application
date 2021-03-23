from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Category,Location

# Create your views here.
def welcome(request):
    images = Image.get_all_images()
    categories = Category.objects.all()
    location = Location.objects.all()
    return render(request,'welcome.html',{"images":images, 'categories':categories,'locations':location})

def search_image(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'Image' in request.GET and request.GET['Image']:
        search_term = request.GET.get('image-search')
        found_results = Image.get_image_by_cat(search_category)
        message = f'{search_term}'

        return render(request, 'search.html',{'found_results':found_results,'message':message,'categories':categories,'locations':locations})

    else:
        return render(request,'search.html')