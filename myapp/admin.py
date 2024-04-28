from django.contrib import admin
from myapp.models import Item, RegisterReservation, ItemImage, Client

# Register your models here.
# admin.site.register(models.Client)
# admin.site.register(models.RegisterReservation)

class ItemImageInlineAdmin(admin.TabularInline):
    model = ItemImage
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInlineAdmin]

admin.site.register(Item, ItemAdmin)

class ClientAdmin(admin.StackedInline):  
    model = Client  
    extra = 0 

@admin.register(RegisterReservation)
class RegisterReservationAdmin(admin.ModelAdmin):
    inlines = [ClientAdmin]