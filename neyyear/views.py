import datetime
from django.shortcuts import render
from django.utils.timezone import now

# Create your views here.

def index(request):
    return render(request,"neyyear/index.html",{
        "neyyear": now.month==1 and now.date==1
    })