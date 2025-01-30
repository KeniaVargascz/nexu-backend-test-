from app.layers.open_json import get_models_structure, edit_brands_structure, get_brands_structure
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

async def post_brands(body):
    data = get_brands_structure()
    name = body.brand_name
    if any(brand['name'] == name for brand in data):
        return "ERROR: Brand name already exists!"
    data.append({
        "name": name
    })
    edit_brands_structure(data)
    return "Brand ID was correctly added"