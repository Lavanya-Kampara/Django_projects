from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    my_Dict = {"name":"Suthi", "Emp_ID":"1425909"}
    return render(request,'templatesApp/first_Template.html',context=my_Dict)

def renderEmployee(request):
    Dict1 = {"Emp_id": 123, "name": "Suthi", "Sal":30000}
    return render(request,'templatesApp/employee_Template.html',Dict1)
