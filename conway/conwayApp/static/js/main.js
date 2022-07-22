$(document).ready(function() {
    var running = false;
    var canUpdate = true;
    var size = 5;
    var grid = [];
    var interval = 1000;
    
    function initGrid(n) {
        grid = [];
        for(var i = 0; i < n; i++) {
            var row = $('<div>', {class: 'row'});
            var arrRow = [];
            for(var j = 0; j < n; j++) {
                var cell = $('<div>', {
                    id: i + '-' + j,
                    class: 'cell dead'
                }).appendTo(row);
                arrRow.push(0);
            }
            $('#grid').append(row);
            grid.push(arrRow);
        }
    }

    function getNextGrid() {
        $.ajax({
            type: 'GET',
            url: 'next',
            data: {grid: JSON.stringify(grid)},
            success: function(response) {
                grid = response.grid;
                canUpdate = response.canUpdate;
                for(var i = 0; i < size; i++) {
                    for(var j = 0; j < size; j++) {
                        var cell = $('#' + i + '-' + j);
                        if(grid[i][j] == 0) {
                            if(cell.hasClass('alive')) {
                                cell.removeClass('alive');
                                cell.addClass('dead');
                            }
                        }
                        else {
                            if(cell.hasClass('dead')) {
                                cell.removeClass('dead');
                                cell.addClass('alive');
                            }
                        }
                    }
                }
            },
            complete: function(data) {
                if(canUpdate && running)
                    setTimeout(getNextGrid, interval);
            }
        });
    }
    
    $('#size_submit').click(function(e) {
        size = $('#size').val();
        $('#grid').empty();
        initGrid(size);
    });
    
    $('#start_stop').click(function(e) {
        canUpdate = true;
        running = !running;
    
        if(running) {
            $(e.target).html("Stop");
            $('.cell').each(function() {
                $(this).css("cursor", "auto");
            })
            getNextGrid();
        }
        else {
            $(e.target).html("Start");
            $('.cell').each(function() {
                $(this).css("cursor", "pointer");
            })
        }
    });

    $('#next').click(function(e) {
        running = false;
        $('#start_stop').html("Start");
        if(canUpdate)
            getNextGrid();
    });
    
    $('#clear').click(function(e) {
        $('#grid').empty();
        initGrid(size);
    });
    
    $('#grid').on('click', '.cell', function(e) {
        if(!running) {
            var id = ($(e.target).attr('id')).split('-');
            if($(e.target).hasClass('dead')) {
                $(e.target).removeClass('dead');
                $(e.target).addClass('alive');
                grid[id[0]][id[1]] = 1;
            }
            else {
                $(e.target).removeClass('alive');
                $(e.target).addClass('dead');
                grid[id[0]][id[1]] = 0;
            }
        }
    });

    initGrid(size);
});

