from aiohttp import web
import aiohttp_jinja2
from .models import Posts


@aiohttp_jinja2.template("index.html")
async def index(request: web.Request):
    pass


async def add_post(request: web.Request):
    in_data = await request.json()
    created_post = await Posts.add_post(
        db=request.app["db"],
        title=in_data["title"],
        post_text=in_data["text"],
        topic=in_data["topic"],
        image=in_data["img"],
    )
    if created_post:
        return web.json_response(created_post["_id"])
    else:
        raise web.HTTPInternalServerError


async def add_comment(request: web.Request):
    in_data = await request.json()
    created_comment = await Posts.add_comment(
        db=request.app["db"],
        name=in_data["name"],
        title=in_data["title"],
        text=in_data["text"],
        post_id=in_data["post_id"],
    )
    return web.json_response(created_comment)


@aiohttp_jinja2.template("posts.html")
async def posts(request: web.Request):
    pass

async def get_count_posts_in_db(self):
    count_post = await Posts.count_posts(db=self.app["db"],
                                         filter=self.match_info["filter"])
    if count_post:
        return web.json_response(count_post)


async def get_show_posts_json(request: web.Request):
    all_posts = await Posts.show_all_posts(db=request.app["db"],
                                           pageNum=request.match_info["id"],
                                           pageSize=request.match_info["volume"])
    if all_posts:
        return web.json_response(all_posts)
    else:
        return web.Response(text="The are no posts")


async def aggregate_topic(request: web.Request):
    aggregated_by_topic = await Posts.aggregate_topics(db=request.app["db"])
    if aggregated_by_topic:
        return web.json_response(aggregated_by_topic)
    else:
        return web.Response(text="The are no posts")


@aiohttp_jinja2.template("topic.html")
async def get_topic_page_html(request: web.Request):
    pass


async def get_posts_by_topic_json(self):
    filtered_posts_by_topic = await Posts.get_posts_by_topic(
                                    db=self.app["db"],
                                    filter=self.match_info["topic"],
                                    pageNum=self.match_info["id"],
                                    pageSize=self.match_info["volume"]
                                    )
    if filtered_posts_by_topic:
        return web.json_response(filtered_posts_by_topic)
    else:
        raise web.HTTPNotFound()


@aiohttp_jinja2.template("recipe.html")
async def get_post_detail_by_id_html(self):
    pass


async def get_post_detail_by_id_json(self):
    # print("get_post_detail_by_id_json was called")
    post_by_id = await Posts.get_post_by_id(db=self.app["db"], post_id=self.match_info["id"])
    # print(post_by_id)
    if post_by_id:
        return web.json_response(post_by_id)
    else:
        raise web.HTTPNotFound()
