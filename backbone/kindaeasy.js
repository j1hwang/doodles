(function($){

  var Item = Backbone.Model.extend({
    defaults: {
      part1: 'hello',
      part2: 'world!'
    }
  });

  var List = Backbone.Collection.extend({
    model: Item
  });

  var ListView = Backbone.View.extend({
    el: $('body'), // attaches `this.el` to an existing element.

    events: {
      'click #hello': 'addItem'
    },

    initialize: function() {
      // every function that uses 'this' as the current object should be in here
      _.bindAll(this, 'render', 'addItem', 'appendItem'); 

      this.collection = new List();

      ////////// collection event binder //////////
      this.collection.bind('add', this.appendItem); 
      /////////////////////////////////////////////
      // Backbone doesn't offer a separate 'Controller' for bindings

      this.counter = 0;
      this.render(); // not all views are self-rendering. This one is.
    },

    render: function() {

      var self = this;

      $(this.el).append(`<button id="hello">hello world!</button>`);
      $(this.el).append(`<ul></ul>`);

      _(this.collection.models).each(function(item) { //in case collection is not empty
        self.appendItem;
      }, this);
    },

    addItem: function(){
      this.counter++;
      var item = new Item();
      item.set({
        part2: item.get('part2') + this.counter // modify item defaults
      });
      this.collection.add(item); // add item to collection; view is updated via event 'add'
    },

    appendItem: function(item){
      $('ul', this.el).append("<li>"+item.get('part1')+" "+item.get('part2')+"</li>");
    }

  });

  var listView = new ListView();

})(jQuery);