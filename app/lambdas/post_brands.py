from app.layers.open_json import get_models_structure, edit_brands_structure, get_brands_structure


async def post_brands(_id: str):
    data = get_brands_structure()
    if _id in data:
        return "ERROR: Brand name is already exist!"
    data = data.append(_id)
    edit_brands_structure(data)
    return "Brand ID was correctly added"