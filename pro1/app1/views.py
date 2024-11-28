from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from  django.contrib.auth.decorators import login_required
# Create your views here

def eview(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/employee.html",{"form":form})


def sview(request):
    obj = Employee.objects.all()
    return render(request,"app1/show.html",{"obj":obj})

def uview(request,pk):
    obj = Employee.objects.get(eid=pk)
    form = EmployeeForm(instance=obj)
    if request.method == "POST":
        form = EmployeeForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/employee.html",{"form":form})

def dview(request,k):
    obj = Employee.objects.get(eid=k)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"app1/success.html",{"obj":obj})

def searchview(request):
    obj = Employee.objects.all()
    if request.method == "POST":
        n = request.POST.get("search")
        obj = Employee.objects.filter(name__contains=n)

    return render(request,"app1/show.html",{"obj":obj})

def fview(request):
    q = request.GET.get("q")
    obj = Employee.objects.filter(gender=q)
    return render(request,"app1/show.html",{"obj":obj})

