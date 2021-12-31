from fastapi import FastAPI
from .models.main import Item
from fastapi.encoders import jsonable_encoder
from .controllers import mongoExa
from .models.main import *
from .controllers.crud import *
from .routes.users import *
from .routes.users import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/user")

# Home page
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!", "status":200, "success":True}

# Create queries
@router.post("/", response_description="user data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "user added successfully.")

# Read queries
@router.get("/", response_description="users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")

@router.get("/{id}", response_description="user data retrieved")
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "user data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "user doesn't exist.")

# Update queries
@router.put("/{id}")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "user with ID: {} name update is successful".format(id),
            "user name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )

# Delete queries
@router.delete("/{id}", response_description="user data deleted from the database")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "user with ID: {} removed".format(id), "user deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "user with id {0} doesn't exist".format(id)
    )
    
# @app.post('/v1/loggingForm')
# async def login_info(item : Item):
    
#     payload = jsonable_encoder(item)
    
#     name = payload["name"]
#     email = payload["email"]
#     age = payload["age"]
#     languages = payload["languages"]
#     password = payload["password"]

#     myStorage = mongoExa.add_query(name, email, age, languages, password)
    
#     return myStorage