from second_demo.analyticsModel import Analytics
from tests.test_base_test import BaseTest, _async_run
from datetime import datetime



class AnalyticsModelUnittest(BaseTest):
    @_async_run
    async def setUp(self):
        super().setUp()
        db = await self.get_database()
        # await self.get_collection_posts(db)
        await self.delete_collection_postsVisits(db)
    #     print("setUp:  Expected result - 0 documents")

    @_async_run
    async def tearDown(self):
        db = await self.get_database()
        await self.delete_collection_postsVisits(db)


    @_async_run
    async def test_add_new_visit_to_db_return_true(self):
        db = await self.get_database()
        data = await self.load_test_data("test_postVisits.json")
        result = await Analytics.add_new_visit_to_db(db, data[0]["post_id"],
                                                     data[0]["post_title"],
                                                     data[0]["post_category"],
                                                     data[0]["posts_comments_qty"])
        self.assertTrue(result)


    @_async_run
    async def test_query_agreggate_for_chart_return_list(self):
        db = await self.get_database()
        data = await self.load_test_data("test_postVisits.json")
        data[0]["date_visited"]= datetime.utcnow().replace(microsecond=0)
        data[1]["date_visited"]= datetime.utcnow().replace(microsecond=0)
        await self.insert_document_into_postsVisits(db, data[0])
        await self.insert_document_into_postsVisits(db, data[1])
        result = await Analytics.query_agreggate_for_chart(db)
        print(result, type(result), len(result))
        expected = isinstance(result, list)
        self.assertTrue(expected)









