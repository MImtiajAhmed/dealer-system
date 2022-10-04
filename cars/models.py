from turtle import color
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Car(models.Model):
    
    # State name listing
    state_choice = (
        ('NE', 'Nevada'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
    )
    
    # Year choice list
    year_choice =[]
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))
        
    # Feature choice list
    
    feature_choices = (
        ('NE', 'Nevada'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
        ('XX', 'XXXXXX'),
    )
    
    prod_title = models.CharField(max_length=150)
    city = models.CharField(choices = state_choice, max_length=100)
    state = models.CharField(choices = state_choice, max_length=100)
    color = models.CharField(max_length=100)
    prod_model = models.CharField(max_length=100)
    year = models.IntegerField('year', choices = year_choice)
    prod_condition = models.CharField(max_length=100)
    prod_price = models.IntegerField()
    prod_description = RichTextField()
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    photo1 = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    photo2 = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    photo3 = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    photo4 = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank = True)
    prod_features = models.CharField(choices=feature_choices, max_length=100)
    prod_style = models.CharField(choices=feature_choices, max_length=100)
    is_featured = models.BooleanField(default= False)
    # You can add many more
    added_date = models.DateTimeField(auto_now_add=True)
    
    