/* global $ */
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?', function (data) {
    $('DIV#character').text(data.name);
  });
});
