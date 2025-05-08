from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def acerca_de(request):
    return render(request, 'core/acerca_de.html')

def contactos(request):
    return render(request, 'core/contactos.html')

def vehiculo_1(request):
    return render(request, 'core/vehiculo_1.html')

def home2(request):
    return render(request, 'core/home2.html')

def home3(request):
    return render(request, 'core/home3.html')