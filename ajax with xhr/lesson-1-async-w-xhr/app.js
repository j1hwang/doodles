(function () {
    const form = document.querySelector('#search-form');
    const searchField = document.querySelector('#search-keyword');
    let searchedForText;
    const responseContainer = document.querySelector('#response-container');

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        responseContainer.innerHTML = '';
        searchedForText = searchField.value;

        const unsplashRequest = new XMLHttpRequest();
		unsplashRequest.onload = addImage;
		unsplashRequest.onerror = function(err) {
			requestError(err, 'image');
		}
		unsplashRequest.open('GET', `https://api.unsplash.com/search/photos?page=1&query=${searchedForText}`);
		unsplashRequest.setRequestHeader('Authorization', 'Client-ID 77525a9cb44b701c8ce084a3d3d2eb2a7062dc3227f0e6ed0d8c2c6b0c415461');
		unsplashRequest.send();

		const articleRequest = new XMLHttpRequest();
		articleRequest.onload = addArticles;
		articleRequest.open('GET', `http://api.nytimes.com/svc/search/v2/articlesearch.json?q=${searchedForText}&api-key=4067df4122aa45068c179f0f0e4afbae`);
		//unsplashRequest.setRequestHeader
		articleRequest.send();
    });	


    function addImage() {
    	//debugger;
    	let htmlContent = '';
    	const data = JSON.parse(this.responseText);
    	
    	if(data && data.results && data.results[0]) {
	    	const firstImage = data.results[0];

	    	htmlContent = `<figure>
	    		<img src="${firstImage.urls.regular}" alt="${searchedForText}">
	    		<figcaption>${searchedForText} by ${firstImage.user.name}</figcaption>
	    	</figure>`;

	    	//console.log(htmlContent);
	    	responseContainer.insertAdjacentHTML('afterbegin', htmlContent);
	    }
	}

	function addArticles() {

		let htmlContentForNews = '';
		const data = JSON.parse(this.responseText);

		console.log(data);
		if(data && data.response && (data.response.docs.length!==0)) {
			const articles = data.response.docs;
			
			htmlContentForNews = `<ul>`;
			for( var i=0; i<articles.length; i++) {
				var article = articles[i];
				htmlContentForNews += `<li class='article'><h2><a href='${article.web_url}'>${article.headline.main}</a></h2>
				<p>${article.snippet}</p></li>`;
			}
			htmlContentForNews += `</ul>`;
			console.log(htmlContentForNews);
		}else {
			htmlContentForNews = `<h5>No Article About "${searchedForText}"</h5>`;
		}
		//console.log(htmlContentForNews);
		responseContainer.insertAdjacentHTML('beforeend', htmlContentForNews);
	}
})();
