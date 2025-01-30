from http.client import responses
from logging import exception

from app.layers.open_json import get_models_structure, get_id, edit_models_structure
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

async def post_brands_id_models(_id: str, body):
    data = list(get_models_structure())
    logger.info(data)
    if _id not in data:
        f"ERROR: the brand {_id} does not exist!"

    average_price = body.average_price if body.average_price else 0

    try:
        name = body.name
        average_price = average_price
        new_id= get_id(data)+ 1
        logger.info(new_id)
        new_data = {
            "id": new_id ,
            "brand_name": _id,
            "average_price": average_price,
            "name": name
        }
        data.append(new_data)
        edit_models_structure(data)

    except exception as e:
        return "ERROR was occurred!"

    return f"Modal was added, the id is {new_id}"