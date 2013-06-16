$('.language-selector a').on('click',  function() {
    lang = $(this).attr('data')
    document.cookie = 'language='+lang
    document.location.reload(true)
})

$('#newsletter-signup-btn').on('click', function(e) {
    e.preventDefault()
    $(this).attr('disabled', 'disabled')
    var self = this
    var email = $('#newsletter-email').val()
    var token = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax('/newsletter',  {
        type: 'POST',
        data: { 'email': email, 'csrfmiddlewaretoken': token },
        statusCode: {
            400: function(res) {
                console.log(res.responseText)
                $('.newsletter-error').show()
                $('.newsletter-already').hide()
                $(self).removeAttr('disabled')
            },
            500: function(res) {
                $('.newsletter-error').hide()
                $('.newsletter-already').show()
                console.log(res.responseText)
                $(self).removeAttr('disabled')
            },
        },
        success: function() {
            $('#newsletter-signup input, #newsletter-signup button').hide()
            $('.newsletter-error').hide()
            $('.newsletter-already').hide()
            $('.newsletter-signedup').show()
            $(this).removeAttr('disabled')
        },
    })
})