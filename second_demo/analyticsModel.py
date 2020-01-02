from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime
from bson import ObjectId

# from bson.son import SON
import pymongo
from operator import itemgetter


class Analytics:
    @staticmethod
    async def add_new_visit_to_db(
            db: AsyncIOMotorDatabase,
            post_id: str,
            post_title: str,
            post_category: str,
            posts_comments_qty: int,
    ):
        new_visit_dict = {
            "_id": str(ObjectId()),
            "post_id": post_id,
            "post_title": post_title,
            "post_category": post_category,
            "posts_comments_qty": posts_comments_qty,
            "date_visited": datetime.utcnow().replace(microsecond=0),
        }
        # print(new_visit_dict)
        add_new_visit = await db.postsVisits.insert_one(new_visit_dict)
        return add_new_visit.acknowledged

    @staticmethod
    async def query_agreggate_for_chart(db: AsyncIOMotorDatabase):
        # Category VS Visits (Date)
        # pipeline = [
        #     {"$facet": {
        #         "dates": [
        #             {"$group": {
        #                 "_id": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date_visited"}},
        #             }},
        #             {"$sort": {"_id": 1}}
        #         ],
        #         "categorys": [
        #             {
        #                 "$group": {
        #                     "_id": "$post_category"
        #                 }
        #             }],
        #         "visits": [{"$group": {
        #             "_id": {"category": "$post_category",
        #                     "date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date_visited"}}},
        #             "count": {"$sum": 1}}},
        #             {"$project": {
        #                 "_id": 0,
        #                 "label": "$_id.date",
        #                 "category": "$_id.category",
        #                 "value": "$count"}},
        #             {"$sort": {"label": 1}}
        #         ]
        #     }
        #     }
        # ]

        pipeline = [{"$facet": {
            "dates": [
                {"$group": {
                    "_id": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date_visited"}},
                }}, {"$sort": {"_id": 1}}],
            "visits": [
                {"$group": {
                    "_id": {"category": "$post_category",
                            "date": {"$dateToString": {"format": "%Y-%m-%d", "date": "$date_visited"}},
                            }, "count": {"$sum": 1}
                }
                }, {"$project": {
                    "_id": 0,
                    "date": "$_id.date",
                    "category": "$_id.category",
                    "value": "$count"
                }
                }, {"$sort": {"date": 1}
                    }, {"$group": {"_id": "$category",
                                   "data": {"$push": "$value"},
                                   "labels": {"$push": "$date"}
                                   }
                        }
            ]
        }}]
        data_for_chart = []
        async for doc in db.postsVisits.aggregate(pipeline):
            data_for_chart.append(doc)
        print(type(data_for_chart))
        return data_for_chart
