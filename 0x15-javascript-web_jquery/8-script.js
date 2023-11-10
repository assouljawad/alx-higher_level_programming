/* global $ */
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    data.results.forEach((e, i) => {
      $('UL#list_movies').append('<li>' + e.title + '</li>');
    });
  });
});
