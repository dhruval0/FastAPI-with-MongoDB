from pydantic import BaseModel
from typing import List, Optional

class Item(BaseModel):
    name : str
    email : str
    age : int
    languages : List[str]
    password : str