from django.urls import path 
from . import views

urlpatterns = [
     path("case",views.case,name="case"),
     path("addFromBank",views.addFromBank,name="addFromBank"),
     path("bankSee",views.bankSee,name="bankSee"),
     path("addDebt",views.addDebt,name="addDebt"),
     path("debtSee",views.debtSee,name="debtSee")
]