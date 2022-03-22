console.log("main.js is running...");

$(document).ready(function () {
  $("#login-form").submit(function (e) {
    // Get the value of hidden csrf_token
    var csrf_token = $("input[name=csrf_token]").val();

    e.preventDefault();

    $.ajax({
      type: "POST",
      url: "/login-user",
      beforeSend: function (xhr) {
        xhr.setRequestHeader("X-CSRF-Token", csrf_token);
      },
      data: {
        username: $("#username").val(),
        password: $("#password").val(),
        csrf_token: csrf_token,
      },
    }).done(function (response) {
      if (response.data.status == "success") {
        window.location.replace("/messages");
      } else {
        console.log(response.data);
      }
    });
  });

  $("#username").keyup(function (e) {
    var username = $("#username").val();
    if (username.length > 0) {
      $("#username-form-validation").css("display", "none");
    } else {
      $("#username-form-validation").css("display", "block");
    }
  });

  $("#password").keyup(function (e) {
    var password = $("#password").val();
    if (password.length > 0) {
      $("#password-form-validation").css("display", "none");
    } else {
      $("#password-form-validation").css("display", "block");
    }
  });
});

$(document).ready(function () {
  $("a#user").each(function (index, element) {
    $(this).click(function () {
      $("a#user").each(function (index, element) {
        $(this).removeClass(" active");
      });
      $(this).addClass(" active");
    });
  });
});

