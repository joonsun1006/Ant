from django.urls import path
from . import views

urlpatterns = [
    path('deposit/', views.deposit),
    path('savings/', views.savings),
    path('detail/<int:detail_pk>/', views.detail),
    path('update/', views.dbupdate),
    path('exchange-rate/', views.exchange),
    path('recommend/', views.recommend),
    path('dnsaddordelete/<int:user_pk>/<int:dns_pk>/', views.addOrDeleteProducts),
]