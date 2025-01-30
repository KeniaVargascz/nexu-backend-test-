from app.layers.open_json import get_models_structure, edit_models_structure
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

async def put_model_by_id(_id: int, body):
    data = get_models_structure()
    average_price = body.average_price if body.average_price else 0
    logger.info(average_price)
    logger.info(_id)
    for element in data:
        logger.info(element)
        if int(element["id"]) == int(_id):
            logger.info(element["id"])
            element["average_price"] = average_price
            break
    edit_models_structure(data)
    return "Changes was updated correctly!"