from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from .models import CustomersTable,ProductTable,Price,Kilogram,Company,Paids
from. forms import CustomersForm,ProductsForm,ImageForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg,Count,Max,Min,Sum



         
 


@login_required(login_url='login_request')
def home(request): 
     return render(request,"anasayfa.html")

def custsomerAdd(request):
     if request.method == "POST":
       namesurname = request.POST["namesurname"]
       tc = request.POST["tc"]
       phoneNum=request.POST["phoneNum"]
       if CustomersTable.objects.filter(namesurname=namesurname).exists():
          return render(request,"customerAdd.html",{"error":f"Zaten {namesurname} adında bir müşteri var Lütfen belirteç ekleyiniz örneğin {namesurname}1 veya {namesurname}2"})
       else:
          if CustomersTable.objects.filter(tc=tc).exists():
               return render(request,"customerAdd.html",{"error":f"Zaten {tc} numaralı bir müşteri var.Tekrar giriniz 11 hane olacak şekilde"})
          else:
               customer=CustomersTable.objects.create(namesurname=namesurname,tc=tc,phoneNum=phoneNum)
               customer.save()
               return render(request,"customerAdd.html",{"error":f"Müşteri kayıt edildi ! Adı Soyadı:{namesurname},Tc Kimlik numarası:{tc} dir."})
     else:
          return render(request,"customerAdd.html")




def customerSee(request):
     customers=CustomersTable.objects.all()
     context={
          "customers":customers
     }
     return render(request,"customerSee.html",context)


def customerEdit(request,id):
     customer=get_object_or_404(CustomersTable,pk=id)

     if request.method == "POST":
          form=CustomersForm(request.POST,instance=customer)
          if form.is_valid():
               form.save()
               return redirect("custsomerSee")
     else:
          form=CustomersForm(instance=customer)
     return render(request,"customerEdit.html",{
          "form":form
     })



def productsAdd(request):
     
     if request.method == "POST":
       namesurname = request.POST["namesurname"]
       adet=request.POST["adet"]
       daralı=request.POST["daralı"]
       daraHesap=(int(adet))*(Kilogram.objects.get(pk=1).kilo)
       darasız=(int(daralı))-(int(daraHesap))
       safi=(int(darasız))
       tutar=(int(safi))*(Price.objects.get(pk=2.).price)
       if CustomersTable.objects.filter(namesurname=namesurname).exists():
               product=ProductTable.objects.create(namesurname=namesurname,adet=adet,daralı=daralı,safi=safi,tutar=tutar)
               product.save()
               return render(request,"productsAdd.html",{"error":f"Ürün ekleme başarılı"})
       else:
            return render(request,"productsAdd.html",{"error":f"Eklediğiniz ürünün sahibi yani {namesurname} müşteriler tablonuzda görünmüyor.Lütfen ekleyin daha sonra tekrar deneyin"})

              
     else:
          return render(request,"productsAdd.html")



def productsSee(request):
     products=ProductTable.objects.all()
     companys=Company.objects.all()

     context={
          "products":products,
          "companys":companys
     }
     return render(request,"productsSee.html",context)


def deleteEdit(request,id):
     productss=get_object_or_404(ProductTable,pk=id)
     if request.method == "POST":
          ProductTable.objects.get(pk=id).delete()
          return redirect("productsSee")
     return render(request,"productDeleteConfirm.html",{
          "productss":productss


     })
def customerdeleteEdit(request,id):
     products=get_object_or_404(CustomersTable,pk=id)
     if request.method == "POST":
          CustomersTable.objects.get(pk=id).delete()
          return redirect("custsomerSee")
     return render(request,"customerDeleteConfirm.html",{
          "products":products
     })


def personFilter(request,slug):
     

     
     context={
          "blogs":ProductTable.objects.filter(slug=slug),
          "clean":ProductTable.objects.all(),
          "cust":CustomersTable.objects.filter(slug=slug),
          "aggregate":ProductTable.objects.filter(slug=slug).aggregate(TUTAR=Sum('tutar')),
          "toplam":ProductTable.objects.filter(slug=slug).aggregate(ADET=Sum('adet')),
          "daralı":ProductTable.objects.filter(slug=slug).aggregate(DARALI=Sum('daralı')),
          "safi":ProductTable.objects.filter(slug=slug).aggregate(SAFİ=Sum('safi')),
     }    
     return render(request,"person.html",context)

def dateFilter(request,date):
     context={
          "days":ProductTable.objects.filter(date=date),

     }
     return render(request,"dateFilter.html",context)


def dailyTable(request):
     return redirect("productsSee")


def settings(request):
     return render(request,"settings.html")


def setPrice(request):
     context={
                "fiyat":Price.objects.get(pk=2).price
          }
     if request.method == "POST":
          setPrice=request.POST["setPrice"]
          
          Price.objects.filter(pk=2).update(price=setPrice)
          return render(request,"anasayfa.html",{"error":f"Eklediğiniz fiyat:{setPrice} TL'dir :Hesaplar {setPrice}, TL üzerinden yapılacak"})
     else:
          fiyat=Price.objects.all()
          context={ 
                "fiyat":fiyat
          }
          return render(request,"setPrice.html",context)
          


def setKg(request):
     context={
                "":Kilogram.objects.get(pk=1).kilo
          }
     if request.method == "POST":
          setKg=request.POST["setKg"]
          
          Kilogram.objects.filter(pk=1).update(kilo=setKg)
          return render(request,"anasayfa.html",{"error":f"Eklediğiniz Kasa ağırlığı:{setKg} Kg'dir Hesaplar {setKg}, Kg üzerinden yapılacak"})
     else:
          kilo=Price.objects.all()
          context={ 
                "kilo":kilo
          }
          return render(request,"setKg.html",context)



def setCompany(request):
     
     
     if request.method == "POST":
          setCompany=request.POST["setCompany"]
          
          Company.objects.filter(pk=1).update(company=setCompany)
          return render(request,"anasayfa.html",{"error":f"Yeni Şirket isminiz {setCompany}'dir"})
     else:
          return render(request,"setCompany.html")

def paid(request,id,slug):
     context={
          "paidProducts":ProductTable.objects.all(),
          "toplamtutar":ProductTable.objects.filter(slug=slug).aggregate(TUTAR=Sum('tutar')),
          "toplamtoplam":ProductTable.objects.filter(slug=slug).aggregate(ADET=Sum('adet')),
          "daralıdaralı":ProductTable.objects.filter(slug=slug).aggregate(DARALI=Sum('daralı')),
          "safisafi":ProductTable.objects.filter(slug=slug).aggregate(SAFİ=Sum('safi')),
          
       }
     products=get_object_or_404(ProductTable,pk=id)
     if request.method == "POST":
          prdct=ProductTable.objects.get(pk=id).delete()
          save=Paids.objects.create(prdct)
          save.save()
          return redirect("paid")
     return render(request,"home.html",{
          "products":products
     })