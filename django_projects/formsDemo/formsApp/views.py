from django.shortcuts import render
from . import forms
# Create your views here.
def UserRegistrationView(request):
    form = forms.UserRegistrationForm()
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("form is Valid")
            print("First Name",form.cleaned_data['firstName'])
            print("First Name",form.cleaned_data['lastName'])
            print("First Name",form.cleaned_data['email'])
    return render(request,'formsDemo/userRegistration.html',{'form':form})
