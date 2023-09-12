from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, "landing/index.html")

def tab1(request):
    return render(request, 'landing/tab1.html')

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def age_display(request):
    # Hardcoded birthdate
    birthdate = datetime(1999, 7, 6)
    
    age = calculate_age(birthdate)
    
    context = {
        'age': age,
    }
    
    return render(request, 'landing/index.html', context)
