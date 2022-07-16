running = false;

$('#start_stop').click(function(e) {
    running = !running;
    $('#run').html(running.toString());

    if(running) {
        $(e.target).html("Stop");
        $('.cell').each(function() {
            $(this).css("cursor", "auto");
        })
    }
    else {
        $(e.target).html("Start");
        $('.cell').each(function() {
            $(this).css("cursor", "pointer");
        })
    }
});

$('#reset').click(function(e) {
    $('.cell').each(function() {
        if($(this).hasClass('alive')) {
            $(this).removeClass('alive');
            $(this).addClass('dead');
        }
    })
});

$('.cell').click(function(e) {
    if(!running) {
        if($(e.target).hasClass('dead')) {
            $(e.target).removeClass('dead');
            $(e.target).addClass('alive');
        }
        else {
            $(e.target).removeClass('alive');
            $(e.target).addClass('dead');
        }
    }
});