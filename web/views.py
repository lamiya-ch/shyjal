from django.shortcuts import render
from .models import Project
# Create your views here.

def index(request):
    return render(request,'index.html')
def features(request):
    return render(request,'features.html')


def projects(request):
    context = {
        'pro': Project.objects.all()
    }
    return render(request,'projects.html',context)

def writtings(request):
    return render(request,'writtings.html')