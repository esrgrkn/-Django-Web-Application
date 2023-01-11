from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('custsomerAdd',views.custsomerAdd,name='custsomerAdd'),
    path('custsomerSee',views.customerSee,name='custsomerSee'),
    path('edit/<int:id>',views.customerEdit,name='customerEdit'),
    path('delete/<int:id>',views.deleteEdit,name='deleteEdit'),
    path('deletes/<int:id>',views.customerdeleteEdit,name='customerdeleteEdit'),
    path('productsAdd',views.productsAdd,name='productsAdd'),
    path('productsSee',views.productsSee,name="productsSee"),
    path("person/<slug:slug>", views.personFilter, name="personFilter"),
    path("settings",views.settings,name="settings"),
    path("setPrice",views.setPrice,name="setPrice"),
    path("setKg",views.setKg,name="setKg"),
    path("filter_date/<str:date>", views.dateFilter, name="dateFilter"),
    path("dailyTable",views.dailyTable,name="dailyTable"),
    path("setCompany",views.setCompany,name="setCompany"),
    path("paid/<int:id>",views.paid,name="paid")

]
