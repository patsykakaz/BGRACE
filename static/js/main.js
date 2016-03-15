
$('#loader .fa').css('top',($(window).height()-$('#loader .fa').outerHeight())/2);
$('#loader .fa').css('left',($(window).width()-$('#loader .fa').outerWidth())/2);

$(document).ready(function(){
    if($('#liner').hasClass('red') || !$('#liner').length){
        $('form>.form-group>input.form-control').addClass('red');
    }
    $('#searchScreen form').css('margin-top',($(window).height()-$('#searchScreen form').outerHeight())/2);
    $('#btn-search').click(function(){
        $("#searchScreen").fadeIn();
        $('#searchScreen .form-control').focus();
    });
    $("#btn-search-close").click(function(){
        $("#searchScreen").fadeOut();
    });
});

$(window).load(function(){
    logoWings();
    carouselCaption();
    BoatPlacing();
    BoatHover();
    $('#loader').fadeOut('slow');
});
$(window).resize(function(){
    $('#loader .fa').css('top',($(window).height()-$('#loader .fa').outerHeight())/2)
            .css('left',($(window).width()-$('#loader .fa').outerWidth())/2);
    logoWings();
    carouselCaption();
    BoatPlacing();
    BoatHover();
})


function logoWings(){
    refW = $('#logo').width();
    W = (refW - $('#logo img').outerWidth())/2 - 10;
    $('.logo_wing').each(function(){
        $(this).width(W);
    });
}

function carouselCaption(){
    padding = 10;
    $('.carousel-caption').height($('.carousel_caption_title').outerHeight()+$('.carouse-caption p').outerHeight()+2*padding);
    $('.carousel-caption').width($('.carousel_caption_title').outerWidth()+$('.carouse-caption p').outerWidth()+2*padding);
}

function BoatPlacing(){
    minW = 175;
    windowW = $(window).width();
    boatCounter = $('.boat_container').length;
    if(windowW>991){
        margin = 15;
    }
    else if (windowW > 768){
        margin = 8;   
    }
    else if (windowW < 768){
        margin = 15;   
    }

// REDO
    // issue with title.height() when length too high
    x = 0;
    $('.boat_title').each(function(){
        if($(this).height()>x){
            x = $(this).height();
        }
    });
    $('.boat_title').height(x);
// ./REDO

    if(windowW>768){
        W = ($('#boats').width()-(boatCounter-1)*margin) / boatCounter;
        $('.boat_container').each(function(){
            $(this).outerWidth(W)
                .height(W*0.8)
                .css('left', margin+(W+margin)*$(this).index());
            boat_box = $(this).children('.boat_box');
            boat_box.width(W-20);
            H = boat_box.children('img').outerHeight() 
                + boat_box.children('h4').outerHeight()
                + $(this).children('h4').outerHeight();
            boat_box.height(H);
            boat_box.attr('fold_size',H)

        });
        $('.boat_container').css('bottom',W*0.2);
        $('#boats').outerHeight(W*1.25);
    }else{
        if(windowW > 544){
            boatsPerCol = 3;
        }else{
            boatsPerCol = 2;
        }
        W = ($('#boats').width()-(boatsPerCol-1)*margin) / boatsPerCol;
        $('.boat_container').each(function(){
            $(this).outerWidth(W)
                .height(W*0.8)
                .css('left', margin+W*($(this).index()%boatsPerCol)+margin*($(this).index()%boatsPerCol));
            boat_box = $(this).children('.boat_box');
            boat_box.width(W-20);
            H = boat_box.children('img').outerHeight() + boat_box.children('h4').outerHeight() + $(this).children('h4').outerHeight();
            boat_box.height(H);
            boat_box.attr('fold_size',H)
            $(this).css('bottom', W*0.2+ Math.floor($(this).index()/boatsPerCol)*W);
        });
        $('#boats').outerHeight(W*0.2+W*Math.floor($('.boat_container').length/boatsPerCol));  
    }
}


function BoatHover(){
    $('.boat_container').mouseover(function(){
        boat_box = $(this).children('.boat_box');
        FullHeight = boat_box.children('img').height()+boat_box.children('.boat_title').outerHeight()+$(this).children('h5').outerHeight();
        $(this).height(FullHeight);
    });
    $('.boat_container').mouseout(function(){
        $(this).height($(this).outerWidth()*0.8);
    });
}






