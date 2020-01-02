from aiohttp import web
from .analyticsModel import Analytics


async def add_visited_post_analytics(request: web.Request):
    client_data = await request.json()
    print(request)
    is_visit_added = await Analytics.add_new_visit_to_db(
        db=request.app["db"],
        post_id=client_data["post_id"],
        post_title=client_data["post_title"],
        post_category=client_data["post_category"],
        posts_comments_qty=client_data["posts_comments_qty"],
    )
    print("is_visit_added", is_visit_added)
    if is_visit_added != True:
        return web.HTTPBadRequest

    return web.HTTPOk


async def get_clicks_depending_frontend_request(request: web.Request):
    analytics_chart = await Analytics.query_agreggate_for_chart(db=request.app["db"])

    # print("analytics_chart", analytics_chart)
    if analytics_chart:
        return web.json_response(analytics_chart)
