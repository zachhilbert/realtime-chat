$(function() {
    var $messages = $('#messages');
    var template = _.template('<p class="alert alert-<%= status %>"><%= user %>: <%= text %></p>');
    
    var chat = {
        connect: function(done) {
            var self = this;

            this.socket = io.connect('/chat');
            this.socket.on('connect', done);

            this.socket.on('message', function(message) {
                if ( self.onMessage ) {
                    self.onMessage(message);
                }
            });
        },
        
        join: function(nick, onJoin) {
            this.socket.emit('join', nick, onJoin);
        },
        
        sendMessage: function(message, onSent) {
            this.socket.emit('message', message, onSent);
        },

    };

    var displayAlert = function(message, type, callback, args) {
        $('.alert').addClass('alert-'+type);
        $('.alert').html(message);
        $('.alert').show();
        $('.alert').fadeOut(2000, function() {
            $('.alert').html('');
            $('.alert').removeClass('alert-'+type);
            if ( callback ) {
                callback(args);
            }
        });
    };

    var localDisplayMessage = function(message) {
        var status = message.sender == 'me' ?  'success':'danger';
        var html = template({status: status, user: message.sender, text: message.text});
        $messages.append(html);
    };

    var getMessages = function() {
        $.ajax({
        	url: '/get_messages',
        	type: 'GET',
            processData: false,
            contentType: 'application/json',
        	dataType: 'json',
            success: function(data) {
                _.each(data.messages, function(message) {
                    localDisplayMessage(message);
                });
            }
        });
    };

    var setup = function() {
        $('.form-signin').on('submit', function(e) {
            var self = this;
            e.preventDefault();
            chat.join($(this).find('[name="username"]').val(),
                function(joined, nick) {
                    if ( joined ) {
                        displayAlert('You have joined Coupon Chat!', 'success');//, getMessages);
                        $(self).hide();
                        $('#chatRoom').show();
                    }
                    else {
                        displayAlert('You have joined Coupon Chat!', 'success');
                    }
            });
        });
        
        // For enter button on message form
        $('[name="message-text"]').keypress(function (e) {
            if (e.which == 13) {
                e.preventDefault();
                var $textField = $('.message-form').find('[name="message-text"]');
                var iMessage = $textField.val();
                // clear for next message
                $textField.val('');
                chat.sendMessage(iMessage,
                    function(sent) {
                        if ( sent ) {
                            localDisplayMessage({text: iMessage, sender: 'me'});
                        }
                });
            }
        });

        chat.onMessage = function(message) {
            localDisplayMessage(message);
        };
    };
    
    // Start chat
    setup();
    chat.connect(function(){});
});
