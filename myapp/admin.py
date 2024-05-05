from django.contrib import admin
from myapp.models import Item, ItemImage, RegisterReservation

# Register your models here.
admin.site.register(RegisterReservation)

class ItemImageInlineAdmin(admin.TabularInline):
    model = ItemImage
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInlineAdmin]

admin.site.register(Item, ItemAdmin)