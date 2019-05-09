from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Movie, Genre


# Create your views here.
# Declare functions that take inputs from client
# performs processing and returns to the client

def index(request):
    # Movie.objects.all() - reads the table
    # Movie.objects.filter(release_year = 2004)
    # Movie.objects.get(id=1)

    catalog = Movie.objects.all()
    return render(request,"views/index.html",
    {"catalog": catalog, 'title': "This is the title"})

def test(request):
    return HttpResponse("<h1>Im a Test</h1>")

def contact(request):
    return HttpResponse("<h2>Page under construction</h2>")

#movies/detail/1
#find the object with id = 1 and render detail for that object
def detail(request,movie_id):
    try:
        the_movie=Movie.objects.get(id=movie_id)
        return render(request,"views/detail.html", {"movie" : the_movie})
    except Movie.DoesNotExist:
        #raise a 404 error
        raise Http404()

def genres(request):
    the_genre=Genre.objects.all()
    return render(request,"views/genres.html",{"genres" :the_genre})

def history(request):
    return render(request,'views/history.html')

def order(request):
    return render(request, "views/order.html")


