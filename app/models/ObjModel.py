from pydantic import BaseModel
from typing import Optional

class ModelRequest(BaseModel):
    name: str | None = None
    average_price: int | None = None
    brand_name: str | None = None
