function rvalidate(){
	var fname=document.registration.fname.value;
	var lname=document.registration.lname.value;
	var email=document.registration.email.value;
	var contact=document.registration.contact.value;
	var password=document.registration.password.value;
	var cpassword=document.registration.cpassword.value;
	var flag=true;
	
	if(fname=="" || lname=="" || contact.length!=10 ||email=="" || password=="" || cpassword=="" || password!=cpassword){
		if(fname==""){
				document.getElementById('fname').innerText="field should not be empty";
			}
		if(lname==""){
				document.getElementById('lname').innerText="field should not be empty";
			}
		if(email==""){
				document.getElementById('email').innerText="field should not be empty";
			}
		if(contact.length!=10){
				document.getElementById('contact').innerText="Contact no to short or long";
			}
		if(password==""){
				document.getElementById('password').innerText="field should not be empty";
			}
		if(cpassword==""){
				document.getElementById('cpassword').innerText="field should not be empty";
			}
		if(password!=cpassword){
				document.getElementById('cpassword').innerText="password dosn't match";
			}
		alert("Validation Failed!");
		return false;
	}
	else{
		return true;
	}	
}
function lvalidate(){
	var email=document.Login.email.value;
	var password=document.Login.password.value;
	var flag=true;
	if(email=="" || password==""){
		if(email==""){
				document.getElementById('lemail').innerText="field should not be empty";
			}
		if(password==""){
				document.getElementById('lpassword').innerText="field should not be empty";
			}
		alert("Validation Failed!");
		return false;
	}
	else{
		return true;
	}	
}
function fvalidate(){
	var email=document.registration.email.value;
	var contact=document.registration.contact.value;
	var password=document.registration.password.value;
	var cpassword=document.registration.cpassword.value;
	var flag=true;
	
	if(contact.length!=10 || email=="" || password=="" || cpassword=="" || password!=cpassword){
		if(email==""){
				document.getElementById('femail').innerText="field should not be empty";
			}
		if(contact.length!=10){
				document.getElementById('fcontact').innerText="Contact no to short or long";
			}
		if(password==""){
				document.getElementById('fpassword').innerText="field should not be empty";
			}
		if(cpassword==""){
				document.getElementById('fcpassword').innerText="field should not be empty";
			}
		if(password!=cpassword){
				document.getElementById('fcpassword').innerText="password dosn't match";
			}
		alert("Validation Failed!");
		return false;
	}
	else{
		return true;
	}	
}
function check(id){
	document.getElementById(id).innerText="";
}

function slide() {
	document.getElementById('register').classList.toggle('hide');
	document.getElementById('login').classList.toggle('hide');
	document.getElementById('form-slide1').classList.toggle('active');
	document.getElementById('form-slide2').classList.toggle('active');
}
function forget(){
	document.getElementById('form-slide1').classList.toggle('hide');
	document.getElementById('form-slide2').classList.toggle('hide');
	document.getElementById('form-slide3').classList.toggle('hide');
	document.getElementById('form-slide3').classList.toggle('active');
	document.getElementById('login').classList.toggle('hide');
	document.getElementById('fpass').classList.toggle('hide');
}
function form_collapse(){
	document.getElementById('form').classList.toggle('m-fadeOut');
	document.getElementById('form').classList.toggle('m-fadeIn');
}

document.addEventListener("click", function() {
  if (document.getElementById('form').classList.contains('m-fadeIn')) {
  	document.addEventListener("click",function(){
  	form_collapse();
  	});
  	document.getElementById('form1').addEventListener("click",function() {
  		form_collapse();
  	});
  }
  document.getElementById('formlink').addEventListener("click",function(){
		form_collapse();
		if (document.getElementById('form-slide3').classList.contains('active')) {
  		forget();
  		slide();
  	}
  });
  
});
