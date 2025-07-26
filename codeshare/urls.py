from django.urls import path
from . import views

app_name = 'codeshare'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('reset/<int:pk>/', views.reset, name='reset'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),

]
