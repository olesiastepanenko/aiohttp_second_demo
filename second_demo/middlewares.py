import aiohttp_jinja2
from aiohttp import web
from aiohttp_session import get_session


async def handle_404(request):
    aiohttp_jinja2.render_template("404.html", request, {})


async def handle_500(request):
    aiohttp_jinja2.render_template("500.html", request, {})


def create_error_middleware(overrides):
    @web.middleware
    async def error_middleware(request, handler):
        try:
            response = await handler(request)
            override = overrides.get(response.status)
            if override:
                return override(request)
            return response
        except web.HTTPException as ex:
            override = overrides.get(ex.status)
            if override:
                return await override(request)
            raise

    return error_middleware


def setup_middleware(app):
    error_middleware = create_error_middleware({404: handle_404, 500: handle_500})
    return app.middlewares.append(error_middleware)


@web.middleware
async def user_session_middleware(request, handler):
    request.session = await get_session(request)
    response = await handler(request)
    return response
