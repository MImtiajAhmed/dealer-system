import re
from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
    prod_data = Car.objects.order_by('-added_date')
    paginator = Paginator(prod_data, 4)
    page = request.GET.get('page')
    paged_prod = paginator.get_page(page)
    
    model_search = Car.objects.values_list('prod_model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    style_search = Car.objects.values_list('prod_style', flat=True).distinct()
    
    
    data = {
        'prod_data': paged_prod,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'style_search': style_search,
    }
    return render(request, 'pages/cars/cars.html', data)

def prod_details(request, id):
    single_prod = get_object_or_404(Car, pk=id)
    single_prod_data = {
        'single_prod': single_prod
    }
    return render(request, 'pages/cars/prod_details.html', single_prod_data)



def search(request):
    prod_data = Car.objects.order_by('-added_date')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            prod_data = prod_data.filter(prod_title__icontains = keyword)
        
        
    if 'prod_model' in request.GET:
        prod_model = request.GET['prod_model']
        if prod_model:
            prod_data = prod_data.filter(prod_model__iexact = prod_model)
        
        
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            prod_data = prod_data.filter(city__iexact = city)
        
        
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            prod_data = prod_data.filter(year__iexact = year)
        
    if 'type' in request.GET:
        prod_style = request.GET['type']
        if type:
            prod_data = prod_data.filter(prod_style__iexact = prod_style)
        
        
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            prod_data = prod_data.filter(prod_price__gte = min_price, prod_price__lte = max_price)
        
    
    data = {
        'prod_data': prod_data,
    }
    
    return render(request, 'pages/cars/search.html', data)