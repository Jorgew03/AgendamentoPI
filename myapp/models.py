from django.db import models
from datetime import datetime, timedelta
# Create your models here.
## Cadastro de Clientes     
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return "{} - {}".format(self.name, self.email)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-id']

## Opções de Imóveis
class TypeItem(models.TextChoices):
    BLOUSE = 'BLUSA','BLUSA'
    PANTS = 'CALCA','CALCA'
    HANDBAG = 'BOLSA','BOLSA'
    DRESS = 'VESTIDO', 'VESTIDO'
    TSHIRT = 'CAMISETA', 'CAMISETA'

## Cadastro de Imóveis
class Item(models.Model):
    code = models.CharField(max_length=100)
    type_item = models.CharField(max_length=100, choices=TypeItem.choices)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    is_reserved = models.BooleanField(default=False)
    
    
    def __str__(self):
        return "{} - {}".format(self.code, self.type_item)
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering = ['-id']

## Cadastrar as Imagens do Imóvel
class ItemImage(models.Model):
    image = models.ImageField('Images',upload_to='images')
    item = models.ForeignKey(Item, related_name='item_images', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item.code # form key
    
# Registrar Reserva - adaptação original
class RegisterReservation(models.Model):
        item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reg_reservation')
        client = models.ForeignKey(Client, on_delete=models.CASCADE)
        booking_date = models.DateTimeField('Data')
        create_at = models.DateField(default=datetime.now, blank=True)
    
        def __str__(self):
            return "{} - {}".format(self.client, self.item)
    
        class Meta:
            verbose_name = 'Registrar Reserva'
            verbose_name_plural = 'Registrar Reservas'
            ordering = ['-id']