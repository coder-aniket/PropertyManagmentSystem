$(document).ready(function(){
/*****Fixed Menu******/
var secondaryNav = $('.cd-secondary-nav'),
   secondaryNavTopPosition = secondaryNav.offset().top;
	$(window).on('scroll', function(){
		if($(window).scrollTop() > secondaryNavTopPosition) {
			secondaryNav.addClass('is-fixed');	
		} else {
			secondaryNav.removeClass('is-fixed');
		}
	});		
	/*****Responsive Menu******/
	
		$(window).on('resize', function(){
			if($(window).width() < 768 ) {
				$('#login_a').removeClass('hide');
				$('#user_drop').addClass('hide');
			} else {
				$('#login_a').addClass('hide');
				$('#user_drop').removeClass('hide');
			}
		});
		$(window).on('load', function(){
			if($(window).width() < 768 ) {
				$('#login_a').removeClass('hide');
				$('#user_drop').addClass('hide');
			} else {
				$('#login_a').addClass('hide');
				$('#user_drop').removeClass('hide');
			}
		});
		if ($('#login_a').hasClass('active_tab') || $('#user_drop').hasClass('active_tab')) {
			$(window).on('resize', function(){
			if($(window).width() < 768 ) {
				$('#login_a').addClass('active_tab');
				$('#user_drop').removeClass('active_tab');
			} else {
				$('#login_a').removeClass('active_tab');
				$('#user_drop').addClass('active_tab');
			}
		});
		$(window).on('load', function(){
			if($(window).width() < 768 ) {
				$('#login_a').addClass('active_tab');
				$('#user_drop').removeClass('active_tab');
			} else {
				$('#login_a').removeClass('active_tab');
				$('#user_drop').addClass('active_tab');
			}
		});
		}

});

function img_submit(){
	$("#img_submit").trigger("click");
}


