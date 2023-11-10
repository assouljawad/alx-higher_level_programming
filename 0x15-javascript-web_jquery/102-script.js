/* global $ */
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $('DIV#hello').empty();
    const lang = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/?lang=' + lang,
      success: function (data) {
        $('DIV#hello').append(data.hello);
      }
    });
  });
});
