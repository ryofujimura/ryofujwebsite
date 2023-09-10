from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# landing/views.py
# def landing_page(request):
#     return render(request, 'landing/index.html')

def index(request):
    return render(request, "landing/index.html")
