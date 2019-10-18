from aiohttp import web
import aiohttp_jinja2
from datetime import datetime
import json
from bson import ObjectId


@aiohttp_jinja2.template("index.html")
async def index(request: web.Request):
    pass
    # collection = "posts"
    # db = request.app["db"]
    # posts = await db.get_collection(collection).find().to_list(length=100)
    # if posts:
    #     return {"posts": posts}
    # else:
    #     return web.Response(text="The are no posts")


async def add_post(request: web.Request):
    in_data = await request.post()
    data_dict = {
        "title": in_data["title"],
        "post_text": in_data["text"],
        "date_created": str(datetime.utcnow().replace(microsecond=0)),
        "image": in_data["image"]
    }
    print(data_dict)
    await request.app["db"].posts.insert_one(data_dict)
    # return web.HTTPFound(location=request.app.router['index'].url_for())
    return web.json_response({"title": data_dict["title"],
                              "post_text": data_dict["post_text"],
                              "date_created": data_dict["date_created"],
                              "image": data_dict["image"]})


@aiohttp_jinja2.template("posts.html")
async def posts(request: web.Request):
    pass


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


async def show_posts(request: web.Request):
    collection = "posts"
    db = request.app["db"]
    data = []
    async for col in db.get_collection(collection).find():
        col.pop('_id')
        col.update({'date_created': str(col.get('date_created'))})
        # encoded = JSONEncoder().encode(col)
        # print(encoded)
        data.append(col)
    if data:
        return web.json_response(data)
    else:
        return web.Response(text="The are no posts")
