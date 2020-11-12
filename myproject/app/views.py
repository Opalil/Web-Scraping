from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    jobs = Job.objects.all()
    context = {'jobs': jobs}
    return render(request, 'base/index.html', context)