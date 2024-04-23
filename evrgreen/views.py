from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
   queryset = Product.objects.all()
   context={'product':queryset}
   return render(request,'base.html',context)