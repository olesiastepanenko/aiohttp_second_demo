function getPosts(){
       $.ajax({
        type: "GET",
        url: "/show_posts",
        dataType: "json"
    })
    .done(posts => {
        console.log("posts", posts)
        posts.forEach(post => renderPost(post))
    })
    .fail( () => {
        console.log("error")
    })
}
function renderPost(post) {
    let title = $("<div />").addClass("post_title").text(post.title);
    let image = $("<img />").addClass("post_image").attr("src", post.image);
//    let text = $("<div />").addClass("post_text").text(post.post_text);
//    let date = $("<div />").addClass("post_date").text(post.date_created);

    $("<div />").addClass("post_body")
        .append([image, title])
        .appendTo("#content")
}


function countTopic() {
    console.log('count hier');
    $.ajax({
        type: "GET",
        url: "/count_topic",
        dataType: "json"
    })
    .done(topics => {
        topics.forEach(function(element) {
                                        $("."+element._id).children(':first')
                                                          .text(element.count)
                                         })
    })
    .fail( () => {
        console.log("error")
    })
}




