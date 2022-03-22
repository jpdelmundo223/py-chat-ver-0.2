// Get server url
var serverURL = "http://127.0.0.1:5000/";

// Initialize socket
var socket = io(serverURL);

// Globals
let username = "";
let room = "";
let entered_room = "";

// Test connection
socket.on("connect", function () {
  console.log("Socket IO is now running...");
  // socket.send("User is connected!");
  socket.send({
    message: "Some Message",
    username: "jpdelmundo",
    room: "112002354534",
  });
});

socket.on("message", function (data) {
  $("#messages-list").append(`<li>${data.message}</li>`);
});

function sendMessage(msg) {
  socket.send({
    message: msg,
    username: "jpdelmundo",
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
  sendMessage(message_text);
  $("#message-text").val("").focus();
});

// Login form validations

$(document).ready(function () {
  $("a#user").each(function () {
    $(this).click(function () {
      username = "jpdelmundo";
      room = $(this).text();
      if (room == entered_room) {
        console.log("You are already in the room.");
      } else {
        leaveRoom(username, entered_room);
        joinRoom(username, room);
        entered_room = $(this).text();
        $("#message-text").val("").focus();
      }
    });
  });
});

$("#message-text").keyup(function (e) {
  e.preventDefault();
  // The send function will fire if the user press 'Enter' from the message text area field
  if (e.keyCode == 13) {
    e.preventDefault();
    var message_text = $("#message-text").val();
    console.log(message_text);
    sendMessage(message_text);
    $("#message-text").val("").focus();
  } else {
    // Nothing happens
  }
});
