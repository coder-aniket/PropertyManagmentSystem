$(document).ready(function(){
$('#bs-example-navbar-collapse-2 ul').on('click','li a',function(){
$('#bs-example-navbar-collapse-2 ul li a.active_tab').removeClass('active_tab');
$(this).addClass('active_tab');
$('#main_pannel>div').addClass('hide');
if (this.id==1) {
	$('#profile').removeClass('hide');
}
else if (this.id==2) {
	// $('#main_pannel>div').addClass('hide');
	$('#enquiry').removeClass('hide');
}
else if (this.id==3) {
	// $('#main_pannel>div').addClass('hide');
	$('#wishlist').removeClass('hide');
}
else if (this.id==4) {
	// $('#main_pannel>div').addClass('hide');
	$('#broker').removeClass('hide');
}
else if (this.id==5) {
	// $('#main_pannel>div').addClass('hide');
	$('#user').removeClass('hide');
}

});

});