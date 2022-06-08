from django.shortcuts import render
from .models import Employee, Department, Roll

# Create your views here.


def home(request):
    return render(request, 'index.html')


def allemp(request):

    all_emps = Employee.objects.all()
    context = {
        'all_emps': all_emps
    }
    return render(request, 'allemp.html', context)
