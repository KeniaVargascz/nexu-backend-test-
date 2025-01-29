from app.layers.open_json import get_models_structure

async def put_model_by_id(_id: str, body):
    data = get_models_structure()
    average_price = body.average_price if body.average_price else 0

    for element in data:
        if element["id"] == _id:
            element["average_price"] = average_price
            break

    return "Changes was updated correctly!"