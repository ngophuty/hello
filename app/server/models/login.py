from fastapi import FastAPI,Query,Path
from enum import Enum
from typing import Union,Optional,List
from pydantic import BaseModel


class User(BaseModel):
    username : str
    password : str

class database(BaseModel):
    username : str = "ngophuty123"
    password : str = "123456"

class infor(BaseModel):
    name :str = ""
    age : int
    job : str
    interest : Optional[str]

