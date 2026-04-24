$(document).ready(function() {
    $('#btn').click(function() {
        let userText = $('#txt').val();
        $.ajax({
            url: '/analyze',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({'text': userText}),
            success: function(res) {
                $('#w').text(res.words);
                $('#c').text(res.chars);
            }
        });
    });
});git init