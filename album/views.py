from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Category,Location

# Create your views here.
def welcome(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    location = Location.objects.all()
    return render(request,'welcome.html',{"images":images, 'categories':categories,'locations':location})

def search_image(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        found_results = Image.get_image_by_cat(search_term)
        message = f"{search_term}"
        print(found_results)

        return render(request, 'search.html',
                    {'found_results': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
        message = 'You havent searched yet'
        return render(request, 'search.html',{"message": message})

def category(request):
    categories = Image.get_all_images()
    return render(request, 'category.html', {"categories": categories})