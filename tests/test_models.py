import unittest
from second_demo.models import Posts
from tests.test_base_test import BaseTest, _async_run




class ModelsUnitTests(BaseTest):
    @_async_run
    async def setUp(self):
        super().setUp()
        db = await self.get_database()
        # await self.get_collection_posts(db)
        await self.delete_collection_posts(db)
    #     print("setUp:  Expected result - 0 documents")

    @_async_run
    async def tearDown(self):
        db = await self.get_database()
        await self.delete_collection_posts(db)

    @_async_run
    async def test_add_post_return_dict(self):
        db = await self.get_database()
        data = await self.load_test_data("test_models.json")
        data = data['addPost'][0]
        result = await Posts.add_post(db, data["title"], data["text"], data["img"], data["topic"])
        expected = isinstance(result, dict)
        print("Method 1: test_add_post_return_dict. Expected result is dict-", result)
        self.assertTrue(expected)

    @_async_run
    async def test_add_post_empty_input_data(self):
        with self.assertRaises(ValueError):
            db = await self.get_database()
            data = await self.load_test_data("test_models.json")
            data = data['addPost'][1]
            await Posts.add_post(db, data["title"], data["text"], data["img"], data["topic"])

    @_async_run
    async def test_add_post_not_string(self):
        with self.assertRaises(TypeError):
            db = await self.get_database()
            data = await self.load_test_data("test_models.json")
            data = data['addPost'][2]
            await Posts.add_post(db, data["title"], data["text"], data["img"], data["topic"])

    @_async_run
    async def test_add_comment_will_update_document(self):
        db = await self.get_database()
        data = await self.load_test_data("test_models.json")
        document = data['testDocument'][0]
        # insert test document
        await self.insert_document_into_posts(db, document)
        # await coll.insert_one(document)
        comment = data["commentWillAdd"][0]
        # update test document
        await Posts.add_comment(db, comment["name"], comment["title"], comment["text"], comment["post_id"])
        # find updated document
        coll = db.posts
        res = await coll.find_one({"_id": "12345"})
        # check that document was updated
        print("Method 2: document was updated. Expected result - length of commentsList = 1 is", len(res["comments"]))
        self.assertEqual(len(res["comments"]), 1)

    @_async_run
    async def test_add_comment_empty_input_data(self):
        with self.assertRaises(ValueError):
            db = await self.get_database()
            data = await self.load_test_data("test_models.json")
            document = data['testDocument'][0]
            # insert test document
            await self.insert_document_into_posts(db, document)
            # try with empty data
            comment = data["commentWillAdd"][1]
            await Posts.add_comment(db, comment["name"], comment["title"], comment["text"], comment["post_id"])
        # print("Method 4: test_add_comment_empty_in_data. Expected result TypeError", the_exception)

    @_async_run
    async def test_add_comment_input_data_notString(self):
        with self.assertRaises(TypeError):
            db = await self.get_database()
            data = await self.load_test_data("test_models.json")
            document = data['testDocument'][0]
            # insert test document
            await self.insert_document_into_posts(db, document)
            # try with empty data
            comment = data["commentWillAdd"][2]
            await Posts.add_comment(db, comment["name"], comment["title"], comment["text"], comment["post_id"])

    @_async_run
    async def test_add_comment_return_dict(self):
        db = await self.get_database()
        data = await self.load_test_data("test_models.json")
        comment = data["commentWillAdd"][0]
        result = await Posts.add_comment(db, comment["name"], comment["title"], comment["text"], comment["post_id"])
        expected = isinstance(result, dict)
        print("Method 3: test_add_comment_return_dict. Expected result is dict-", result)
        self.assertTrue(expected)

    @_async_run
    async def test_get_post_by_id(self):
        db = await self.get_database()
        data = await self.load_test_data("test_models.json")
        # insert 2 documents
        await self.insert_document_into_posts(db, data['testDocument'][0])
        await self.insert_document_into_posts(db, data['testDocument'][1])
        test_id = "5678"
        result = await Posts.get_post_by_id(db, test_id)
        print("Method 4: test_get_post_by_id. Expected result dict with _id=", result["_id"])
        self.assertEqual(result["_id"], test_id)

    @_async_run
    async def test_get_post_by_not_exist_id(self):
        db = await self.get_database()
        data = await self.load_test_data("test_models.json")
        # insert test document
        await self.insert_document_into_posts(db, data['testDocument'][0])
        result = await Posts.get_post_by_id(db, "5555")
        print("Method 5: test_get_post_by_not_exist_id. Expected result None", result)
        self.assertIsNone(result)

    @_async_run
    async def test_get_post_by_exist_id_but_not_str(self):
        db = await self.get_database()
        data = await self.load_test_data("test_models.json")
        # insert test document
        await self.insert_document_into_posts(db, data['testDocument'][0])
        result = await Posts.get_post_by_id(db, 5678)
        print("Method 5: test_get_post_by_exist_id_but_not_str. Expected result None", result)
        self.assertIsNone(result)
        

    @_async_run
    async def test_get_posts_by_topic_return_list(self):
        db = await self.get_database()
        data = await self.load_test_data("test_models.json")
        # insert 3 test documents
        await self.insert_document_into_posts(db, data['testDocument'][0])
        await self.insert_document_into_posts(db, data['testDocument'][1])
        await self.insert_document_into_posts(db, data['testDocument'][2])
        result = await Posts.get_posts_by_topic(db, "topic2")
        expected = isinstance(result, list)
        print("Method 6: test_get_posts_by_topic_return_list. Expected result is list and list length = 2")
        self.assertEqual(len(result), 2)
        self.assertTrue(expected)


    @_async_run
    async def test_get_posts_by_topic_not_exist_input(self):
        db = await self.get_database()
        data = await self.load_test_data("test_models.json")
        await self.insert_document_into_posts(db, data['testDocument'][0])
        await self.insert_document_into_posts(db, data['testDocument'][1])
        await self.insert_document_into_posts(db, data['testDocument'][2])
        result = await Posts.get_posts_by_topic(db, "notExistTopic")
        print("Method 7: test_get_posts_by_topic_not_exist_input. Expected result list length = 0")
        self.assertEqual(len(result), 0)


    @_async_run
    async def test_aggregate_topics_return_list(self):
        db = await self.get_database()
        data = await self.load_test_data("test_models.json")
        await self.insert_document_into_posts(db, data['testDocument'][0])
        await self.insert_document_into_posts(db, data['testDocument'][1])
        await self.insert_document_into_posts(db, data['testDocument'][2])
        result = await Posts.aggregate_topics(db)
        expected = isinstance(result, list)
        print("Method 8: test_aggregate_topics_list. Expected result list length = 2", result[0]["_id"])
        self.assertTrue(expected)
        self.assertEqual(result[0]["_id"], "topic")
        self.assertEqual(result[1]["_id"], "topic2")

    @_async_run
    async def test_aggregate_topics_not_exist_input(self):
        with self.assertRaises(AttributeError):
            await Posts.aggregate_topics("db")


    @_async_run
    async def test_aggregate_topics_empty_db(self):
        db = await self.get_empty_database()
        result = await Posts.aggregate_topics(db)
        print("Method 9: test_aggregate_topics_empty_db. Expected result list length = 0")
        self.assertEqual(len(result), 0)


    @_async_run
    async def test_show_all_posts_return_list(self):
        db = await self.get_database()
        data = await self.load_test_data("test_models.json")
        await self.insert_document_into_posts(db, data['testDocument'][0])
        await self.insert_document_into_posts(db, data['testDocument'][1])
        await self.insert_document_into_posts(db, data['testDocument'][2])
        print("Method 10: test_show_all_posts_return_list. Expected result list length = 3")
        result = await Posts.show_all_posts(db)
        self.assertEqual(len(result), 3)

    @_async_run
    async def test_show_all_posts_not_exist_input(self):
        with self.assertRaises(AttributeError):
            await Posts.show_all_posts("db")


    @_async_run
    async def test_show_all_posts_empty_database(self):
        with self.assertRaises(AttributeError):
            db = self.get_empty_database()
            await Posts.show_all_posts(db)


if __name__ == "__main__":
    unittest.main()
