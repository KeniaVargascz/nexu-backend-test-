from app.layers.open_json import get_models_structure


async def get_list_all_brands():
    data = get_models_structure()
    return data