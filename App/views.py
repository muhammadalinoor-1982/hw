from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

# Create your views here.
def main(Request):
    user_prof = Profile.objects.all()
    return render(Request,'First.html', locals())

def create(Request):
    return render(Request, 'create.html', locals())


