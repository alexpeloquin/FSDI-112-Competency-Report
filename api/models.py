from django.db import models
from tastypie.resources import ModelResource, ALL
from movies.models import Movie, Genre, Order, Order_Items
from tastypie.authorization import Authorization

# Create your models here.
# Model the data that will go into the front end
# API aka resources

class MovieResource(ModelResource):
    class Meta:
        resource_name = "movies"
        # What query to be run to get data
        queryset = Movie.objects.all()
        #excludes = ['price']
        # Filtering is done with a ? at the end of the URL address
        # ?stock__gt=11
        filtering = {'price':ALL,"stock":ALL,}

class GenreResource(ModelResource):
    class Meta:
        resource_name = "genres"
        # What query to be run to get data
        queryset = Genre.objects.all()
        #excludes = ['price']
        # Filtering is done with a ? at the end of the URL address
        # ?stock__gt=11
        filtering = {'name':ALL}

# is what the API will use
class Order_ItemsResource(ModelResource):
    class Meta:
        resource_name = "orderitems"
        queryset = Order_Items.objects.all()

# allows the get method for orders
class OrderResource(ModelResource):
    class Meta:
        resource_name = "orders"
        queryset = Order.objects.all()
        # also needs to receive post methods to update cart
        allowed_methods = ['get', 'post', 'put', 'patch', 'delete']
        authorization = Authorization()


