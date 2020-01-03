class CreatePost extends HTMLElement {
    render() {
        let form = document.createElement('FORM');
        $(form).addClass("add_new_post")
            .attr("enctype", "multipart/form-data")
            .attr("method", "POST");

        let topic = document.createElement('SELECT');
        $(topic).addClass("post_form")
            .addClass("empty_field")
            .attr("name", "topic")
            .attr("id", "post_topic");
        topic.insertAdjacentHTML('afterbegin', ' <select name="dishes"> <option value="meat">Meat dishes</option> <option value="fish">Fish dishes</option> <option value="vegetarian">Vegetarian dishes</option> <option value="dessert">Dessert</option> </select> ');
        form.append(topic);
        topic.insertAdjacentHTML('beforebegin', '<label for="topic">Choose chapter</label>');

        let title = document.createElement('INPUT');
//        let title = $(":input");
        $(title).attr("id", "title")
            .addClass("post_form")
            .addClass("empty_field")
            .attr("name", "title")
            .attr("type", "text")
            .attr("value", "");
        form.append(title);
        title.insertAdjacentHTML('beforebegin', '<label for="title">Post title</label>');

        let img_field = document.createElement("INPUT");
        $(img_field).attr("id", "post_img")
            .addClass("post_form")
            .addClass("empty_field")
            .attr("name", "image")
            .attr("type", "file")
            .attr("onchange", "encodeImageFileAsURL(this)");
        form.append(img_field);

        let text = document.createElement('TEXTAREA');
        $(text).attr("id", "post_text")
            .addClass("post_form")
            .addClass("empty_field")
            .attr("name", "post_text")
            .attr("value", "");
        form.append(text);
        text.insertAdjacentHTML('beforebegin', '<label for="post_text">Post message</label>');

        this.append(form);
        let button = document.createElement("div");
        button.id = "create_post";
        button.innerHTML = "CREATE";
        button.className = "still_but";
        this.append(button)
    }

    connectedCallback() {
        if (!this.rendered) {
            this.render();
            this.rendered = true;
        }
        let form = $(".add_new_post");
        form.find(".post_form").each(function () {
        // check that felds are not empty
            $(this).change(function () {
                if ($(this).val().length == 0) {
                    $(this).addClass("empty_field");
                    $(this).removeClass(".empty_field_syles")
                } else {
//                    console.log($(this).val().length)
                    $(this).removeClass("empty_field");
                    $(this).removeClass("empty_field_syles")
                }
            })
        });
        $("#create_post").on("click", function () {
            var title, topic, text, data;
            if (form.find(".empty_field").length > 0) {
                form.find(".empty_field").each(function () {
                    $(this).addClass("empty_field_syles")
                })
            } else {
                console.log("All fields are not empty, ready for Ajax");
                topic = $("#post_topic").val();
                title = $("#title").val();
                text = $("#post_text").val();
                data = {
                    topic: topic,
                    title: title,
                    text: text,
                    img: temp,
                };
                $.ajax({
                    type: "POST",
                    url: "/api/add_post",
                    data: data,
                    success: function (data) {
                        closeModalCreatePost();
//                        postById("/recipe/" + data._id)
                        console.log("data", data, typeof(data))
//                        renderPost(data);
                    }
                })
            }
        })
    };


    static get observedAttributes() {
        return ['title'];
    }

    attributeChangedCallback(name, oldValue, newValue) {
//    здесь сделаю отслеживание что формы заполнены
        this.render();
    }
}

customElements.define("create-post", CreatePost);

var temp; //что с этим делать куда блин сохранять ????
// image to base64
function encodeImageFileAsURL(element) {
    var file = element.files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        temp = reader.result;
        return temp
    }
    reader.readAsDataURL(file);
}

function closeModalCreatePost(){
    $("#modal_fixed_overlay_add_post").css("display", "none");
}