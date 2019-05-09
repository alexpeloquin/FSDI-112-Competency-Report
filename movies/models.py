from django.db import models

# Create your models here

class Genre(models.Model):
    name = models.CharField(max_length=50)
    # modify the str representation of Genre objects
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_year = models.IntegerField()
    price = models.FloatField()
    stock = models.IntegerField()
#Relation between tables(classes), CASCADE means genre removed, then also removed from other Movies with same Genre
#Everytime you change the model you need to perform another migration
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Order(models.Model):
    cleint_id = models.IntegerField()
    total = models.FloatField()

class Order_Items(models.Model):
    movie_id: models.IntegerField()
    quantity: models.IntegerField()
    order: models.ForeignKey(Order,on_delete = models.CASCADE)











