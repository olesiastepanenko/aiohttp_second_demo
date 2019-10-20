$(document).ready(function () {
    console.log('Document is ready');
    // lissener for modal ADD post
    $(".new_post_button").on("click", function () { $("#modal_fixed_overlay_add_post").css("display", "block")})
    getPosts();

});

function getPosts(){
       $.ajax({
        type: "GET",
        url: "/show_posts",
        dataType: "json"
    })
    .done(posts => {
        console.log(posts)
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


//function addNewPostHandler(){
//        let form = $(".add_new_post")
//        form.find("input").each(function(){
//            $(this).change(function(){
//                console.log($(this))
//                if ($(this).val().length==0){
//                    $(this).addClass("empty_field")
//                    $(this).removeClass(".empty_field_syles")
//                } else {
//                    console.log($(this).val().length)
//                    $(this).removeClass("empty_field")
//                    $(this).removeClass("empty_field_syles")
//                }
//            })
//        })
//    $("#create_post").on("click", function(){
//            var title, text;
//            if(form.find(".empty_field").length>0){
//                form.find(".empty_field").each(function(){
//                    $(this).addClass("empty_field_syles")
//                })
//            } else{
//                console.log("All fields are not empty, ready for Ajax");
//                title = $("#title").val();
//                text = $("#post_text").val();
//                data = {
//                    title: title,
//                    text: text
//                };
//                $.ajax({
//                    type: "POST",
//                    url: "/add_post",
//                    data: data,
//                success: function (data) {
//                    console.log("Ajax successed", data)
//                }
//                })
//            }
//        })
//
//}


//class AllPosts extends HTMLElement {
//        static get observedAttributes() {
//            console.log("observed")
//            return ['title', 'text'];
//        }
////        constructor() {
////        super();
////        const shadow = this.attachShadow({mode: 'open'});
////        const title = document.createElement('div');
////        const text = document.createElement('div');
////        const style = document.createElement('style');
////        shadow.appendChild(style);
////        shadow.appendChild(title);
////        shadow.appendChild(text);
////        const title = document.createElement('div');
////        const text = document.createElement('div');
////        title.className = "post_title";
////        text.className = "post_text";
////        title.innerHTML = this.dataset.title;
////        console.log(this.dataset.title, 'render');
////        text.innerHTML = this.dataset.text;
//
//
////        $(this).append(title);
////        $(this).append(text)
////        console.log(this.dataset.title)
////        }
//    render() {
//    console.log("render")
//        let title = document.createElement('div');
//        let text = document.createElement('div');
//        title.className = "post_title";
//        text.className = "post_text";
////        title.innerHTML = this.data.title;
////        console.log(this.dataset.title, 'render');
////        text.innerHTML = this.data.text;
//        this.append(title);
//        this.append(text)
//
//    }
//
//    connectedCallback() {
//        $.ajax({
//            type: "GET",
//            url: "/posts"}).done(function(data){
//                data.forEach(function(value){
//                    renderPost(value);
//                }
//                )
//            }).fail(function(){
//            console.log("error")})
//}
//    static get observedAttributes() {
//        return ['title', 'text'];
//    }
//
//    attributeChangedCallback(name, oldValue, newValue) {
////        this.render();
//    }
//}
//
//customElements.define("posts-page", AllPosts);




