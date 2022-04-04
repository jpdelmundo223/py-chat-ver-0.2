// Get server url
var devURL = "http://127.0.0.1:5000/";
var prodURL = "http://192.168.254.100:5000/";

// Initialize socket
var socket = io("http://127.0.0.1:5000/");

// Globals
let username = "";
let username1 = "";
let room = "";

let jples = "jplesroom";
let jromeles = "jromelesroom";
let jpjrome = "jpjromeroom";

let entered_room = "";
let random_room = Math.floor(Math.random() * 99999999999);

let sender = "";
let receiver = "";

console.log(random_room);

// Test connection
socket.on("connect", function () {
  console.log("Socket IO is now running...");
  // socket.send("User is connected!");
  // socket.send({
  //   message: "Some Message",
  //   username: "jpdelmundo",
  //   room: "112002354534",
  // });
});

socket.on("message", function (data) {
  $("#messages-list").append(
    `<li class="message message-sent" style="height: auto;">${data.message}</li>`
  );
});

socket.on("room response", function (data) {
  console.log(data);
});

function sendMessage(msg, room) {
  socket.send({
    message: msg,
    username: sender,
    room: room,
  });
}

function joinRoom(username, room) {
  socket.emit("join_room", { username: username, room: room });
}

function leaveRoom(username, room) {
  socket.emit("leave_room", { username: username, room: room });
}

$("#send-message").click(function (e) {
  e.preventDefault();
  var message_text = $("#message-text").val();

  console.log(message_text);

  sender = $("#current-user").text();
  if (sender == "jpdelmundo" && receiver == "lesvelarde") {
    sendMessage(message_text, jples);
  } else if (sender == "jpdelmundo" && receiver == "jeromedelmundo") {
    sendMessage(message_text, jpjrome);
  } else if (sender == "lesvelarde" && receiver == "jpdelmundo") {
    sendMessage(message_text, jples);
  } else if (sender == "lesvelarde" && receiver == "jeromedelmundo") {
    sendMessage(message_text, jromeles);
  } else if (sender == "jeromedelmundo" && receiver == "jpdelmundo") {
    sendMessage(message_text, jpjrome);
  } else if (sender == "jeromedelmundo" && receiver == "lesvelarde") {
    sendMessage(message_text, jromeles);
  }

  $("#message-text").val("").focus();
});

// Login form validations

$("span#user").each(function () {
  $(this).click(function () {
    sender = $("span#current-user").text();
    receiver = $(this).text();
    if (sender == "jpdelmundo" && receiver == "lesvelarde") {
      leaveRoom(sender, jromeles);
      leaveRoom(sender, jpjrome);
      joinRoom(sender, jples);
    } else if (sender == "jpdelmundo" && receiver == "jeromedelmundo") {
      leaveRoom(sender, jromeles);
      leaveRoom(sender, jples);
      joinRoom(sender, jpjrome);
    } else if (sender == "lesvelarde" && receiver == "jpdelmundo") {
      leaveRoom(sender, jromeles);
      leaveRoom(sender, jpjrome);
      joinRoom(sender, jples);
    } else if (sender == "lesvelarde" && receiver == "jeromedelmundo") {
      leaveRoom(sender, jpjrome);
      leaveRoom(sender, jples);
      joinRoom(sender, jromeles);
    } else if (sender == "jeromedelmundo" && receiver == "jpdelmundo") {
      leaveRoom(sender, jromeles);
      leaveRoom(sender, jples);
      joinRoom(sender, jpjrome);
    } else if (sender == "jeromedelmundo" && receiver == "lesvelarde") {
      leaveRoom(sender, jpjrome);
      leaveRoom(sender, jples);
      joinRoom(sender, jromeles);
    }

    $("#messages-list").empty();
  });
});

// $(document).ready(function () {
//   $("a#user").each(function (index, element) {
//     $(this).click(function () {
//       username = $(this).text();
//       room = $(this).text();
//       if (room == entered_room) {
//         console.log("You are already in the room.");
//       } else {
//         leaveRoom(username, entered_room);
//         joinRoom(username, room);
//         entered_room = $(this).text();
//         $("#message-text").val("").focus();
//         $("#messages-list").empty();
//       }
//     });
//   });
// });

$("#message-text").keyup(function (e) {
  e.preventDefault();
  if (e.keyCode == 13) {
    e.preventDefault();
    var message_text = $("#message-text").val();

    console.log(message_text);
    sender = $("#current-user").text();
    if (sender == "jpdelmundo" && receiver == "lesvelarde") {
      sendMessage(message_text, jples);
    } else if (sender == "jpdelmundo" && receiver == "jeromedelmundo") {
      sendMessage(message_text, jpjrome);
    } else if (sender == "lesvelarde" && receiver == "jpdelmundo") {
      sendMessage(message_text, jples);
    } else if (sender == "lesvelarde" && receiver == "jeromedelmundo") {
      sendMessage(message_text, jromeles);
    } else if (sender == "jeromedelmundo" && receiver == "jpdelmundo") {
      sendMessage(message_text, jpjrome);
    } else if (sender == "jeromedelmundo" && receiver == "lesvelarde") {
      sendMessage(message_text, jromeles);
    }

    $("#message-text").val("").focus();

    $("#message-text").val("").focus();
  } else {
    // Nothing happens
  }
});

// $("#message-text").keydown(function(e) {
//   if (e.ctrlKey && e.keyCode == 13) {
//     alert("Ctrl + Enter pressed!");
//   }
//   // The send function will fire if the user press 'Enter' from the message text area field
//   else
// })
