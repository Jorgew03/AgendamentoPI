from django.urls import path 
from myapp import views

# urlpatterns = [
#     path('', views.mysite, name='mysite'), 
# ]

from django.urls import path 
from myapp import views

urlpatterns = [
    path('', views.list_item, name='list-item'),

    path('form-reservation/<int:id>/', views.form_reservation, name='reservation-create')
 ]