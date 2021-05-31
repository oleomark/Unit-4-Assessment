from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('items/add', views.ItemCreate.as_view(), name='items_add'),
  path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='home'),
]