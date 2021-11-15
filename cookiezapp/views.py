from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import user

# Create your views here.
from .models import cakecookiez


def index(request):
    obj=cakecookiez.objects.all()
    return render(request,'index.html',{'results':obj})