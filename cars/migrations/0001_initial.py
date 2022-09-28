# Generated by Django 4.0.6 on 2022-09-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_title', models.CharField(max_length=150)),
                ('city', models.CharField(choices=[('NE', 'Nevada'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX')], max_length=100)),
                ('state', models.CharField(choices=[('NE', 'Nevada'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX')], max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('prod_model', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], verbose_name='year')),
                ('prod_condition', models.CharField(max_length=100)),
                ('prod_price', models.IntegerField()),
                ('prod_description', models.TextField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('prod_features', models.CharField(choices=[('NE', 'Nevada'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX')], max_length=100)),
                ('prod_style', models.CharField(choices=[('NE', 'Nevada'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX'), ('XX', 'XXXXXX')], max_length=100)),
                ('is_featured', models.BooleanField(max_length=100)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]