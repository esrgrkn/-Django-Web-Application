from django.contrib import admin
from.models import CustomersTable,ProductTable,Price,Kilogram


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    
    list_display=(
     'pk',
     'namesurname',
     'tc',)

    list_editable=(
     'namesurname',
     'tc',
    )

class ProductsAdmin(admin.ModelAdmin):
   
    list_display=(
     'pk',
     'namesurname',
     'adet',
     'daralı',
     'safi',)
    
    list_editable=(
     
     'namesurname',
     'adet',
     'daralı',
     'safi',
    )


class PriceAdmin(admin.ModelAdmin):
   
    list_display=(
     'pk',
     'price'
    )

class KilogramAdmin(admin.ModelAdmin):
   
    list_display=(
     'pk',
     'kilo'
    )
    
   


admin.site.register(CustomersTable,CustomerAdmin)
admin.site.register(ProductTable,ProductsAdmin)
admin.site.register(Price,PriceAdmin)
admin.site.register(Kilogram,KilogramAdmin)