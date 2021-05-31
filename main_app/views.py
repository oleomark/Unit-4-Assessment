  
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import Item

# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', { 'items' : items })

class ItemCreate(CreateView): 
    model = Item
    fields = '__all__'
    success_url = '/'

class ItemDelete(DeleteView): 
    model = Item
    success_url = '/'