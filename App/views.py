from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile
from django.db.models import Q

# Create your views here.
def main(Request):
    if Request.method == 'GET':
        search = Request.GET.get('search')
        if search:
            user_prof = Profile.objects.filter(
                Q(name__icontains=search) |
                Q(email__icontains=search) |
                Q(age__icontains=search) |
                Q(religion__icontains=search)
            )
            if not user_prof:
                messages.warning(Request, 'No such Account Exist')
                return redirect('main')
        else:
            user_prof = Profile.objects.all()
    return render(Request,'First.html', locals())

def create(Request):
    if Request.method == 'POST':
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

def delete(Request, id):
    prof = Profile.objects.get(id=id)
    prof.delete()
    messages.error(Request, 'Profile has been deleted successfully')
    return redirect(main)






