from django.shortcuts import render
from.models import Bank,Debt
from aromaapp.models import CustomersTable

# Create your views here.
def case(request):
     return render(request,"case.html")

def addFromBank(request):
     if request.method == "POST":
       bankName = request.POST["bankName"]
       iban = request.POST["iban"]
       title = request.POST["title"]
       price=request.POST["price"]
       description=request.POST["description"]
       customer=Bank.objects.create(bankName=bankName,ıban=iban,title=title,price=price,description=description)
       customer.save()
       return render(request,"addFromBank.html",{"error":f"Kayıt edildi !"})
     else:
          return render(request,"addFromBank.html")

def bankSee(request):
     banks=Bank.objects.all()
     context={
          "banks":banks
     }
     return render(request,"bankSee.html",context)

def addDebt(request):
     if request.method == "POST":
       namesurname = request.POST["namesurname"]
       price = request.POST["price"]
       debtType = request.POST["debtType"]
       description=request.POST["description"]
       if CustomersTable.objects.filter(namesurname=namesurname).exists():
          debts=Debt.objects.create(namesurname=namesurname,price=price,debtType=debtType,description=description)
          debts.save()
          return render(request,"addDebt.html",{"error":f"Borç Kaydedildi !"})
       else:
            return render(request,"addDebt.html",{"error":f"Borç Verdiğiniz kişi {namesurname} müşteriler tablonuzda görünmüyor."})

     else:
          
          return render(request,"addDebt.html")

def debtSee(request):
     debtss=Debt.objects.all()
     context={
          "debtss":debtss
     }
     return render(request,"debtSee.html",context)
