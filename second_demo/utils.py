import logging

from motor.motor_asyncio import AsyncIOMotorClient
import pathlib
import yaml

# BASE_DIR = pathlib.Path(__file__).parent.parent


def get_config(path):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
        return config


# config = get_config(config_path)

# создаем клиента дб
def init_mongo(conf):
    log = logging.getLogger(__name__)

    log.info("Initializing MongoDB %s:%s", conf["mongo"]["host"], conf["mongo"]["port"])
    client: AsyncIOMotorClient = AsyncIOMotorClient(conf["mongo"]["host"], conf["mongo"]["port"])

    log.info("Connecting to DB %s", conf["mongo"]["database"])
    db = client.get_database(conf["mongo"]["database"])

    log.info("Connected to %s:%s", conf["mongo"]["host"], conf["mongo"]["port"])
    return db
