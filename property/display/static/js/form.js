function validate(){
  if ($('#form').hasClass('m-fadeIn'))
  {
    var flag=0;

    if($("input[name='email']").val()==""){
        $("input[name='email']").next("span").text("field should not be empty");
        $("input[name='email']").addClass("input_warning");
        flag=1;
      }
    if($("input[name='password']").val()==""){
        $("input[name='password']").next("span").text("field should not be empty");
        $("input[name='password']").addClass("input_warning");
        flag=1;
      }
     if($("input[name='password']").val().length<8 || $("input[name='password']").val().length>15){
        $("input[name='password']").next("span").text("Password must be 8-15 characters");
        $("input[name='password']").addClass("input_warning");
        flag=1;
      } 
    if ($("input[type='submit']").not('.hide').val()!="Log In") {
      if($("input[name='contact']").val().length!=10){
        $("input[name='contact']").next("span").text("Contact no to short or long");
        $("input[name='contact']").addClass("input_warning");
        flag=1;
        }
      if($("input[name='cpassword']").val()==""){
          $("input[name='cpassword']").next("span").text("field should not be empty");
          $("input[name='cpassword']").addClass("input_warning");
          flag=1;
        }
      if($("input[name='password']").val()!=$("input[name='cpassword']").val()){
          $("input[name='cpassword']").next("span").text("password dosn't match");
          $("input[name='cpassword']").addClass("input_warning");
          flag=1;
        }
      if ($("input[type='submit']").not('.hide').val()=="Register") {
        if($("input[name='fname']").val()==""){
          $("input[name='fname']").next("span").text("field should not be empty");
          $("input[name='fname']").addClass("input_warning");
          flag=1;
        }
        if($("input[name='lname']").val()==""){
          $("input[name='lname']").next("span").text("field should not be empty");
          $("input[name='lname']").addClass("input_warning");
          flag=1;
        }
      }
    }
    
    if (flag==1) {
      alert("Validation Failed");
      return false;
    }
    else{
      return true;
    }
  }

}

$(document).ready(function(){
  $(".nav-item").click(function(){
    $(".nav-item").removeClass('active');
    $(this).addClass('active');
    if ($(this).is("#register-tab")) {
      $("input[disabled='disabled']").parent().removeClass("hide");
      $(".rfield").removeAttr("disabled");
      $("input[type='submit']").addClass("hide");
      $(".fbutton").addClass("hide");
      $("input[value='Register']").removeClass("hide");
      $("span").text("")
      $("form").attr('action', '/register/');
    }
    else if ($(this).is('#login-tab')) {
      $(".rfield").attr('disabled', 'disabled');
      $(".lfield").removeAttr("disabled");
      $("input[disabled='disabled']").parent().addClass("hide");
      $("input[type='submit']").addClass("hide");
      $("input[value='Log In']").removeClass("hide");
      $(".fbutton").removeClass("hide");
      $(".lbutton").addClass("hide");
      $("span").text("")
      $("form").attr('action', '/login/');
    }
  });
  $(".fbutton").click(function(){
    $(".rfield").removeClass("hide");
    $(".rfield").attr('disabled', 'disabled');
    $("input[disabled='disabled']").parent().removeClass("hide");
    $(".ffield").removeAttr("disabled");
    $("input[disabled='disabled']").parent().addClass("hide");
    $("input[type='submit']").addClass("hide");
    $(".fbutton").addClass("hide");
    $("input[value='Reset Password']").removeClass("hide");
    $(".lbutton").removeClass("hide");
    $(".nav-item").toggleClass("hide");
    $(".nav-item").removeClass("active");
    $(".nav-item:last").addClass("active");
    $("span").text("")
    $("form").attr('action', '/resetpass/');
  });
  $(".lbutton").click(function(){
    $("#login-tab").trigger( "click" );
    $(".nav-item").toggleClass("hide");
    // $(".nav-item:last").addClass("active");
    $("span").text("")
  });


  $("input").not(".btn").keypress(function() {
    $(this).next("span").text("");
  });

  function form_toggle(){ 
    $("#form").toggleClass("m-fadeOut");
    $("#form").toggleClass("m-fadeIn");
    $("input").removeClass("input_warning");
    $("input+span").text("");
  }

  $(".formlink").click(function(){
    form_toggle();
      if ($("#form").hasClass("m-fadeIn")) {
        if ($("#forget-tab").hasClass("active")) {
          $(".lbutton").trigger("click");
        }
        if ($("#login-tab").hasClass("active")) {
          $("#register-tab").trigger("click");
        }
      }
  });

  $("#form").click(function(){
    form_toggle();
  });

  $("#form1").click(function(){
    form_toggle();
  });
});

