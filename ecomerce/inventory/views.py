from django.shortcuts import render
from django.http import HttpResponse
import random



# Create your views here.
def index(request):
    names = ["sule", "sepe", "saayo", "gbogo", "maga", "mogo"]
    name= names[random.randint(0, 5)]
    return render(request, 'index.html', {"name": name})

def about(request):
    return render(request, 'test/about.html')


def counter(request):
    haha = request.POST["message"]
    textcount = len(haha)
    return render(request, "test/counter.html", {"textcount":textcount, "message": haha})