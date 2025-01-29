from app.layers.open_json import get_models_structure


async def get_model(greater: int, lower: int):
    if not lower:
        lower = 0
    data = get_models_structure()
    response = [element for element in data if lower <= element["average_price"] <= greater]
    response_sorted = sorted(response, key=lambda x: x["average_price"], reverse=True)

    return response_sorted