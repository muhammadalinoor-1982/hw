from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(Request):
    value = Request.POST.get('txt')
    # print(value)
    context = {
        'data' : value
    }
    return render(Request,'First.html', context)


