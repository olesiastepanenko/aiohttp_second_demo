from second_demo import views


def setup_routes(app, base_dir):
    app.router.add_get("/", views.index, name="index"),
    app.router.add_get("/show_posts", views.show_posts, name="show_posts"),
    app.router.add_get("/posts", views.posts, name="posts"),
    app.router.add_post("/add_post", views.add_post, name="add_post")

    app.router.add_static("/static/", path=str("/{}/static".format(base_dir)), name="static")