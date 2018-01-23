(function($){

  var ListView = Backbone.View.extend({
    el: $('body'), // attaches `this.el` to an existing element.

    events: {
      'click #hello': 'addItem'
    },

    initialize: function() {
      _.bindAll(this, 'render', 'addItem'); // fixes loss of context for 'this' within methods

      this.counter = 0;
      this.render(); // not all views are self-rendering. This one is.
    },

    render: function() {
      $(this.el).append(`<button id="hello">hello world!</button>`);
      $(this.el).append(`<ul></ul>`);
    },

    addItem: function() {
      $('ul', this.el).append(`<li>hello again! (${++this.counter})</li>`)

    }
  });

  var listView = new ListView();

})(jQuery);