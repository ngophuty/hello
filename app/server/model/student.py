from doctest import Example
import email
from msilib import schema
from re import I
from typing import Optional
from urllib.parse import scheme_chars
from pydantic import BaseModel,EmailStr,Field



class StudentSchema(BaseModel):
    fullname : str = Field(...)
    email : EmailStr = Field(...)
    course_of_study : str =Field(...)
    year: int =Field(...,gt=0,lt=4)
    gpa : float =Field(...,le=4.0)

    class Config:
        schema_extra = {
            "example" : {
                "fullname" : "Ngo phu ty",
                "email" : "ngophuty@hcmut.edu.vn",
                "course_of_study" : "hello word",
                "year" : 3,
                "gpa"  : 3.5,

            }
        }


class UpdateStudentModel(BaseModel):
    fullname : Optional[str]
    email : Optional[EmailStr]
    course_of_study : Optional[str]
    year: Optional[int]
    gpa : Optional[float]

def ResponseModel(data,messgae):
    return {
        "data": [data],
        "code":200,
        "message" : messgae
    }
def ErrorResponseModel(error,code,message):
    return {
        "error":error,
        "code": code,
        "message":message
    }
