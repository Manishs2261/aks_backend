from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from bson import ObjectId

class ProductModel(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    price: float
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


class ProductCreateRequest(BaseModel):
    name: str
    price: float
