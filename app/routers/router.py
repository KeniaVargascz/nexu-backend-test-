from fastapi import APIRouter
from app.lambdas.lambdas import (
    get_list_all_brands,
    get_list_all_models,
    post_brands_id_models,
    post_brands,
    put_model_by_id,
    get_model
)
from app.models.ObjModel import ModelRequest

router = APIRouter()

@router.get("/")
async def get_something():
    return  "Here are nothing!!"

@router.get("/brands")
async def get_brands():
    return await get_list_all_brands()

@router.get("/brands/{_id}/models")
async def get_brands_id_models(_id: str):
    return await get_list_all_models(_id)

@router.post("/brands")
async def post_brands_(_id: str):
    return await post_brands(_id)

@router.post("/brands/{_id}/models")
async def post_brands_id_models_endpoint(_id: str, body: ModelRequest):
    return await post_brands_id_models(_id, body)

@router.put("/models/{_id}")
async def put_model_id(_id: str, body: ModelRequest):
    return await put_model_by_id(_id, body)

@router.get("/models")
async def get_model_(greater: int, lower: int):
    return await get_model(greater, lower)
