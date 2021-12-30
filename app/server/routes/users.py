from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.controllers.crud import *

from server.database import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)
from server.models.main import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel,
)

router = APIRouter()