from django.contrib import admin

from cars.models import Car

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'prod_title', 'city', 'state', 'added_date')
    
    
admin.site.register(Car, CarAdmin)