
$(window).load(function(){
    logoWings();
    placeBoats();
});
$(window).resize(function(){
    logoWings();
    placeBoats();
})


function logoWings(){
    refW = $('#logo').width();
    W = (refW - $('#logo img').outerWidth())/2 - 5;
    $('.logo_wing').each(function(){
        $(this).width(W);
    });
}

function placeBoats(){
    W = $(window).width();
    currentLeft = 0;
    itemW = $('.boat_container:first').outerWidth();
    itemCount = $('.boat_container').length;
    if(W > 1050 && itemCount <= 7){
        currentLeft = ( $(window).width() - (itemW*itemCount + 20*(itemCount-1)) )/2;
        $('.boat_container').each(function(){
            $(this).css('left',currentLeft);
            currentLeft += $(this).outerWidth() + 20;
        });
    }
}