import os
import sys

from aiohttp import web
import pathlib
from second_demo.routes import setup_routes
import aiohttp_jinja2
import jinja2
import logging

from second_demo.utils import (get_config, init_mongo)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
config_path = "{}/config/config.yaml".format(BASE_DIR)
# static_path = "{}/static".format(BASE_DIR)


# async def init():
#     conf = get_config(BASE_DIR / 'config' / 'config.yaml')
#     return conf


# async def setup_mongo(app, conf):
#     mongo = await init_mongo(conf['mongo'])
#
#     async def close_mongo(app):
#         mongo.client.close()
#
#     app.on_cleanup.append(close_mongo)
#     return mongo

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def main():
    log = logging.getLogger()

    log.info("Launching application..")
    app = web.Application()
    # подключаюсь к клиенту
    app['db'] = init_mongo(get_config(config_path))
    setup_routes(app, BASE_DIR)
    aiohttp_jinja2.setup(app,
                         loader=jinja2.FileSystemLoader(
                             "{}/second_demo/templates".format(BASE_DIR)))
    web.run_app(app)


if __name__ == '__main__':
    main()
