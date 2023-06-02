from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile

# Create your views here.
def main(Request):
    user_prof = Profile.objects.all()
    return render(Request,'First.html', locals())

def create(Request):
    name     = Request.POST.get('name')
    image    = Request.FILES.get('image')
    email    = Request.POST.get('email')
    age      = Request.POST.get('age')
    address  = Request.POST.get('address')
    phone    = Request.POST.get('phone')
    dob      = Request.POST.get('dob')
    religion = Request.POST.get('religion')
    gender   = Request.POST.get('gender')

    if name:
        if image:
            prof = Profile.objects.create(
                name     = name,
                image    = image,
                email    = email,
                age      = age,
                address  = address,
                phone    = phone,
                dob      = dob,
                religion = religion,
                gender   = gender
            )
            prof.save()
            messages.success(Request, 'User Account has been Created successfully')
            return redirect('main')
        else:
            prof = Profile.objects.create(
                name        = name,
                email       = email,
                age         = age,
                address     = address,
                phone       = phone,
                dob         = dob,
                religion    = religion,
                gender      = gender
            )
            prof.save()
            messages.success(Request, 'User Account has been Created successfully without user image')
            return redirect('main')
    else:
        messages.error(Request, "Please Fill up all fields.")
        return render(Request, 'create.html', locals())



