from django.shortcuts import render, redirect

from myapp.forms import ClientForm, RegisterReservationForm
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


def form_reservation(request, id):

    get_item = Item.objects.get(id=id) ## filtra objeto
    form = RegisterReservationForm(request.POST or None)  
    client_form = ClientForm(request.POST or None) # Inserção do Formulário de Clientes
    if request.method == 'POST':
        form = RegisterReservationForm(request.POST)
        if form.is_valid() and client_form.is_valid():
            reservation_form = form.save(commit=False)
            reservation_form.item = get_item ## salva id do item 
            reservation_form.save() 

            client_form.save() 

            ## muda status do item como "Reservado"
            itm = Item.objects.get(id=id)
            itm.is_reserved = True ## passa ser True
            itm.save() 

            return redirect('list-item') # Retorna para lista
    context = {'form': form, 'client_form': client_form,'reservation': get_item}
    return render(request, 'form-reservation.html', context)