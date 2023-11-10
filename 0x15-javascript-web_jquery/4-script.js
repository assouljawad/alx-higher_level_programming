/* global $ */
$('DIV#toggle_header').on('click', function () {
  const cls = $('header').hasClass('red');
  if (cls) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
