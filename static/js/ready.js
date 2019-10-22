$(document).ready(function () {
    console.log('Document is ready');

    // lissener for modal Add post
    $(".new_post_button").on("click", function () { $("#modal_fixed_overlay_add_post")
                                                        .css("display", "block")});
    $("#modal_fixed_overlay_add_post span.icon-close").on("click", closeModalCreatePost);

    // Topic
    countTopic();

//    render Posts
    getPosts();

});
$(function(){
    $(window).resize(function() {
//          console.log( $(window).height() );
    })
})