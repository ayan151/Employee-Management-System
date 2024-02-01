from django.shortcuts import render
from django.shortcuts import HttpResponse 
from django.http import response
from datetime import datetime

from .models import Employee
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,"index.html")


def all_emp(request):

    emps = Employee.objects.all()
    contexts = {
        'emps': emps
    }
    return render(request,"all_emp.html" , contexts)


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        dept = int(request.POST["dept"])
        salary = int(request.POST["salary"])
        bonus = int(request.POST["bonus"])
        role = int(request.POST["role"])
        phone = request.POST["phone"]
        hire_date = request.POST["hire_date"]
        new_emp = Employee(first_name = first_name ,last_name =last_name, salary=salary, bonus=bonus, phone=phone, role_id=role, dept_id=dept,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse ("summet successfully")
    elif request.method == "GET":
        return render(request,'add_emp.html')
    else:
        return HttpResponse("An Exception  Occured! Employee")
    
    # return render(request,"add_emp.html")



def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_remove = Employee.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            return HttpResponse("Employee Removed successfully")
        except:
            return HttpResponse("reply ENter valid emp_id ")
    emps = Employee.objects.all()
    contexts = {
       'emps' :emps
    }
    return render(request,"remove_emp.html",contexts)


def filter_emp(request):
    if request.method =='POST':
        name = request.POST["name"]
        dept = request.POST["dept"]
        role = request.POST["role"]
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        contexts = {
           'emps': emps 
        }

        return render(request,"all_emp.html" ,contexts)
    elif request.method == 'GET':
        return render(request,"filter_emp.html" )
    
    else:
        return HttpResponse("your data is invalided")


