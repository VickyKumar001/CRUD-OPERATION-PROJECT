from django.shortcuts import render, redirect
from .models import Student

def home(reqeust):
    st = Student.objects.all()
    return render(reqeust, 'home.html', {'st':st})



def add(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        roll=request.POST.get("roll")
        email=request.POST.get("email")
        num=request.POST.get("num")
        address=request.POST.get("address")
        city=request.POST.get("city")
        pincode=request.POST.get("pincode")

        
        s=Student()
        s.name=name
        s.roll=roll
        s.email=email
        s.num=num
        s.address=address
        s.city=city
        s.pincode=pincode
        s.save()
        return redirect('home')

    return render(request, "add.html")


def delete(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect("/home")



def update(request, roll):
    s=Student.objects.get(pk=roll)
    return render(request, "update.html", {'s':s})


def doupdate(request,roll):
    s=Student.objects.get(pk=roll)
    if request.method == 'POST':
        name=request.POST.get("name")
        roll=request.POST.get("roll")
        email=request.POST.get("email")
        num=request.POST.get("num")
        address=request.POST.get("address")
        city=request.POST.get("city")
        pincode=request.POST.get("pincode")
        
        s.name=name
        s.roll=roll
        s.email=email
        s.num=num
        s.address=address
        s.city=city
        s.pincode=pincode
        s.save()

        return redirect('home')
    
    return redirect('update')







    


