from app.layers.open_json import get_models_structure


async def get_list_all_models(_id: str):
    data = get_models_structure()
    by_brand_id = [element for element in data if element["brand_name"] == str(_id)]
    return by_brand_id