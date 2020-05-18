from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemForm
# Create your views here.
def pageCount(request):
    count = request.session.get('count',0)
    count = count + 1
    request.session['count'] = count
    return render(request,'sessionApp/count.html',{'count':count})
def index(request):
    request.session.set_expiry(120)
    raise Exception("Something terrible has happened")
    return render(request,'sessionApp/index.html')

def addItem(request):
    form = ItemForm()
    if request.method == "POST":
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name]=quantity
    return render(request,'sessionApp/addItem.html',{'form':form})
def displayCart(request):
    return render(request,'sessionApp/displayItems.html')
