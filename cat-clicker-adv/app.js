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
	}
};

var view = {
	init: function() {
		view.render_list();
		this.render_detail(0);
	},
	render_list: function() {
		var cats = octopus.getCats();
		var many = cats.length;
		for(var i=0; i<many; i++) {
			$('#list').append(`<ul id="cat${i}">${cats[i].name}</ul>`);
			$('#cat'+i).click( (function(catNum) {
				return function() {
					view.render_detail(catNum);
				}
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
		
		this.render_number(catNum);

     

		$('#admin').click( function() { $('.hidden').toggle(); });

		// $('#name').val(cats[catNum].name);
		// // $('#url').val(cats[catNum].imgURL);


		// $('#cancel').click( function() { 
		// 	$('.hidden').toggle(); 
		// 	// $('#name').attr('value', cats[catNum].name);
		// 	// $('#url').attr('value', cats[catNum].imgURL);
		// 	// $('#clicks').attr('value', cats[catNum].numOfClicks);
		// });
		
		// $('#save').click( function() {

		// 	$('.hidden').toggle();
		// });	
		
	},
	render_number: function(catNum) {
		var cats = octopus.getCats();
		var count = octopus.getCount(catNum);
		$('#num').text(count);
		$('#clicks').val(cats[catNum].numOfClicks);
	},

};
octopus.init();
