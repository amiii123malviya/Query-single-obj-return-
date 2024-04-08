from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student

def home(request):
    # data=Student.objects.create(Name="amisha",
    #                             Email="amii@gmail.com",
    #                             Contact="123456789",
    #                             City="Bhopal")

    # data=Student.objects.get(id=2)
    data=Student.objects.get(Name="amisha")

    print(data)
    return HttpResponse(data)
    


