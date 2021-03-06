from aiohttp import web
from .analyticsModel import Analytics
from datetime import datetime


async def add_visited_post_analytics(request: web.Request):
    client_data = await request.json()
    try:
        await Analytics.add_new_visit_to_db(
            db=request.app["db"],
            post_id=client_data["post_id"],
            post_title=client_data["post_title"],
            post_category=client_data["post_category"],
            posts_comments_qty=client_data["posts_comments_qty"],
        )

    except Exception as e:
        print("Exception", e)
    return web.Response()


async def get_clicks_depending_frontend_request(request: web.Request):
    filter = request.match_info["filter"]
    if filter == "noFilters":
        analytics_chart = await Analytics.query_agreggate_for_chart_full(db=request.app["db"])
        if analytics_chart:
            return web.json_response(analytics_chart)
    elif filter == "period":
        # Filter period of date
        period = request.match_info["filterData"].split("E")
        analytics_chart = await Analytics.query_agreggate_for_chart_period(db=request.app["db"],
                                                                           start=period[0], end=period[1])
        if analytics_chart:
            return web.json_response(analytics_chart)
    elif filter == "month":
        month = request.match_info["filterData"].split("E")
        analytics_chart = await Analytics.query_agreggate_for_chart_month(db=request.app["db"],
                                                                          firstDay=month[0],
                                                                          lastDay=month[1])
        if analytics_chart:
            return web.json_response(analytics_chart)


