$(document).ready(function(){
$('#bs-example-navbar-collapse-2 ul').on('click','li a',function(){
$('#bs-example-navbar-collapse-2 ul li a.active_tab').removeClass('active_tab');
$(this).addClass('active_tab');
if (this.id==1) {
	$('#main_pannel>div').addClass('hide');
	$('#profile').removeClass('hide');
}
else if (this.id==2) {
	$('#main_pannel>div').addClass('hide');
	$('#enquiry').removeClass('hide');
}
else if (this.id==3) {
	$('#main_pannel>div').addClass('hide');
	$('#property').removeClass('hide');
}
else if (this.id==4) {
	$('#main_pannel>div').addClass('hide');
	$('#broker').removeClass('hide');
}
else if (this.id==5) {
	$('#main_pannel>div').addClass('hide');
	$('#user').removeClass('hide');
}

});

});