from django.shortcuts import render

from .models import Contact

def info(request):
    return render(request, 'contact/info.html')
