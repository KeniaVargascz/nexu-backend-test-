import json
import os
import logging
__all__ = [
    "get_models_structure",
    "edit_brands_structure",
    "edit_models_structure",
    "get_brands_structure",
    "get_id"
]
base_path = os.path.dirname(os.path.abspath(__file__))
file_path_brands = os.path.join(base_path, 'brands.json')
file_path_models = os.path.join(base_path, 'models.json')


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_models_structure():
    with open(file_path_models, 'r') as file:
        data = json.load(file)
    return data

def get_brands_structure():
    with open(file_path_brands, 'r') as file:
        data = json.load(file)
    return data

def edit_brands_structure(new_data):
    logger.info(new_data)
    with open(file_path_brands, "w") as file:
        json.dump(new_data, file, indent=4)
    return new_data

def edit_models_structure(new_data):
    with open(file_path_models, "w") as file:
        json.dump(new_data, file, indent=4)
    return new_data

def get_id(data):
    return max(data, key=lambda x: x['id'])['id']