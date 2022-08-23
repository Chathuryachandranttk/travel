import django.shortcuts
from .models import Place
from .models import Team
from django.shortcuts import render


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'result1': obj1})


def home(request):
    return render(request, "index.html")


def about(request):
    return django.render(request, "index.html")

# def operations(request):
#    x = int(request.GET['num1'])
#    y = int(request.GET['num2'])
#    r1 = x + y
#    r2 = x - y
#    r3 = x * y
#    r4 = x / y
#    return django.shortcuts.render(request, "result.html", {'r1': r1, 'r2': r2, 'r3': r3, 'r4': r4})
