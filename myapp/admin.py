from django.contrib import admin
from myapp import models

# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.RegisterReservation)

class ItemImageInlineAdmin(admin.TabularInline):
    model = models.ItemImage
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInlineAdmin]

admin.site.register(models.Item, ItemAdmin)