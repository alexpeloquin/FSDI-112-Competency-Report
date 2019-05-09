from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    #These are the columns i want to display on the genre
    list_display = ("id","name") #tuple

class MoviesAdmin(admin.ModelAdmin):
    # will exclude what ever field include comma
    #exclude = ('price',)
    # list which elements will be there on add movie
    #fields = ("title", "stock")
    list_display = ('id','title','stock','price') #properties on list table
 
# Register your models here.
admin.site.register(Genre,GenreAdmin)
admin.site.register(Movie,MoviesAdmin)

