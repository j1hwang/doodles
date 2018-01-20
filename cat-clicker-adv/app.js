var model = {
	cats: [
	{
		name: 'Navvy',
		imgURL: './images/navvy.jpg',
		numOfClicks: 0
	},
	{
		name: 'Chewie',
		imgURL: './images/chewie.jpg',
		numOfClicks: 0
	},
	{
		name: 'Nick',
		imgURL: './images/nick.jpg',
		numOfClicks: 0
	},
	{
		name: 'Sham',
		imgURL: './images/sham.jpg',
		numOfClicks: 0
	},
	{
		name: 'Tiger',
		imgURL: './images/tiger.jpg',
		numOfClicks: 0
	}
	]
};

var octopus = {
	init: function() {
		view.init();
	},
	getCats: function() {
		return model.cats;
	},
	getCount: function(catNum) {
	 	return model.cats[catNum].numOfClicks;
	},
	increase: function(catNum) {
		model.cats[catNum].numOfClicks++;
		view.render_number(catNum);
	},
	update: function(catNum, name, imgURL, numOfClicks) {
		console.log(catNum);
		model.cats[catNum].name = name;
		model.cats[catNum].imgURL = imgURL;
		model.cats[catNum].numOfClicks = numOfClicks;
	}
};

var view = {
	init: function() {
		view.render_list();
		view.render_detail(0);
	},
	render_list: function() {
		var cats = octopus.getCats();
		var many = cats.length;
		$('#list').empty();
		for(var i=0; i<many; i++) {
			$('#list').append(`<ul id="cat${i}">${cats[i].name}</ul>`);
			$('#cat'+i).click( (function(catNum) {
				return function() {
					view.render_detail(catNum);
				};
			})(i) );
		}
	},
	render_detail: function(catNum) {
		var cats = octopus.getCats();
		
		$('#photo').empty();
		$('#photo').append(`<img id="kitty" src="${cats[catNum].imgURL}" height="400">`);
		$('#kitty').click( function() {
			octopus.increase(catNum);
		});
		
		view.render_number(catNum);

		// set admin button
		$('#admin').unbind();
     	$('#admin').click( function() { $('#secret').toggle(); });
	
		// set default input value
		$('#name').val(cats[catNum].name);
		$('#url').val(cats[catNum].imgURL);

		// set cancel button
		$('#cancel').unbind();
		$('#cancel').click( function() { 
			$('#secret').toggle(); 
			$('#name').val(cats[catNum].name);
			$('#url').val(cats[catNum].imgURL);
			$('#clicks').val(cats[catNum].numOfClicks);
		});
		
		// set save button
		$('#save').unbind();
		$('#save').click( function() {
			var name = $('#name').val();
			var url = $('#url').val();
			var clicks = parseInt($('#clicks').val());

			octopus.update(catNum, name, url, clicks);

			view.render_list();
			view.render_detail(catNum);
			$('#secret').toggle();
		});	
		
	},
	render_number: function(catNum) {

		var cats = octopus.getCats();
		var count = octopus.getCount(catNum);
		$('#num').text(count);
		$('#clicks').val(cats[catNum].numOfClicks);
	}
};
octopus.init();
