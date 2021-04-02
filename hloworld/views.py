from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    nm="hlhlhk"
    ls=[1,2,3,4]
    context={
        "name":nm,
        "lt":ls
    }
    return render(request,"index.html",context)