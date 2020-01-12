from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime
from bson import ObjectId
import pymongo
from operator import itemgetter


class Posts:
    # all posts are sorts DESC
    @staticmethod
    async def show_all_posts(db: AsyncIOMotorDatabase, limit=100):
        all_posts = await db.posts.find(
            {}, {"_id": 1, "topic": 1, "title": 1, "image": 1}, sort=[("_id", pymongo.DESCENDING)]
        ).to_list(limit)
        return all_posts

    @staticmethod
    async def aggregate_topics(db: AsyncIOMotorDatabase):
        pipeline = [{"$group": {"_id": "$topic"}}]
        topics = []
        async for doc in db.posts.aggregate(pipeline):
            topics.append(doc)
        # сотрировка списка топиков
        topics.sort(key=itemgetter("_id"))
        # print(topics)
        return topics

    @staticmethod
    async def get_posts_by_topic(db: AsyncIOMotorDatabase, filter):
        filtered_posts_by_topic = await db.posts.find(
            {"topic": filter},
            {"_id": 1, "topic": 1, "title": 1, "image": 1},
            sort=[("_id", pymongo.DESCENDING)],
        ).to_list(length=100)
        return filtered_posts_by_topic

    @staticmethod
    async def get_post_by_id(db: AsyncIOMotorDatabase, post_id):
        post_by_id = await db.posts.find_one(
            {"_id": post_id},
            {"_id": 1, "title": 1, "image": 1, "post_text": 1, "topic": 1, "comments": 1},
            sort=[("comments", pymongo.DESCENDING)],
        )

        return post_by_id


    @staticmethod
    async def add_post(
            db: AsyncIOMotorDatabase, title: str, post_text: str, image: str, topic: str,
    ):
        if len(title) and len(post_text) and len(image) and len(topic) > 0:
            data_dict = {
                "_id": str(ObjectId()),
                "topic": topic,
                "title": title,
                "post_text": post_text,
                "date_created": str(datetime.utcnow().replace(microsecond=0)),
                "image": image,
                "comments": [],
            }
            # class 'pymongo.results.InsertOneResult'
            new_post = await db.posts.insert_one(data_dict)
            # print("data_dict from models", new_post)
            if new_post.acknowledged:
                return data_dict
        raise ValueError

    @staticmethod
    async def add_comment(db: AsyncIOMotorDatabase, name: str, title: str, text: str, post_id: str):
        if len(name) and len(title) and len(text) and len(post_id) > 0:
            data_dict = {
                "_id": str(ObjectId()),
                "name": name,
                "title": title,
                "text": text,
                "date_created": str(datetime.utcnow().replace(microsecond=0)),
            }
            # push comment to post document
            inserted_comment = await db.posts.update_one(
                {"_id": post_id}, {"$push": {"comments": data_dict}}
            )
            if inserted_comment.acknowledged:
                # print(inserted_comment)
                return data_dict
        raise ValueError
