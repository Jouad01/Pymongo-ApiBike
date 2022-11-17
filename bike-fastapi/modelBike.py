import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Bicycle(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    booking : Optional[bool] = False
    price : Optional[float] = 0.0
    material : Optional[str] = None
    components : Optional[bool] = False
    typeBike : Optional[str] = None
    year : Optional[int] = 0


    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "id": "f1f1f1f1-f1f1-",
                "booking": False,
                "price": 200,
                "material": "Carbono",
                "components": True,
                "typeBike": "city",
                "year": 2019
            }
        }

class BicycleUpdate(BaseModel):
    material : Optional[str] = None
    components : Optional[bool] = False
    typeBike : Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "material": "Carbono",
                "components": True,
                "typeBike": "city",
            }
        }
    