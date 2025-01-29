import json
__all__ = [
    "get_models_structure",
    "edit_brands_structure",
    "edit_models_structure",
    "get_brands_structure",
    "get_id"
]

def get_models_structure():
    with open('models.json', 'r') as file:
        data = json.load(file)
    return data

def get_brands_structure():
    with open('brands.json', 'r') as file:
        data = json.load(file)
    return data

def edit_brands_structure(new_data):
    with open('brands.json', "r+") as file:
        file.seek(0)
        file.write(new_data)
    return new_data

def edit_models_structure(new_data):
    with open('brands.json', "r+") as file:
        file.seek(0)
        file.write(new_data)
    return new_data

def get_id(data):
    return max(data, key=lambda x: x['id'])['id']