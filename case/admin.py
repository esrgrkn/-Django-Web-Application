from django.contrib import admin
from .models import Bank,Debt



class BankAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("bankName",)}
    list_display=(
     'pk',
     'bankName',
     'title',
     'price',
     'transactionDate')
    
    list_editable=(
     
     'bankName',
     'title',
     'price',
     
    )


class DebtAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("namesurname",)}
    list_display=(
     'pk',
     'namesurname',
     'price',
     'debtType',
     'description')
    
    list_editable=(
     
     'namesurname',
     'price',
     'debtType',
     'description'
     
    )

admin.site.register(Bank,BankAdmin)
admin.site.register(Debt,DebtAdmin)
