 $(document).ready(function(){
 	  var ht= $(window).height();
      $(".button-collapse").sideNav();
      $('.parallax').parallax();
      $('.modal-trigger').leanModal();
      $('.slider').slider({height:ht, indicators:false});
    });