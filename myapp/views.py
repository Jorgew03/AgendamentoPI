from django.shortcuts import render
from .models import Item

# # Create your views here.
# def mysite(request):
#     return render(request, 'index.html')

def list_item(request):
    items = Item.objects.filter(is_reserved=False)
    context = {
        'items': items
    }
    return render(request, 'list-item.html', context)