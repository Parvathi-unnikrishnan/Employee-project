from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from app1.models import Emp






# Create your views here.
def home(request):
    k=Emp.objects.all()
    return render(request,'home.html',{'employee':k})

def add(request):
    if(request.method=="POST"):
        n=request.POST['n']
        add = request.POST['add']
        a= request.POST['a']
        i = request.FILES['i']
        e = request.POST['e']
        m=Emp.objects.create(name=n,address=add,age=a,email=e,image=i)
        m.save()
        return home(request)
    return render(request,'add.html')









def details(request,i):
    k=Emp.objects.get(id=i)
    return render(request,'details.html',{'employee':k})




def delete(request,i):
    k=Emp.objects.get(id=i)
    k.delete()
    return home(request)








def edit(request,i):
    k=Emp.objects.get(id=i)
    if(request.method=="POST"):
        k.name=request.POST['n']
        k.address=request.POST['add']
        k.age=request.POST['a']
        k.email=request.POST['e']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.image=request.FILES.get('i')
        k.save()
        return home(request)

    return render(request,'edit.html',{'employee':k})

