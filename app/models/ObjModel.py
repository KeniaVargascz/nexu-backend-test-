from pydantic import BaseModel
from typing import Optional

class ModelRequest(BaseModel):
    name: str
    average_price: Optional[int] = None
