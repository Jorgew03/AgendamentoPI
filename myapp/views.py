from django.shortcuts import render, redirect
#from django.utils import timezone

from myapp.forms import RegisterReservationForm
from .models import Item



def list_item(request):
    items = Item.objects.filter(is_reserved=False)
    context = {
        'items': items
    }
    return render(request, 'list-item.html', context)


def form_reservation(request, id):
    get_item = Item.objects.get(id=id)
    form = RegisterReservationForm()
    if request.method == 'POST': 
        form = RegisterReservationForm(request.POST)
        if form.is_valid():
            reservation_form = form.save(commit=False)
            reservation_form.item = get_item
            reservation_form.save()
            
            itm = Item.objects.get(id=id)
            itm.is_reserved = True ## passa ser True
            itm.save() 
            
            return redirect('list-item')

    context = {'form': form, 'reservation': get_item}
    return render(request, 'form-reservation.html', context)