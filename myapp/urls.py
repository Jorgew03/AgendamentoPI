from django.urls import path 
from myapp import views

urlpatterns = [
    path('', views.list_item, name='list-item'),

    # #Versão anterior 
    path('form-reservation/<int:id>/', views.form_reservation, name='reservation-create'),

    # Versão 02-05-2024
    #path('reservation-create/<int:id>/', views.reservation_create, name='reservation-create'),

 ]