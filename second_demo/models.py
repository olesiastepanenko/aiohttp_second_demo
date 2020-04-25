from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime
from bson import ObjectId
import pymongo
from operator import itemgetter


class Posts:

    @staticmethod
    async def count_posts(db: AsyncIOMotorDatabase, filter):
        try:
            if filter == "posts":
                collection_length = await db.posts.count_documents({})
                return collection_length
            else:
                collection_length = await db.posts.count_documents({"topic": filter})
                return collection_length
        except ValueError:
            print("ERROR", filter)



    @staticmethod
    async def show_all_posts(db: AsyncIOMotorDatabase, pageNum, pageSize):
        try:
            all_posts = await db.posts.find(
                    {}, {"_id": 1, "topic": 1, "title": 1, "image": 1},
                    sort=[("_id", pymongo.DESCENDING)]
                        ).skip(int(pageSize)*int(pageNum)).to_list(int(pageSize))
            return all_posts
        except ValueError:
            print("Input data are not number")


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
    async def get_posts_by_topic(db: AsyncIOMotorDatabase, filter, pageNum, pageSize):
        try:
            filtered_posts_by_topic = await db.posts.find(
                {"topic": filter},
                {"_id": 1, "topic": 1, "title": 1, "image": 1},
                sort=[("_id", pymongo.DESCENDING)],
            ).skip(int(pageSize)*int(pageNum)).to_list(int(pageSize))
            return filtered_posts_by_topic
        except ValueError:
            print("Input data are not number")

    @staticmethod
    async def get_post_by_id(db: AsyncIOMotorDatabase, post_id):
        post_by_id = await db.posts.find_one(
            {"_id": post_id},
            {"_id": 1, "title": 1, "image": 1, "post_text": 1, "topic": 1, "comments": 1}
        )
        # print(post_by_id)
        return post_by_id

    @staticmethod
    async def add_post(
        db: AsyncIOMotorDatabase, title: str, ingredients:str, post_text: str, image: str, topic: str,
    ):
        data_dict = {
            "_id": str(ObjectId()),
            "topic": topic,
            "title": title,
            "ingredients": ingredients,
            "post_text": post_text,
            "date_created": datetime.utcnow().replace(microsecond=0),
            "image": image,
            "comments": [],
        }
        new_post = await db.posts.insert_one(data_dict)
        if new_post.acknowledged:
            return data_dict

    @staticmethod
    async def add_comment(db: AsyncIOMotorDatabase, name: str, title: str, text: str, post_id: str):
        data_dict = {
            "_id": str(ObjectId()),
            "name": name,
            "title": title,
            "text": text,
            "date_created": str(datetime.utcnow().replace(microsecond=0)),
        }
        # push comment to post document
        inserted_comment = await db.posts.update_one(
            # {"_id": post_id}, {"$push": {"comments": data_dict}}
        {"_id": post_id}, {"$push": {"comments": {"$each":[data_dict], "$sort": {"_id":-1}}}}
        )
        if inserted_comment.acknowledged:
            # print(inserted_comment)
            return data_dict


# db.members.update({_id:1}, {$push:{comments: {name: "Lucy", "title":"Hello world 2"}}})
