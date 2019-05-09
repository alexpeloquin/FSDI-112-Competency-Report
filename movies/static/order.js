
var movies = [];
var serverURL = "http://127.0.0.1:8000";

var order = {
    total: 0,
    client_id: 42,
    items: []
};

function getCatalog(){
    $.ajax({
        url: serverURL + "/api/movies/",
        type: "GET",
        success: function(res){
            movies = res.objects;
            for(var i=0; i<movies.length; i++){
                //some filtering if wanted by having the display function within and below
                displayMovie(movies[i]);

            }
        },
        error: function(error) {
            console.error("**ERROR**",error);
        }
    })
}

function displayMovie(movie){
    var tbody = $("#tblCatalog > tbody")
    console.log(tbody)
    var tr = `<tr>
    <td>${movie.id}</td>
    <td>${movie.title}</td>
    <td>${movie.release_year}</td>
    <td>${movie.stock}</td>
    <td>${movie.price}</td>
    <td><button movie-id= "${movie.id}" class= "btn btn-sm btn-success btn-add">Add to Cart</button></td>
    </tr>`;
    tbody.append(tr);
}

function add2Cart(movie) {
    // add to object
    var rentMovie = {
        movie_id: movie.id,
        quantity: 1,
    }

    var found = false;
    //check if the id exist on the order.items
    for (var i=0; i<order.items.length; i++){
        var indexM = order.items[i];
        if(indexM.id == rentMovie.movie_id){
            //found it
            indexM.quantity +=1;
            found = true;
        }
    }
    if (!found) {
            //if not, just add the rentMovie about
            order.items.push(rentMovie);
    }
    //else increase the quantity of the existing one
    order.total += movie.price;
    
    //update display
    $("#txtNumberItems").val(order.items.length);
    $("#txtTotal").val(order.total.toFixed(2));
}

function saveOrder(){
    $.ajax({
        url: serverURL + "/api/orders/",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(order),
        success: function(res){
            console.log("Im a yedi DEV",res);
        },
        error: function(error){
            console.error("**ERROR**",error);
        }
    });
}

function init() {
    console.log("order.js loaded");
    //get movie catalog
    getCatalog();

    // save button
    $("#btnSave").click(saveOrder);

    // dynamic hook of events and hook the click from the rent button
    // whenever a CLICK happens on a BTN.ADD class element
    $("#tblCatalog").on('click',".btn-add",function(){
        var id = $(this).attr("movie-id");
        //find the movie with that ID
        for(var i=0; i<movies.length; i++ ){
            var m=movies[i];
            if(m.id ==id){
                //found it
                add2Cart(m);
                break; //finish the loop
            }
        }
    });
}


window.onload = init;