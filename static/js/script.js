(function($) {

	"use strict";

	$('nav .dropdown').hover(function(){
		var $this = $(this);
		$this.addClass('show');
		$this.find('> a').attr('aria-expanded', true);
		$this.find('.dropdown-menu').addClass('show');
	}, function(){
		var $this = $(this);
			$this.removeClass('show');
			$this.find('> a').attr('aria-expanded', false);
			$this.find('.dropdown-menu').removeClass('show');
	});

})(jQuery);

//SLIDER AAAAAAAAAA

//cdnjs.cloudflare.com/ajax/libs/jquery.touchswipe/1.6.4/jquery.touchSwipe.min.js
//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js
//cdnjs.cloudflare.com/ajax/libs/jquery.touchswipe/1.6.4/jquery.touchSwipe.min.js
$(".carousel").swipe({

	swipe: function(event, direction, distance, duration, fingerCount, fingerData) {
  
	  if (direction == 'left') $(this).carousel('next');
	  if (direction == 'right') $(this).carousel('prev');
  
	},
	allowPageScroll:"vertical"
  
  });

  
 /*navbar*/ 

  const menuToggle = document.getElementById('menu-toggle');
  const menu = document.getElementById('menu');
  
  menuToggle.addEventListener('click', () => {
	if (menu.style.display === 'block' || menu.style.display === '') {
	  menu.style.display = 'none';
	} else {
	  menu.style.display = 'block';
	}
  });
  
 