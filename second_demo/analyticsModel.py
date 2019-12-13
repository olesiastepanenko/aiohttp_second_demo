from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime
from bson import ObjectId
import pymongo
from operator import itemgetter


class Analytics:

    @staticmethod
    async def add_new_visit_to_db(db: AsyncIOMotorDatabase, post_id: str, post_title: str,
                                  post_category: str, posts_comments_qty: int):
        new_visit_dict = {
            "_id": str(ObjectId()),
            "post_id": post_id,
            "post_title": post_title,
            "post_category": post_category,
            "posts_comments_qty": posts_comments_qty,
            "date_visited": str(datetime.utcnow().replace(microsecond=0)),
        }
        add_new_visit = await db.postsVisits.insert_one(new_visit_dict)
        return add_new_visit.acknowledged
