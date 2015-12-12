 $(document).ready(function(){
 	  var ht= $(window).height();
      $(".button-collapse").sideNav();
      $('ul.tabs').tabs();
      $('.parallax').parallax();
      $('.modal-trigger').leanModal();
      $('.slider').slider({height:ht, indicators:false});
      $('.datepicker').pickadate({
    		selectMonths: true,
    		selectYears: 50 
  			});
    });