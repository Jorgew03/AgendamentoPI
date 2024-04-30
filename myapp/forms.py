from django import forms
from .models import Client, Item, RegisterReservation

## Cadastra Cliente          
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']
       
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'


## Registra Reserva do item   
class RegisterReservationForm(forms.ModelForm):
    # booking_date = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date',}))
    # booking_date = forms.DateTimeField(
    #     input_formats=['%d-%m-%Y %H:%M'], 
    #     widget=forms.DateTimeInput(attrs={
    #         'type': 'datetime-local',
    #         'format': '%d-%m-%Y %H:%M'
    #     }),
    # )
    booking_date = forms.DateField(
        input_formats=['%d-%m-%Y'], 
        widget=forms.DateInput(attrs={
            'type': 'date',
            'format': '%d-%m-%Y'
        }),
    )
    booking_time = forms.TimeField(
        input_formats=['%H:%M'], 
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'format': '%H:%M'
        }),
    )

    class Meta:
        model = RegisterReservation
        fields = '__all__'
        exclude = ('item','create_at')
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'