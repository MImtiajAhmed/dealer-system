from django.shortcuts import render
from .models import Car

# Create your views here.
def cars(request):
    car_data = Car.objects.all()
    call_data = {
        'car_data': car_data
    }
    return render(request, 'pages/cars/cars.html', car_data)