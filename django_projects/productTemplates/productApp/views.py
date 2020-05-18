from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_Dict = {
    'product1':'Mac',
    'product2':'IPhone',
    'product3':'Dell'
    }

    return render(request,'productApp/products.html',product_Dict)

def toys(request):
    product_Dict = {
    'product1':'Remote Car',
    'product2':'Drone',
    'product3':'Rocket Launcher'
    }

    return render(request,'productApp/products.html',product_Dict)

def shoes(request):
    product_Dict = {
    'product1':'Nike',
    'product2':'Adidas',
    'product3':'Reebok'
    }

    return render(request,'productApp/products.html',product_Dict)

def index(request):
    return render(request,'productApp/index.html')
