import os
import sys

from aiohttp import web
from second_demo.routes import setup_routes
import aiohttp_jinja2
import jinja2
import logging

from second_demo.utils import get_config, init_mongo

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
config_path = "{}/config/config.yaml".format(BASE_DIR)

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

async def init_app(config):
    app = web.Application()
    # подключаюсь к клиенту
    app["db"] = init_mongo(config, config["mongo"]["database"])
    setup_routes(app, BASE_DIR)
    aiohttp_jinja2.setup(
        app, loader=jinja2.FileSystemLoader("{}/second_demo/templates".format(BASE_DIR))
    )
    return app


def main():
    log = logging.getLogger()
    config = get_config(config_path)
    log.info("Launching application..")
    app = init_app(config)

    web.run_app(app)


if __name__ == "__main__":
    main()
