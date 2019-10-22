from aiohttp import web
import aiohttp_jinja2
from datetime import datetime
import json
import bson
from bson import ObjectId
import sys


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
        "topic": in_data["topic"],
        "title": in_data["title"],
        "post_text": in_data["text"],
        "date_created": str(datetime.utcnow().replace(microsecond=0)),
        "image": in_data["image"]
    }
    print("new post added", data_dict)
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
    db = request.app["db"]
    print("db", db)
    collection = db["posts"]
    # cursor = collection.find({}, {"_id": 0, "title": 1, "date_created": 1})
    posts = await collection.find({}, {"_id": 0, "topic": 1, "title": 1, "image": 1}).to_list(length=100)
    if posts:
        return web.json_response(posts)
    else:
        return web.Response(text="The are no posts")


async def count_topic(request: web.Request):
    db = request.app["db"]
    collection = db["posts"]
    pipeline = [{"$group": {"_id": "$topic", "count": {"$sum": 1}}}]
    topics = []
    async for doc in collection.aggregate(pipeline):
        topics.append(doc)
    if topics:
        return web.json_response(topics)
    else:
        return web.Response(text="The are no posts")


@aiohttp_jinja2.template("topic.html")
async def topic(request: web.Request):
    pass
