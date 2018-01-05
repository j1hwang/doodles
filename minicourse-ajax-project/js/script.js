
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");


    // YOUR CODE GOES HERE!
    var street = $('#street').val()
    var city = $('#city').val()

     $greeting.text(`So, you want to live at ${street}, ${city}?`);

    var full_url = `http://maps.googleapis.com/maps/api/streetview?size=600x300&location=${street}, ${city}`;
    $body.append(`<img class='bgimg' src='${full_url}'>`);
    console.log(full_url);

    var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    url += '?' + $.param({
        'api-key': "4067df4122aa45068c179f0f0e4afbae",
        'q' : city,
        'sort': "newest"
    });
   
        
    $.getJSON(url, function (data) {

        $nytHeaderElem.text('New York Times Articles about ' + city);

        console.log(data);
        articles = data.response.docs;
        
        for(var i=0 ; i<articles.length ; i++){
            var article = articles[i];
            $nytElem.append(`<li class='article'><a href='${article.web_url}'>${article.headline.main}</a><p>${article.snippet}</p></li>`);
        }

    }).error(function(err) {
        $nytHeaderElem.text('Error Occurred, Something is WRONG!!');
    });

    
    var wiki_url = 'https://en.wikipedia.org/w/api.php?action=opensearch&search=' + city +'&format=json&callback=wikiCallback';

    var wikiRequestTimeout = setTimeout(function() {
         $wikiElem.text("failed to get Wikipedia resources");
    }, 8000);

    $.ajax(wiki_url, {
        dataType: "jsonp",
        //jsonp: "callback",
        success: function(response){
            var articles = response[1];

            for( var i=0; i<articles.length; i++) {
                title = articles[i];
                var url = 'http://en.wikipedia.org/wiki/' + title;
                $wikiElem.append(`<li><a href='${url}'>${title}</a></li>`);
            }

            clearTimeout(wikiRequestTimeout);
        }        
    });


    return false;
};

$('#form-container').submit(loadData);
