$(document).ready(function () {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    success: function (data) {
      for (var i = 0; i < data.results.length; i++) {
        var t = data.results[i];
        $("#list_movies").append('<li>' + t.title + '</li>');
    }
    },
    error: function (err) {
      console.log(err);
    }
  });
});