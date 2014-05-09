$(function() {
    var socket = io.connect('/chat');
    socket.on('connect', function() {
        alert('connected to chat server');
    });
    var $messages = $('#messages');
    var tplStatus = '{{status}}';
    var tplUser = '{{user}}';
    var tplText = '{{text}}';
    var template = '<div class="bg-'+tplStatus+'">'+tplUser+': '+tplText+'</div>';
    var seqID = 0;
    function getMessages() {
        $.ajax({
            url: '/get_messages/'+seqID,
            processData: false,
            contentType: 'application/json',
        	dataType: 'json',
            success: function(data) {
                for ( var i = 0; i < data.messages.length; i++ ) {
                    var messageText = data.messages[i].text;
                    var username = data.messages[i].username;

                    var status = i % 2 == 0 ? 'danger' : 'success';

                    var html = template.replace(new RegExp(tplStatus), status);
                    html = html.replace(new RegExp(tplUser), username);
                    html = html.replace(new RegExp(tplText), messageText);

                    $messages.append(html);
                }
            },
            error: function(data) {
                $messages.html('<div class="bg-danger">An error has occurred.  Please refresh and try again</div>');
            }
        });
    }
    var count = 0;
    while ( true ) {
        timeoutID = window.setTimeout(getMessages, 2000);
        count++;
        if ( count > 1 ) {
            break;
        }
    }
}); 
