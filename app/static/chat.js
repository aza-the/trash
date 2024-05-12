document.getElementById('send-btn').addEventListener('click', sendMessage);

document.getElementById('message-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault(); 
        sendMessage();
    }
});

function sendMessage() {
    var input = document.getElementById('message-input');
    var message = input.value;
    input.value = ''; 

    if (message.trim() !== '') {
        displayMessage('Вы: ' + message);
        sendToServer(message);
    }
}

function displayMessage(message) {
    var messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    document.getElementById('message-container').appendChild(messageDiv);
}

function sendToServer(message) {
    setTimeout(() => { 
        displayMessage('Сервер: Эхо "' + message + '"');
    }, 500);
}
