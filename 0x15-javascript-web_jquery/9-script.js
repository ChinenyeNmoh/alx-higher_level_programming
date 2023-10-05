$(document).ready(function () {
  $.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    dataType: "json",
    success: function (data) {
      $("#hello").text(data.hello);
    },
    error: function (err) {
      console.log(err);
    }
  });
});