from django.urls import path
from . import views

app_name = 'codeshare'

urlpatterns = [
    path('', views.index, name='index'),
    path('share/', views.share, name='share'),
    path('snippet/<int:pk>/', views.detail, name='detail'),
    path('show_ip/', views.show_ip, name="showip"),
]
