from django.urls import path
from . import views

urlpatterns = [
    path('deposit/', views.deposit),
    path('savings/', views.savings),
    path('update/', views.dbupdate),
    path('exchange-rate/', views.exchange),
]
