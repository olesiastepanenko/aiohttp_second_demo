function getPosts(){
       $.ajax({
        type: "GET",
        url: "/api/show_posts",
        dataType: "json"
    })
    .done(posts => {
//        console.log("posts", posts)
        posts.forEach(post => renderPost(post))
    })
    .fail( () => {
        console.log("error")
    })
}
function renderPost(post) {
    let title = $("<div />").addClass("post_title").text(post.title);
    let image = $("<img />").addClass("post_image").attr("src", post.image);
    let link = $("<a />").attr("href", "/recipe/"+post._id).append([image, title]);
//    let text = $("<div />").addClass("post_text").text(post.post_text);
//    let date = $("<div />").addClass("post_date").text(post.date_created);

    $("<div />").addClass("post_body")
        .append(link)
        .appendTo("#content")
}

function renderPostDetails(post){
        let title = $("<div />").addClass("post_title_details");
        $("<span />").addClass("post_name").text(post.title).appendTo(title);
//        $("<span />").addClass("date_created").text(post.date_created).appendTo(title);
        let image = $("<img />").addClass("post_image_details").attr("src", post.image);
        let post_text = $("<div />").addClass("post_text_details").text(post.post_text);
        $("<div />").addClass("post_details")
                    .append([title, image, post_text])
                    .appendTo("#content")


}


function countTopic() {
    $.ajax({
        type: "GET",
        url: "/api/count_topic",
        dataType: "json"
    })
    .done(topics => {
//        console.log(topics);
        topics.forEach(function(element) {
//        console.log(element);
        let link = $("<a />")
                            .attr("href", "/topic/"+element._id);
        let span = $("<span />")
                            .addClass("topic_count")
                            .text(element.count)
                            .appendTo(link);
        $("<img />").addClass("topic_img")
                    .attr("src", "static/images/"+element._id+".png")
                    .appendTo(link);
//        src="{{ url('static', filename='images/meat.png') }}"
    let animation_span = $("<div class='line__wrap'><span></span><span></span><span></span><span></span></div>");
        $("<div />").addClass("topic")
                    .addClass(element._id)
                    .attr("data-id", element._id)
                    .append([link, animation_span]). appendTo("#topic_wrapper");
//                                        $("."+element._id).children(':first')
//                                                          .text(element.count);
                                         })
    })
    .fail( () => {
        console.log("error, countTopic")
    })
}


function postsByTopic(url){
//event.preventDefault();
//    console.log("clicked");
//    let target, topic_name, url;
//       target = event.target.closest('A');
//       console.log("clicked target", target);
//    if (target){
//        topic_name = target.getAttribute('href');
//        console.log("still target", topic_name, typeof(topic_name));
//    };
//    url = "/api" + topic_name;
//    console.log("still work");
//console.log(url);
    $.ajax({
        type: "GET",
        url: "/api" + url,
        dataType: "json"
    })
    .done(posts_by_topic => {
        posts_by_topic.forEach(post => renderPost(post))
//        topics.forEach(function(element) {
    }).fail( () => {
        console.log("error, Topic filtered")
    })
}

function postById(url){
    $.ajax({
        type: "GET",
        url: "/api" + url,
        dataType: "json"
    })
    .done(post_by_id => {
//    console.log(post_by_id)
        renderPostDetails(post_by_id)
    }).fail( () => {
        console.log("error, Topic filtered")
    })
}






