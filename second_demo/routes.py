from second_demo import views
from second_demo import analyticsViews


def setup_routes(app, base_dir):
    app.router.add_get("/", views.index, name="index"),
    app.router.add_get("/api/show_posts", views.get_show_posts_json, name="show_posts"),
    app.router.add_get("/api/count_topic", views.aggregate_topic),
    app.router.add_get("/posts", views.posts, name="posts"),
    app.router.add_post("/api/add_post", views.add_post, name="add_post"),
    app.router.add_post("/api/add_comment", views.add_comment, name="add_comment"),
    app.router.add_get("/topic/{topic}", views.get_topic_page_html, name="topic"),
    app.router.add_get("/api/topic/{topic}", views.get_posts_by_topic_json),
    app.router.add_get("/recipe/{id}", views.get_post_detail_by_id_html, name="post_by_id"),
    app.router.add_get("/api/recipe/{id}", views.get_post_detail_by_id_json),
    app.router.add_post("/api/visited_post", analyticsViews.add_visited_post_analytics),
    app.router.add_get(
        "/api/clicksvscategory", analyticsViews.get_clicks_depending_frontend_request
    ),
    app.router.add_static("/static/", path=str("/{}/static".format(base_dir)), name="static"),
