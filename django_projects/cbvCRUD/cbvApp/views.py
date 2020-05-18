from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from cbvApp.models import Student
# Create your views here.

class StudentListView(ListView):
    model = Student

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    fields = ('firstName','lastName','testScore')
