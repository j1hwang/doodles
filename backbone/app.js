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


  // rendering each individual 'Item'
  var ItemView = Backbone.View.extend({
    tagName: 'li',
    className: 'test',
    
    initialize: function() {
      _.bindAll(this, 'render');
    },

    render: function() {
      $(this.el).html('<span>'+this.model.get('part1')+' '+this.model.get('part2')+'</span>');
      return this;
    }
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
      var itemView = new ItemView({
        model: item
      });
      $('ul', this.el).append(itemView.render().el);
    }

  });

  var listView = new ListView();

})(jQuery);