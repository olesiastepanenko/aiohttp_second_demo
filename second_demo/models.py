from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime
from bson import ObjectId
import pymongo
from operator import itemgetter


class Posts:
    # all posts are sorts DESC
    @staticmethod
    async def show_all_posts(db: AsyncIOMotorDatabase, limit=100):
        all_posts = await db.posts.find({},
                                        {"_id": 1, "topic": 1, "title": 1, "image": 1}, sort=[('_id', pymongo.DESCENDING)]).to_list(limit)
        return all_posts

    @staticmethod
    async def aggregate_topics(db: AsyncIOMotorDatabase):
        pipeline = [{"$group": {"_id": "$topic"}}]
        topics = []
        async for doc in db.posts.aggregate(pipeline):
            topics.append(doc)
        # сотрировка списка топиков
        topics.sort(key=itemgetter('_id'))
        return topics

    @staticmethod
    async def get_posts_by_topic(db: AsyncIOMotorDatabase, filter):
        filtered_posts_by_topic = await db.posts.find({'topic': filter},
                                                      {"_id": 1, "topic": 1, "title": 1,
                                                       "image": 1}, sort=[('_id', pymongo.DESCENDING)])\
                                                        .to_list(length=100)
        return filtered_posts_by_topic

    @staticmethod
    async def get_post_by_id(db: AsyncIOMotorDatabase, post_id):
        post_by_id = await db.posts.find_one({"_id": post_id},
                                             {"_id": 1, "title": 1, "image": 1, "post_text": 1})
        return post_by_id

    @staticmethod
    async def add_post(db: AsyncIOMotorDatabase, title: str, post_text: str, image: str, topic: str,):
        data_dict = {
            "_id": str(ObjectId()),
            "topic": topic,
            "title": title,
            "post_text": post_text,
            "date_created": str(datetime.utcnow().replace(microsecond=0)),
            "image": image
        }
        await db.posts.insert_one(data_dict)
        return data_dict
