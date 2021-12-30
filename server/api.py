from fastapi import FastAPI
from .models.main import Item
from fastapi.encoders import jsonable_encoder
from .controllers import mongoExa

app = FastAPI()

@app.post('/v1/loggingForm')
def login_info(item : Item):
    
    payload = jsonable_encoder(item)
    
    name = payload["name"]
    email = payload["email"]
    age = payload["age"]
    languages = payload["languages"]
    password = payload["password"]

    myStorage = mongoExa.add_query(name, email, age, languages, password)
    
    return myStorage