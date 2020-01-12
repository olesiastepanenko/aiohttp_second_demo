import unittest
import asyncio
import os
import jsonplus
from main import init_mongo, config_path
from second_demo.utils import get_config
from motor.motor_asyncio import AsyncIOMotorDatabase


def _async_run(func):
    # """Async runner decorator"""
    def wrapper(*args, **kwargs):
        # structlog.get_logger("test_models").debug("Executing test: %s", args)
        return asyncio.get_event_loop().run_until_complete(func(*args, **kwargs))

    return wrapper


class BaseTest(unittest.TestCase):
    def __init__(self, method_name="runTest"):
        super().__init__(method_name)
        self._loop = asyncio.get_event_loop()

    @staticmethod
    async def get_database():
        config = get_config(config_path)
        db = init_mongo(config, config["mongoTest"]["database"])
        print("Current Database", db)
        return db

    @staticmethod
    async def get_empty_database():
        config = get_config(config_path)
        db = init_mongo(config, config["mongoTestEmpty"]["database"])
        print("Current Database", db)
        return db

    @staticmethod
    async def get_collection_posts(db: AsyncIOMotorDatabase):
        cursor = db.posts.find()
        for document in await cursor.to_list(length=100):
            print("!!!!!! all_posts !!!!!!!", document)

    @staticmethod
    async def get_collection_postsVisits(db: AsyncIOMotorDatabase):
        cursor = db.postsVisits.find()
        for document in await cursor.to_list(length=100):
            print("!!!!!! all_postsVisits !!!!!!!", document)


    @staticmethod
    async def delete_collection_posts(db: AsyncIOMotorDatabase):
        coll = db.posts
        # n = await coll.count_documents({})
        # print('%s documents before calling drop()' % n)
        await coll.drop()
        # print('%s documents after' % (await coll.count_documents({})), "result", result)


    @staticmethod
    async def delete_collection_postsVisits(db: AsyncIOMotorDatabase):
        coll = db.postsVisits
        await coll.drop()


    @staticmethod
    async def insert_document_into_posts(db: AsyncIOMotorDatabase, document):
        coll = db.posts
        result = await coll.insert_one(document)
        # print('%s documents after insert' % (await coll.count_documents({})), 'result %s' % repr(result.inserted_id))
        return result


    @staticmethod
    async def insert_document_into_postsVisits(db: AsyncIOMotorDatabase, document):
        coll = db.postsVisits
        result = await coll.insert_one(document)
        return result


    @staticmethod
    async def load_test_data(data_file):
        working_dir = os.path.dirname(os.path.realpath(data_file))
        jsonplus.prefer_compat()
        with open(f"{working_dir}/data/{data_file}") as file:
            data = jsonplus.loads(file.read())
            file.close()
        return data
