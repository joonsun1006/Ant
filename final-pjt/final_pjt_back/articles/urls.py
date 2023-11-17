from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('<int:article_pk>/comment/', views.comment_create),
]
