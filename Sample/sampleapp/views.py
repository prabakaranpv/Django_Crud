from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Mymodel

# Create your views here.


def home_fun(request):
    return render(request,'home.html')


def add_fun(request):
    obj = Mymodel()
    obj.Name = request.POST['txtname']
    obj.Email = request.POST['txtemail']
    obj.Password = int(request.POST['txtpassword'])
    obj.save()
    # return render(request,'home.html',{'msg':'Insert sucessfully'})
    return redirect('show')

def show_fun(request):
    obj=Mymodel.objects.all()
    return render(request,'show.html',{'show':obj})

def update_fun(request,sampleid):
    obj = Mymodel.objects.get(id=sampleid)
    if request.method == "POST":
         obj.Name = request.POST['txtname']
         obj.Email = request.POST['txtemail']
         obj.Password = int(request.POST['txtpassword'])
         obj.save()
         return redirect('show')
    else:
        return render(request,'update.html',{'up':obj})
        


def delete_fun(request,sampleid):
    obj = Mymodel.objects.get(id=sampleid)
    obj.delete()
    return redirect('show')
