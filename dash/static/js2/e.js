/******** Chat Box ******/
function rightSide() {
  if($(window).width() <= 992) {
    $('.left-chat').hide(300);
    $('.right-chat').show(300);
    $('.right-chat').removeClass('chat-sizes');
    $('.right-chat').addClass('w-97');

} else {
    $('.left-chat').show(300);
    $('.right-chat').show(300);
    $('.right-chat').addClass('chat-sizes');
    $('.right-chat').removeClass('w-97');
  }
}
$('.back-btn').click(function(){
  $('.left-chat').show(300);
  $('.right-chat').hide(300);
})



$('.sent-btn').click(function(){
  $(this).addClass('text-white nav-icon-bg-color').removeClass('nav-icon-color');
  $('.recieved-btn').removeClass('text-white nav-icon-bg-color').addClass('nav-icon-color');

  setTimeout(function(){
    $('.recieved_req').fadeOut();
  },200);
  setTimeout(function(){
    $('.sent-req').fadeIn();
  },500);

});
$('.recieved-btn').click(function(){
  $(this).addClass('text-white nav-icon-bg-color').removeClass('nav-icon-color');
  $('.sent-btn').removeClass('text-white nav-icon-bg-color').addClass('nav-icon-color');
  setTimeout(function(){
    $('.sent-req').fadeOut();
  },200);
  setTimeout(function(){
    $('.recieved_req').fadeIn();
  },500);

});
/**** Slide-in-out in navbar ****/

$('.slide-in').click(function(){
    $('.left').hide(300);  
    $('.right').css({width:'100%'});
    $('.slide-out').show(300);
    $(this).hide(300);
});
$('.slide-out').click(function(){
  $('.left').show(300); 
  $('.right').css({width:'85%'});  
  $(this).hide(300)
  $('.slide-in').show(300);
});

/******** For DropDown Menu  ******/

$('.dropdown').click(function(){
  $('.dropdown-menu').toggle(300);

})

$('.dropdown2').click(function(){
  $('.dropdown-menu2').toggle(300);

})


function success() {
    const Toast = Swal.mixin({
        toast: false,
        position: 'center',
        showConfirmButton: false,
        timer: 3500
      })
      Toast.fire({
        type: 'success',
        title: 'Edit Done Succefully'
      })
}

function addPatientSuccessfully() {
  const Toast = Swal.mixin({
      toast: false,
      position: 'center',
      showConfirmButton: false,
    })
    Toast.fire({
      type: 'success',
      title:'<a href="upload-claims.html" class="text-primary ml-5"><span style="color:#333 !important">" Patient Added Successfylly " </span> "press here To Add New Patient "</a> '
    })
}



function success5() {
  const Toast = Swal.mixin({
      toast: false,
      position: 'center',
      showConfirmButton: false,
      timer: 3500
    })
    Toast.fire({
      type: 'success',
      title: 'Payment Uploaded Succesfully'
    })
}

function accept() {
  const Toast = Swal.mixin({
      toast: false,
      position: 'center',
      showConfirmButton: false,
      timer: 3500
    })
    
    Toast.fire({
      type: 'success',
      title: 'Request Accepted successfully'
    })
}
function Canceled() {
  const Toast = Swal.mixin({
      toast: false,
      position: 'center',
      showConfirmButton: false,
      timer: 3500
    })
    
    Toast.fire({
      type: 'success',
      title: 'Request Refused successfully'
    })
}
function complain() {
  const Toast = Swal.mixin({
      toast: false,
      position: 'center',
      showConfirmButton: false,
      timer: 3500
    })
    
    Toast.fire({
      type: 'success',
      title: 'Compain Sent successfully'
    })
}

function success2() {
    const Toast = Swal.mixin({
        toast: false,
        position: 'center',
        showConfirmButton: false,
        timer: 5500
      })
      
      Toast.fire({
        type: 'success',
        title: '4SOFT has received your request successfully and we will answer soon'
      })
}

function success3() {
  const Toast = Swal.mixin({
      toast: false,
      position: 'center',
      showConfirmButton: false,
      timer: 3000
    })
    
    Toast.fire({
      type: 'success',
      title: 'Updated successfully'
    })
}




$(window).on("scroll",function(){
    if($(window).scrollTop()>=300)
    {
        $('#goUPButton').slideDown(700);
    }
    else
    {
        $('#goUPButton').slideUp(700); 
    }
}) ;
function goUP(){
    window.scrollTo(0,0); 
};
$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {
    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();
      // Store hash
      var hash = this.hash;
      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 1200, function(){
   
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});








