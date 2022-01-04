var socket = io();

socket.on("msg", function (data) {
    chat = document.getElementById("chat");
    msg = document.createElement("li");
    msg.innerText = data['username'] + ': ' + data['msg'];
    chat.appendChild(msg);
    window.scrollTo(0,document.body.scrollHeight);
});

function send() {
    msgbox = document.getElementById("msg");
    socket.emit("msg", {"msg": msgbox.value, "username": username})
    msgbox.value = "";
};

document.getElementById('msg').onkeydown = function(e){
    if(e.keyCode == 13){
      send();
    }
 };