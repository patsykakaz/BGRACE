
$('#loader .fa').css('top',($(window).height()-$('#loader .fa').outerHeight())/2);
$('#loader .fa').css('left',($(window).width()-$('#loader .fa').outerWidth())/2);

$(window).load(function(){
    logoWings();
    BoatPlacing();
    BoatHover();
});
$(window).resize(function(){
    $('#loader .fa').css('top',($(window).height()-$('#loader .fa').outerHeight())/2);
    $('#loader .fa').css('left',($(window).width()-$('#loader .fa').outerWidth())/2);
    logoWings();
    BoatPlacing();
    BoatHover();
})


function logoWings(){
    refW = $('#logo').width();
    W = (refW - $('#logo img').outerWidth())/2 - 5;
    $('.logo_wing').each(function(){
        $(this).width(W);
    });
}

function placeBoats(){
    WW = $(window).width();
    itemW = $('.boat_container:first').outerWidth();
    itemH = $('.boat_container:first').outerHeight();
    itemCount = $('.boat_container').length;
    cursor = 10;
    margin_right = 15;
    
    // Adapt #boats container Height() due to absolute positioning
    X = (Math.floor(itemCount/cursor)+1)*(itemH)+180;
    $('#boats').css('height', X)


    // Ruler to add to boat_container.left
    // in order to center them 
    if(itemCount < cursor){
        leftRuler = ($('#boats').width()-(itemCount*itemW+(itemCount-2)*margin_right))/2;
    }else{
        leftRuler = ($('#boats').width()-(cursor*itemW+(cursor-2)*margin_right))/2;
    }

    if(WW > 1050){
        $('.boat_container').each(function(){
            if($(this).index() < cursor ){
                $(this).css('left',leftRuler+(itemW+margin_right)*($(this).index()))
                    .css('bottom',X/2);
            }else{
                column = $(this).index() % cursor;
                line = Math.floor($(this).index()/cursor);
                $(this).css('left',leftRuler+(itemW+margin_right)*column)
                    .css('bottom',X/2-(itemH+30)*line);
            }
        });
    }else if(true){

    }
}

function BoatPlacing(){
    if($('#loader').css('display') != "block"){
        $('#loader').fadeIn('fast');
    }
    minW = 175;
    windowW = $(window).width();
    boatCounter = $('.boat_container').length;
    if(windowW>991){
        margin = 15;
    }
    else if (windowW > 768){
        margin = 8;   
    }


    if(windowW>768){
        W = ($('#boats').width()-(boatCounter-1)*margin) / boatCounter;
        $('.boat_container').each(function(){
            $(this).outerWidth(W)
                .height(W*0.75)
                .css('left', margin+(W+margin)*$(this).index());
            boat_box = $(this).children('.boat_box');
            boat_box.width(W-20);
            H = boat_box.children('img').outerHeight() + boat_box.children('h4').outerHeight() + $(this).children('h4').outerHeight();
            boat_box.height(H);
            boat_box.attr('fold_size',H)

        });
        $('.boat_container').css('bottom',W*0.2);
        $('#boats').outerHeight(W*1.25);
    }
    else{
        console.log('get responsive')
    }
    $('#loader').fadeOut('slow');
}


function BoatHover(){
    $('.boat_container').mouseover(function(){
        boat_box = $(this).children('.boat_box');
        FullHeight = boat_box.children('img').height()+boat_box.children('.boat_title').outerHeight()+$(this).children('h5').outerHeight();
        $(this).height(FullHeight);
    });
    $('.boat_container').mouseout(function(){
        $(this).height($(this).outerWidth()*0.75);
    });
}






