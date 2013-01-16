(function($) {

var FACEBOOK_URL = 'https://graph.facebook.com';

// keep the original around
var load = Galleria.prototype.load;

/* extend the load method to use facebook if option is present.
   this is the way the Galleria flickr plugin */
Galleria.prototype.load = function() {
    /* check if facebook option is provided. Call the original load
       if not. */
    if(typeof this._options.facebook !== 'string'){
        load.apply(this, Galleria.utils.array(arguments));
        return;
    }

    var galleria = this,
        facebook = this._options.facebook;

    $.ajax({
        url: FACEBOOK_URL + '/' + facebook + '/photos?fields=picture,source&limit=50',
        dataType: 'json',
        success: function(data){
            var images = [];
            for(var i=0; i<data.data.length; i++){
                var _image = data.data[i];
                images.push({
                    image: _image.source,
                    thumb: _image.picture
                });
            }
            galleria._data = images;
            galleria.trigger(Galleria.DATA);
        }
    });
};

}(jQuery));
