$('.language-selector a').on('click',  function() {
    lang = $(this).attr('data')
    document.cookie = 'language='+lang
    document.location.reload(true)
})