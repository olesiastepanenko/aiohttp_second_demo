$(document).ready(function () {
    console.log('Document is ready');
    if (window.location.pathname =="/posts"){
    getPosts();
    } else if (window.location.pathname=="/"){
    countTopic();
    } else if(window.location.pathname.includes("/topic")){
//        console.log("hier", window.location.pathname);
        postsByTopic(window.location.pathname)
    } else if (window.location.pathname.includes("/recipe")){
        postById(window.location.pathname)
    };

    // lissener for modal Add post
    $(".new_post_button").on("click", function () { $("#modal_fixed_overlay_add_post")
                                                        .css("display", "block")});
    $("#modal_fixed_overlay_add_post span.icon-close").on("click", closeModalCreatePost);

//    $("#topic_wrapper").on("click", postsByTopic);





});


$(function(){
//    $(window).resize(function() {
////          console.log( $(window).height() );
//    })


//    console.log("window.location.pathname", window.location.pathname)

})
