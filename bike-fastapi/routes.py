from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from modelBike import Bicycle, BicycleUpdate

router = APIRouter()

# Here is the post for create a new bike
@router.post("/", response_description="Add new bike", status_code=status.HTTP_201_CREATED, response_model=Bicycle)
def create_bike(request: Request, bike: Bicycle = Body(...)):
    bike = jsonable_encoder(bike)
    new_bike = request.app.database["Bicycle"].insert_one(bike)
    create_bike = request.app.database["Bicycle"].find_one({"_id": new_bike.inserted_id})
    return create_bike

# Here is the get all bikes
@router.get("/", response_description="List all Bicycle", response_model=List[Bicycle])
def list_Bicycle(request: Request):
    Bicycle = list(request.app.database["Bicycle"].find(limit = 100))
    return Bicycle

# Here is the get by id 
@router.get("/{id}", response_description="Get a single bike", response_model=Bicycle)
def show_bike(id: str, request: Request):
    if (bike := request.app.database["Bicycle"].find_one({"_id": id})) is not None:
        return bike
    raise HTTPException(status_code=404, detail=f"Bike {id} not found")

# Here is the put of the bike
@router.put("/{id}", response_description="Update a bike", response_model=Bicycle)
def update_bike(id: str, request: Request, bike: BicycleUpdate = Body(...)):
    if (existing_bike := request.app.database["Bicycle"].find_one({"_id": id})) is not None:
        # This loop is to update the bike. key is the name of the field and value is the value of the field
        # if the value is not None, the value is updated
        bike = {k: v for k, v in bike.dict().items() if v is not None}
        update_result = request.app.database["Bicycle"].update_one({"_id": id}, {"$set": bike})
        if update_result.modified_count == 1:
            if (updated_bike := request.app.database["Bicycle"].find_one({"_id": id})) is not None:
                return updated_bike
    raise HTTPException(status_code=404, detail=f"Bike {id} not found")

# Here is the delete 
@router.delete("/{id}", response_description="Delete a bike")
def delete_bike(id: str, request: Request):
    delete_result = request.app.database["Bicycle"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Bicycle {id} not found")