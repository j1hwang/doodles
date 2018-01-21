var initialCats = [
	{
		name: 'Tabby',
		imgSrc: './images/navvy.jpg',
		numOfClicks: 0,
		imgAttr: 'http://www.google.com',
		nicknames: ['Tabtab', 'T-bone', 'Mr.T', 'Tabby the Cat']
	},
	{
		name: 'Chewie',
		imgSrc: './images/chewie.jpg',
		numOfClicks: 0,
		imgAttr: 'http://www.google.com',
		nicknames: ['Chewing Gum']
	},
	{
		name: 'Nick',
		imgSrc: './images/nick.jpg',
		numOfClicks: 0,
		imgAttr: 'http://www.google.com',
		nicknames: ['Nickky']
	},
	{
		name: 'Sham',
		imgSrc: './images/sham.jpg',
		numOfClicks: 0,
		imgAttr: 'http://www.google.com',
		nicknames: ['Shaboom']
	},
	{
		name: 'Tiger',
		imgSrc: './images/tiger.jpg',
		numOfClicks: 0,
		imgAttr: 'http://www.google.com',
		nicknames: ['Tigre']
	}
]

var ViewModel = function() {
	var self = this;

	this.catList = ko.observableArray([]);

	initialCats.forEach(function(catItem) {
		self.catList.push( new Cat(catItem) );
	});
	this.currentCat = ko.observable( self.catList()[0] );

	self.setCat = function(clickedCat) {
		self.currentCat(clickedCat);
	}

	this.incrementCounter = function() {
		self.currentCat().clickCount( self.currentCat().clickCount() + 1 );
	};
};

var Cat = function(data) {

	this.clickCount = ko.observable(data.numOfClicks);
	this.name = ko.observable(data.name);
	this.nicknames = ko.observableArray(data.nicknames);
	this.level = ko.computed( function() {
		if(this.clickCount() < 5) return 'baby';
		else return 'teen';	
	}, this);

	this.imgSrc = ko.observable(data.imgSrc);
	this.imgAttr = ko.observable(data.imgAttr);
};

ko.applyBindings(new ViewModel());