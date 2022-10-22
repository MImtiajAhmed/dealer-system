from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_prod = Car.objects.order_by('-added_date').filter( is_featured=True)
    all_prod = Car.objects.order_by('-added_date')
    model_search = Car.objects.values_list('prod_model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    style_search = Car.objects.values_list('prod_style', flat=True).distinct()
    data = {
        'teams':teams,
        'featured_prod': featured_prod,
        'all_prod': all_prod,
        'model_search': model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'style_search' : style_search,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')