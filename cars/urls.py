from django.urls import path
from .import views
urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.prod_details, name='prod_details'),
    path('search', views.search, name='search'),
    
]